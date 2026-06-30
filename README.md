# 🚀 Agentic Data Platform

An end-to-end modern data engineering platform built using **Python, PostgreSQL, Apache Airflow, Docker, and dbt**.

The project demonstrates how to build a production-style data platform capable of ingesting data from multiple sources, transforming it through a layered warehouse architecture, validating data quality, and orchestrating the complete pipeline.

---

## ✨ Current Features

- CSV Data Ingestion
- Weather API Integration (Open-Meteo)
- PostgreSQL Data Warehouse
- Multi-layer Architecture
  - Raw
  - Bronze
  - Silver
  - Gold
- Data Validation Framework
- Centralized Configuration Management
- Logging & Error Handling
- Apache Airflow Orchestration
- dbt Transformations
- dbt Data Quality Tests
- Dockerized Development Environment

---

## 🏗️ Project Architecture

```
CSV Files + Weather API
          │
          ▼
    Ingestion Layer
          │
          ▼
     PostgreSQL (Raw)
          │
          ▼
   Bronze → Silver
          │
          ▼
      dbt Staging
          │
          ▼
      Gold Models
          │
          ▼
     Data Quality Tests
          │
          ▼
        Airflow DAG
```

---

## 🛠️ Tech Stack

- Python 3.11
- PostgreSQL
- SQLAlchemy
- Pandas
- Apache Airflow
- dbt
- Docker & Docker Compose
- pgAdmin
- HTTPX
- PyYAML

---

## 📂 Project Structure

```
agentic-data-platform/

├── app/
├── config/
├── dags/
├── dbt_project/
├── docker/
├── ingestion/
├── tests/
├── warehouse/
├── docker-compose.yml
├── pyproject.toml
└── README.md
```

---

## 🚀 Running the Project

Clone the repository

```bash
git clone https://github.com/<your-username>/agentic-data-platform.git
```

Start Docker services

```bash
docker compose up -d
```

Run the ingestion pipeline

```bash
python ingestion/pipeline.py
```

Run the warehouse pipeline

```bash
python warehouse/pipeline.py
```

Run dbt models

```bash
cd dbt_project

dbt run

dbt test
```

Launch Airflow

```
http://localhost:8080
```

Launch pgAdmin

```
http://localhost:5050
```

---

## 📊 Current Pipeline

```
CSV + API
    │
    ▼
Ingestion
    │
    ▼
Raw Layer
    │
    ▼
Bronze Layer
    │
    ▼
Silver Layer
    │
    ▼
Gold Layer (dbt)
    │
    ▼
Data Quality Tests
    │
    ▼
Airflow Orchestration
```

---

## ⚠️ Known Data Quality Issue

The Olist dataset contains **3 records without payment information**.

The `dbt` test

```
not_null_fact_sales_payment_value
```

fails intentionally to demonstrate automated data quality validation rather than silently masking source data issues.

---

## 🚧 Upcoming Features

- Streamlit Analytics Dashboard
- AI Analytics Assistant
- RAG over Warehouse Metadata
- Natural Language to SQL
- Interactive Business Reports
- CI/CD Pipeline
- Cloud Deployment

---

## 📅 Project Status

✅ Milestone 1 — Project Setup

✅ Milestone 2 — Data Ingestion

✅ Milestone 3 — Database Layer

✅ Milestone 4 — Validation Framework

✅ Milestone 5 — Production Ingestion Pipeline

✅ Milestone 6 — Data Warehouse

✅ Milestone 7 — Airflow + dbt Integration

🚧 Milestone 8 — Analytics Dashboard (In Progress)

---

## 👨‍💻 Author

**Dheeraj Yadav**

B.Tech CSE | IIIT Bhagalpur

Aspiring Data Engineer & Data Scientist