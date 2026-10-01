# Persona360 AWS S3 Architecture

## S3 Bucket

s3://persona360-demo/

## Folder Structure

persona360-demo/
│
├── raw/
│   ├── customers/
│   ├── sales/
│   ├── marketing/
│   ├── support/
│   └── web_events/
│
├── processed/
│   └── customer_360/
│
└── archive/

## Upload Raw Data

aws s3 cp data/raw/ \
s3://persona360-demo/raw/ \
--recursive

## Upload Processed Data

aws s3 cp data/processed/ \
s3://persona360-demo/processed/ \
--recursive

## Recommended Production Practices

- Enable S3 versioning
- Enable encryption
- Use IAM roles
- Keep raw data immutable
- Separate raw and processed data
- Partition large datasets by date
- Avoid storing AWS credentials in source code