# src/config.py

import os

# -----------------------------
# Project Configuration
# -----------------------------

PROJECT_NAME = "Persona360"
PROJECT_VERSION = "1.0.0"

# -----------------------------
# Directory Configuration
# -----------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, "processed")

# -----------------------------
# Raw Data Files
# -----------------------------

CUSTOMERS_FILE = os.path.join(RAW_DATA_DIR, "customers.csv")
SALES_FILE = os.path.join(RAW_DATA_DIR, "sales.csv")
MARKETING_FILE = os.path.join(RAW_DATA_DIR, "marketing.csv")
SUPPORT_FILE = os.path.join(RAW_DATA_DIR, "support.csv")
WEB_EVENTS_FILE = os.path.join(RAW_DATA_DIR, "web_events.csv")

# -----------------------------
# Processed Output
# -----------------------------

CUSTOMER_360_FILE = os.path.join(
    PROCESSED_DATA_DIR,
    "customer_360.csv"
)

# -----------------------------
# AWS S3 Configuration
# -----------------------------

S3_BUCKET_NAME = os.getenv(
    "PERSONA360_S3_BUCKET",
    "persona360-demo"
)

S3_RAW_PREFIX = "raw/"
S3_PROCESSED_PREFIX = "processed/customer_360/"

# -----------------------------
# Spark Configuration
# -----------------------------

SPARK_APP_NAME = "Persona360_ETL"

# -----------------------------
# Data Quality Thresholds
# -----------------------------

MIN_ENGAGEMENT_SCORE = 10
HIGH_VALUE_REVENUE = 10000
HIGH_CHURN_RISK_SCORE = 10

# -----------------------------
# Logging Configuration
# -----------------------------

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")