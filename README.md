# Persona360 – Customer 360 Analytics Platform

Persona360 provides a 360-degree view of customers by consolidating data from
sales, marketing, customer support and web interactions.

## Business Problem

Customer information is distributed across multiple systems.

The objective of Persona360 is to integrate these touchpoints into a unified
customer-level dataset that can be used for segmentation, engagement analysis,
revenue analysis and churn-risk monitoring.

## Technology Stack

Python | PySpark | SQL | Power BI | Postman | AWS S3

## Architecture

CSV Sources
      ↓
AWS S3 Raw Layer
      ↓
PySpark ETL
      ↓
Customer 360 Dataset
      ↓
SQL Analytics
      ↓
Power BI Dashboard
      ↓
Customer Personas & Insights

## Data Sources

- Customer Master
- Sales Transactions
- Marketing Campaigns
- Support Tickets
- Website Events

## Key Metrics

- Total Revenue
- Total Orders
- Average Order Value
- Marketing Click Rate
- Marketing Open Rate
- Support Tickets
- Average Resolution Time
- Web Engagement
- Customer Persona
- Churn Risk

## Customer Personas

The project creates rule-based personas using customer revenue,
engagement and support activity.

Examples:

- Loyal Champion
- High Value
- Highly Engaged
- At Risk
- Growth Opportunity

## PySpark

PySpark is used to:

1. Read raw datasets
2. Clean and transform data
3. Aggregate customer activity
4. Join multiple datasets
5. Calculate engagement scores
6. Generate customer personas
7. Calculate churn-risk indicators
8. Write the processed Customer 360 dataset

## SQL

SQL is used for:

- Revenue analysis
- Customer segmentation
- Marketing analysis
- Support analysis
- Churn-risk analysis
- Customer-level reporting

## Power BI

Dashboard pages:

1. Executive Overview
2. Customer Personas
3. Customer Engagement
4. Support & Churn
5. Customer 360

## AWS S3

S3 is used as the conceptual data-lake layer:

raw/
processed/
archive/

## Postman

Postman collection demonstrates API testing for:

- Customer 360 profile
- Customer search
- Customer creation

## Dataset

All data included in this repository is synthetic and created for
demonstration purposes.

## Resume Project Description

### Persona360 – Customer 360 Analytics Platform

Developed a Customer 360 analytics solution using Python, PySpark, SQL,
Power BI, Postman and AWS S3 by integrating sales, marketing, support and
web-interaction data. Built PySpark ETL pipelines to create unified customer
profiles and calculated revenue, engagement, persona and churn-risk metrics.
Created Power BI dashboards for customer segmentation, revenue and engagement
analysis and designed an AWS S3 raw/processed data-lake structure.