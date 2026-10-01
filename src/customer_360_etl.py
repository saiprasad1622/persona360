from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    sum,
    count,
    avg,
    max,
    when,
    round
)

spark = (
    SparkSession.builder
    .appName("Persona360")
    .getOrCreate()
)

RAW_PATH = "data/raw/"
OUTPUT_PATH = "data/processed/customer_360"

# -------------------------
# Read source datasets
# -------------------------

customers = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(RAW_PATH + "customers.csv")
)

sales = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(RAW_PATH + "sales.csv")
)

marketing = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(RAW_PATH + "marketing.csv")
)

support = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(RAW_PATH + "support.csv")
)

web = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(RAW_PATH + "web_events.csv")
)

# -------------------------
# Sales aggregation
# -------------------------

sales_agg = (
    sales
    .filter(col("status") == "Completed")
    .groupBy("customer_id")
    .agg(
        round(sum("amount"), 2).alias("total_revenue"),
        count("sale_id").alias("total_orders"),
        round(avg("amount"), 2).alias("avg_order_value"),
        max("sale_date").alias("last_purchase_date")
    )
)

# -------------------------
# Marketing aggregation
# -------------------------

marketing_agg = (
    marketing
    .groupBy("customer_id")
    .agg(
        count("campaign_id").alias("campaign_contacts"),

        sum(
            when(col("engagement") == "Clicked", 1)
            .otherwise(0)
        ).alias("campaign_clicks"),

        sum(
            when(col("engagement") == "Opened", 1)
            .otherwise(0)
        ).alias("campaign_opens")
    )
)

# -------------------------
# Support aggregation
# -------------------------

support_agg = (
    support
    .groupBy("customer_id")
    .agg(
        count("ticket_id").alias("support_tickets"),

        round(
            avg("resolution_hours"), 2
        ).alias("avg_resolution_hours"),

        sum(
            when(col("status") == "Open", 1)
            .otherwise(0)
        ).alias("open_tickets")
    )
)

# -------------------------
# Web aggregation
# -------------------------

web_agg = (
    web
    .groupBy("customer_id")
    .agg(
        count("event_id").alias("web_events"),
        round(
            avg("duration_seconds"), 2
        ).alias("avg_web_duration_seconds")
    )
)

# -------------------------
# Customer 360
# -------------------------

customer_360 = (
    customers

    .join(sales_agg, "customer_id", "left")
    .join(marketing_agg, "customer_id", "left")
    .join(support_agg, "customer_id", "left")
    .join(web_agg, "customer_id", "left")

    .fillna(0)

    .withColumn(
        "engagement_score",

        round(
            col("campaign_clicks") * 10
            + col("campaign_opens") * 5
            + col("web_events") * 2
            + col("avg_web_duration_seconds") / 60,
            2
        )
    )

    # -------------------------
    # Persona classification
    # -------------------------

    .withColumn(
        "persona",

        when(
            (col("total_revenue") >= 20000)
            & (col("engagement_score") >= 20),
            "Loyal Champion"
        )

        .when(
            col("total_revenue") >= 10000,
            "High Value"
        )

        .when(
            col("engagement_score") >= 15,
            "Highly Engaged"
        )

        .when(
            (col("support_tickets") >= 2)
            | (col("open_tickets") >= 1),
            "At Risk"
        )

        .otherwise("Growth Opportunity")
    )

    # -------------------------
    # Churn risk
    # -------------------------

    .withColumn(
        "churn_risk",

        when(
            (col("open_tickets") > 0)
            | (col("engagement_score") < 10),
            "High"
        )

        .when(
            col("support_tickets") >= 2,
            "Medium"
        )

        .otherwise("Low")
    )
)

# -------------------------
# Select final columns
# -------------------------

final_df = customer_360.select(
    "customer_id",
    "customer_name",
    "city",
    "plan",
    "customer_type",
    "total_revenue",
    "total_orders",
    "avg_order_value",
    "last_purchase_date",
    "campaign_contacts",
    "campaign_clicks",
    "campaign_opens",
    "support_tickets",
    "avg_resolution_hours",
    "open_tickets",
    "web_events",
    "avg_web_duration_seconds",
    "engagement_score",
    "persona",
    "churn_risk"
)

final_df.show(truncate=False)

# -------------------------
# Write processed data
# -------------------------

(
    final_df
    .coalesce(1)
    .write
    .mode("overwrite")
    .option("header", True)
    .csv(OUTPUT_PATH)
)

print("Customer 360 dataset created successfully.")

spark.stop()