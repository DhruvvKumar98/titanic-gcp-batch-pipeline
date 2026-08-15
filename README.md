# Real-Time Data Pipeline — Kafka + Airflow + GCP

**End-to-end streaming data pipeline that ingests, transforms, and serves data continuously — not in overnight batch jobs.**

## The Problem

Batch ETL pipelines create reporting delays. Dashboards refresh once a day, decisions are based on yesterday's data, and operational teams can't react to what's happening now. Real-time pipelines close that gap.

## What This Does

Demonstrates a production-grade streaming architecture:

```
Data source → Kafka (streaming) → Airflow (orchestration) → GCS → BigQuery → Looker Studio
```

A 7-task Airflow DAG handles ingestion, cleaning, transformation, statistics, and validation — with branching logic for pass/fail quality checks. Kafka runs parallel for real-time event streaming into BigQuery.

## Architecture

| Layer | Tool | Role |
|-------|------|------|
| Streaming | Apache Kafka | Producer/consumer event streaming |
| Orchestration | Apache Airflow | DAG-based ETL pipeline (7 tasks) |
| Storage | Google Cloud Storage | Raw data landing zone |
| Warehouse | Google BigQuery | Structured analytics tables |
| Infrastructure | Terraform | VPC, subnet, NAT, compute instance |
| Visualisation | Looker Studio | Dashboards from BigQuery |

## Key Features

- **Airflow DAG** with 7 chained tasks: ingest → clean → rename → stats → aggregation query → validation → branch
- **BigQuery validation** — automatic row-count check with pass/fail branching
- **Complex SQL** — 4 CTEs for gender, survival-by-class, age distribution, survival-by-gender aggregations
- **Terraform IaC** — full GCP infrastructure (VPC, private subnet, Cloud Router, NAT, compute instance)
- **Kafka streaming** — parallel real-time ingestion alongside batch pipeline

## Tech Stack

Python · Apache Kafka · Apache Airflow · Google Cloud Platform (GCS, BigQuery) · Terraform · Looker Studio

## About

Built by Dhruv Kumar — Business Analyst, Berlin.
