# 🚀 Agentic Data Platform

> **Building an AI-Native Data Platform from Scratch**

A production-inspired data engineering project that combines modern ETL pipelines, a cloud-ready data warehouse, orchestration, analytics engineering, vector search, and AI-powered querying into a unified platform.

The goal of this project is to demonstrate how modern Data Engineering is evolving from traditional ETL pipelines into **AI-native data platforms**, where Large Language Models can understand business metadata, generate SQL safely, diagnose pipeline failures, and enable natural language analytics.

---

## ✨ Project Goals

This project demonstrates how to build a modern data platform from scratch using industry-standard tools.

It includes:

- Configuration-driven data ingestion
- Dockerized infrastructure
- PostgreSQL Data Warehouse
- Weather API ingestion
- Structured logging
- Airflow orchestration *(Upcoming)*
- dbt transformations *(Upcoming)*
- Vector embeddings *(Upcoming)*
- Gemini-powered Text-to-SQL *(Upcoming)*
- Streamlit analytics application *(Upcoming)*

---

# 🏗️ Architecture

```text
                    External Data Sources
              ┌────────────────────────────┐
              │                            │
              │    Olist CSV Dataset       │
              │    Open-Meteo Weather API  │
              └──────────────┬─────────────┘
                             │
                             ▼
                  Generic Ingestion Layer
              ┌────────────────────────────┐
              │  CSV Loader                │
              │  Weather Loader            │
              │  Config Manager            │
              │  Logger                    │
              └──────────────┬─────────────┘
                             │
                             ▼
                 PostgreSQL Data Warehouse
              ┌────────────────────────────┐
              │ raw schema                 │
              │ staging schema             │
              │ marts schema               │
              │ embeddings schema          │
              └──────────────┬─────────────┘
                             │
                             ▼
                Airflow Orchestration
                     (Coming Soon)
                             │
                             ▼
                     dbt Transformations
                     (Coming Soon)
                             │
                             ▼
                  Gemini Text-to-SQL Agent
                     (Coming Soon)
                             │
                             ▼
                    Streamlit Dashboard
                     (Coming Soon)
```

---

# 📂 Repository Structure

```
agentic-data-platform/

├── docker/
│   └── postgres/
│
├── ingestion/
│   ├── config/
│   ├── models/
│   ├── config.py
│   ├── csv_loader.py
│   ├── database.py
│   ├── logger.py
│   ├── main.py
│   └── weather_loader.py
│
├── tests/
│
├── data/
│
├── docs/
│
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# ⚙️ Technology Stack

| Category | Technologies |
|-----------|--------------|
| Language | Python |
| Warehouse | PostgreSQL 17 |
| Database Extension | pgvector |
| Administration | pgAdmin |
| Containerization | Docker & Docker Compose |
| Data Processing | Pandas |
| HTTP Client | httpx |
| ORM | SQLAlchemy |
| Configuration | YAML |
| Logging | Python Logging |
| API | Open-Meteo |
| Version Control | Git & GitHub |

---

# 📊 Data Sources

## 1. Olist Brazilian E-Commerce Dataset

Used to simulate a real-world transactional data warehouse.

Includes:

- Customers
- Orders
- Order Items
- Products
- Sellers
- Reviews
- Payments
- Geolocation

---

## 2. Open-Meteo Weather API

Used to demonstrate API ingestion into the warehouse.

Current metrics:

- Temperature
- Humidity
- Precipitation
- Wind Speed

---

# ✅ Current Features

- Configuration-driven ingestion
- Generic CSV Loader
- Open-Meteo API ingestion
- PostgreSQL warehouse
- Structured logging
- Dockerized infrastructure
- Reusable database manager
- Unified ingestion pipeline

---

# 🚧 Project Roadmap

## ✅ Milestone 1

Repository Setup

---

## ✅ Milestone 2

Infrastructure

- Docker
- PostgreSQL
- pgvector
- pgAdmin

---

## ✅ Milestone 3

Data Ingestion

- Generic CSV Loader
- Weather API Loader
- Unified Pipeline

---

## 🔄 Milestone 4

Airflow Orchestration

- DAGs
- Scheduling
- Retries
- Monitoring

---

## 🔄 Milestone 5

dbt Transformations

- Staging Models
- Mart Models
- Testing
- Documentation

---

## 🔄 Milestone 6

AI Layer

- Gemini Function Calling
- Text-to-SQL
- SQL Validation
- Vector Search

---

## 🔄 Milestone 7

Streamlit Dashboard

- Chat Interface
- SQL Display
- Analytics
- Visualizations

---

## 🔄 Milestone 8

Failure Diagnosis Agent

- Airflow Failure Analysis
- Root Cause Detection
- Slack Notifications

---

## 🔄 Milestone 9

Deployment

- End-to-End Docker Deployment
- Documentation
- Demo Video

---

# 🚀 Getting Started

## Clone

```bash
git clone https://github.com/Dheerajyadav1/agentic-data-platform.git

cd agentic-data-platform
```

---

## Create Environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Linux

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment

Create

```
.env
```

using

```
.env.example
```

---

## Start Docker

```bash
docker compose up -d
```

---

## Run Ingestion

```bash
python ingestion/main.py
```

---

# 🎯 Learning Objectives

This project demonstrates practical experience with:

- Data Engineering
- ETL Pipelines
- Docker
- PostgreSQL
- SQLAlchemy
- YAML Configuration
- Logging
- API Integration
- Data Warehousing
- Software Architecture
- AI-ready Data Platforms

---

# 📈 Future Enhancements

- Apache Airflow
- dbt
- ChromaDB / pgvector Embeddings
- Gemini Text-to-SQL Agent
- SQL Guardrails
- Failure Diagnosis Agent
- Streamlit Dashboard
- CI/CD Pipeline
- Unit Testing
- Integration Testing

---

# 🤝 Contributing

Contributions, ideas, and suggestions are welcome.

Feel free to fork the repository and open a Pull Request.

---

# 📄 License

This project is licensed under the MIT License.

---

# ⭐ Acknowledgements

- Olist Brazilian E-Commerce Dataset
- Open-Meteo
- PostgreSQL
- Apache Airflow
- dbt Labs
- Google Gemini