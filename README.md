# Titanic GCP Batch Pipeline

**Airflow DAG that ingests Titanic CSV data into BigQuery, cleans and transforms it, computes statistics, and validates the result — with Terraform-managed GCP infrastructure.**

## What This Does

A 7-task Airflow DAG processes the Titanic dataset through a batch pipeline:

```
GCS (CSV) → BigQuery (raw) → clean → rename columns → statistics → aggregation queries → validation (pass/fail branch)
```

The infrastructure (VPC, subnet, NAT, compute instance) is defined as Terraform IaC.

## Architecture

| Layer | Tool | Role |
|-------|------|------|
| Orchestration | Apache Airflow | DAG-based batch pipeline (7 tasks) |
| Storage | Google Cloud Storage | CSV landing zone |
| Warehouse | Google BigQuery | Structured analytics tables |
| Infrastructure | Terraform | VPC, subnet, Cloud Router, NAT, compute instance |

## DAG Tasks

1. **Ingest** — `GCSToBigQueryOperator` loads CSV from GCS
2. **Clean** — removes duplicate rows
3. **Rename** — standardises column names, casts types
4. **Statistics** — `df.describe()` → BigQuery table
5. **Aggregation** — 4 CTEs: gender counts, survival by class, age distribution, survival by gender
6. **Validation** — `BigQueryCheckOperator` row-count check
7. **Branch** — pass/fail paths after validation

## Prerequisites

- GCP project with BigQuery and GCS enabled
- Apache Airflow 2.x environment (Cloud Composer or self-hosted)
- Terraform for infrastructure provisioning

## Tech Stack

Python · Apache Airflow · Google Cloud Platform (GCS, BigQuery) · Terraform

## Data

Uses the [Titanic dataset](https://www.kaggle.com/c/titanic) — this is an architecture demo, not a production data source.
