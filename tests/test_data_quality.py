import csv
from pathlib import Path

RAW = Path("data/raw")


def test_customer_ids_are_unique():

    with open(
        RAW / "customers.csv",
        newline="",
        encoding="utf-8"
    ) as file:

        rows = list(csv.DictReader(file))

    customer_ids = [
        row["customer_id"]
        for row in rows
    ]

    assert len(customer_ids) == len(set(customer_ids))


def test_sales_have_valid_customer_ids():

    with open(
        RAW / "customers.csv",
        newline="",
        encoding="utf-8"
    ) as file:

        customer_ids = {
            row["customer_id"]
            for row in csv.DictReader(file)
        }

    with open(
        RAW / "sales.csv",
        newline="",
        encoding="utf-8"
    ) as file:

        sales = list(csv.DictReader(file))

    assert all(
        row["customer_id"] in customer_ids
        for row in sales
    )