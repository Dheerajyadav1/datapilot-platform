# 🚀 DataPilot

[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![PostgreSQL 15](https://img.shields.io/badge/PostgreSQL-15-blue?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-2.7%2B-red?logo=apacheairflow&logoColor=white)](https://airflow.apache.org/)
[![dbt Core 1.6+](https://img.shields.io/badge/dbt--core-1.6%2B-orange?logo=dbt&logoColor=white)](https://www.getdbt.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Docker Compose](https://img.shields.io/badge/Docker%20Compose-Ready-blue?logo=docker&logoColor=white)](https://www.docker.com/)

An end-to-end, production-grade Modern Data Stack (MDS) and Agentic AI assistant platform. The platform automates data ingestion from diverse sources (CSVs & REST APIs), orchestrates complex transformation flows via a structured **Medallion Data Warehouse Architecture**, conducts automated data-quality testing, and exposes a high-fidelity **Business Intelligence (BI) Dashboard** coupled with a **Generative AI Data Assistant (RAG & Natural Language to SQL)**.

Designed to demonstrate industry-standard data engineering best practices—including star-schema modeling, pipeline orchestration, idempotent transformations, metadata-driven query generation, and localized caching.

---

## 🏗️ Platform Architecture

The platform separates ingestion, warehouse processing, orchestration, visualization, and agentic AI layers:

```
                                      [ PLATFORM ARCHITECTURE ]
                                      
  [ Sources ]            [ Ingestion & Staging ]             [ Warehouse Layer (Medallion) ]
  ┌───────────┐          ┌──────────────────────┐          ┌──────────────────────────────────┐
  │ E-Commerce│ ───────> │ CSV Loaders (Python) │ ───────> │ postgres.bronze                  │
  │ CSV Data  │          └──────────────────────┘          │   - Raw records with load audit  │
  └───────────┘                                            └──────────────────────────────────┘
  ┌───────────┐          ┌──────────────────────┐                           │
  │ Open-Meteo│ ───────> │ HTTPX Ingestion API  │ ───┐                      │ Python transformations
  │ REST API  │          └──────────────────────┘    │                      ▼
  └───────────┘                                      │     ┌──────────────────────────────────┐
                                                     ├─>   │ postgres.silver                  │
                                                     │     │   - Schema-conformed & typed     │
                                                     │     │   - Deduplicated & cleaned           │
                                                     │     └──────────────────────────────────┘
                                                     │                      │
                                                     │                      │ dbt Core transformations
                                                     │                      ▼
                                                     │     ┌──────────────────────────────────┐
                                                     └─>   │ postgres.gold (Star Schema)      │
                                                           │   - dim_customers, dim_products  │
                                                           │   - fact_sales, fact_weather         │
                                                           └──────────────────────────────────┘
                                                                            │
 ┌──────────────────────────────────────────────────────────────────────────┴──────────────────────────────────────┐
 │                                                                                                                 │
 ▼                                                                                                                 ▼
[ Orchestration & Testing ]                                                                               [ Analytics & AI Assistant ]
┌──────────────────────────────┐                                                                          ┌───────────────────────────┐
│ Apache Airflow (Docker)      │                                                                          │ Streamlit Web BI App      │
│   - Daily Ingestion DAG      │ <──────────────────────────────────────────────────────────────────────> │  - KPI Metrics (Cached)   │
│   - dbt Run & Test Tasks     │                                                                          │  - Sales & Weather charts │
└──────────────────────────────┘                                                                          └───────────────────────────┘
                                                                                                                        │
                                                                                                                        ▼
                                                                                                          ┌───────────────────────────┐
                                                                                                          │ Agentic AI Orchestrator   │
                                                                                                          │  - NLP-to-SQL Generator   │
                                                                                                          │  - Document RAG (FAISS)   │
                                                                                                          │  - Airflow Health Checker │
                                                                                                          └───────────────────────────┘
```

---

## 🛠️ Technology Stack & Rationale

* **Python 3.11**: Core language for writing custom ingestion pipelines, data validation scripts, and Streamlit components.
* **PostgreSQL 15**: Central relational data warehouse storing the three medallion layers (`bronze`, `silver`, `gold`).
* **dbt (Data Build Tool) Core**: Performs modular SQL transformations inside the data warehouse. Builds models in dependency order, manages materialization strategies (views/incremental tables), and executes data-quality constraint checks.
* **Apache Airflow**: Workflow orchestrator managing and sequencing ingestion tasks, database preparation scripts, and dbt models.
* **Docker & Compose**: Containers ensure a reproducible, isolated local environment for PostgreSQL, pgAdmin, and Apache Airflow.
* **Streamlit**: Renders interactive business dashboards with responsive layouts, lazy-loaded charts, and a custom stateful chat assistant UI.
* **Google Gemini AI SDK**: Powers natural language parsing, SQL query generation, and document retrieval summarization.
* **FAISS (Facebook AI Similarity Search)**: Implements local vector similarity indexes to store and retrieve repository metadata and architectural specifications for RAG.

---

## 📂 Repository Structure

The codebase is organized in a highly modular, decoupled architecture following clean separation of concerns:

```
agentic-data-platform/
├── agent_config/             # Configuration package for global settings & database parameters
│   └── settings.py           # Dotenv parser loading database URLs, model keys, and directory paths
├── agents/                   # Modular Agentic AI Framework
│   ├── core/                 # Orchestrator core
│   │   ├── context.py        # Shared AgentContext tracking conversation traces & execution details
│   │   ├── orchestrator.py   # Intent router directing traffic to appropriate sub-agents
│   │   ├── planner.py        # Dynamically plans sequence of sub-agent calls
│   │   └── registry.py       # Holds registered tools and sub-agents
│   ├── sql/                  # Conversational Database Agent (SQL Generator, Validator, Parser)
│   ├── analytics/            # Dynamic chart and reporting agent
│   ├── knowledge/            # Architecture RAG Agent retrieving documentation context
│   ├── pipeline/             # Pipeline Agent calling Airflow APIs for system health status
│   ├── tools/                # Extensible tools (MetadataTool, DatabaseTool, PipelineTool)
│   └── rag/                  # Document loaders, embeddings parser, and FAISS Vector Store wrapper
├── app/                      # Streamlit Analytics BI Application
│   ├── Home.py               # Application landing page & high-level business KPI metrics
│   ├── app_config.py         # Visual styles, page icons, and page config settings
│   ├── pages/                # Multi-page dashboard modules
│   │   ├── 1_Executive_Dashboard.py
│   │   ├── 2_Sales_Analytics.py
│   │   ├── 3_Customer_Analytics.py
│   │   ├── ...
│   │   └── 8_AI_Assistant.py # Conversational AI Assistant UI with tracing toggles
│   ├── services/             # Database fetcher services (Sales, Products, Sellers, Weather)
│   └── components/           # Custom BI design elements (MetricCards, Footer, Charts, Sidebar)
├── dags/                     # Apache Airflow DAG definitions
├── dbt_project/              # dbt Core projects (Models, Sources, Constraints, and schema specs)
├── docker/                   # Dockerfiles, healthcheck scripts, and container configs
├── ingestion/                # Raw CSV and Weather REST API ingestion logic
├── warehouse/                # Database setup, table creation scripts, and migration files
├── docker-compose.yml        # Orchestrates Local PostgreSQL + Airflow + pgAdmin stack
└── requirements.txt          # Python dependency freeze
```

---

## ⚙️ Medallion Schema Architecture

DataPilot uses a standard four-tier Medallion architecture to ingest, clean, and model Brazilian E-commerce (`Olist`) and weather data:

1. **Bronze Layer (`gold.bronze_*`)**:
   * Appends raw, untouched records directly from CSV files and the Open-Meteo REST API.
   * Includes structural metadata tracking `ingested_at` timestamps and `source_file` paths to establish a reliable data audit trail.

2. **Silver Layer (`gold.silver_*`)**:
   * Cleans raw input: sanitizes column names, checks schema conformity, handles data casting (e.g., standardizing currency, zip codes, and datetimes).
   * Drops duplicates to ensure transactional records (orders, payments, products) conform to primary-key integrity.

3. **Gold Layer (`gold.fact_*` & `gold.dim_*`)**:
   * Uses **Dimensional Modeling (Kimball Star Schema)** to enable high-speed analytics queries.
   * **Dimensions**: `dim_customers` (buyers, locations), `dim_products` (category translations, weights, sizes), `dim_sellers` (vendor states).
   * **Facts**: `fact_sales` (orders, payment values, timestamps), `fact_weather` (temperature, humidity, precipitation).
   * **Marts**: `sales_summary` (aggregated daily trends for business KPI charts).

---

## 🤖 Agentic AI Framework

Milestone 9 integrates a comprehensive, modular Agentic Framework into the data platform. Instead of a single massive prompt,DataPilot uses a routed, multi-agent orchestrator:

* **Intent Routing**: The orchestrator (`AgentOrchestrator`) analyzes incoming natural language questions and routes them to target agents.
* **SQL Agent**:
  * **Schema Injection**: Uses `MetadataTool` to read active table definitions and column details from the active medallion schema (Gold, Silver, Bronze), avoiding schema hallucination.
  * **Safety Validation**: Passes generated queries to a `validator.py` AST compiler to block destructive operations (`DROP`, `DELETE`, `INSERT`, `ALTER`) and SQL injections.
  * **Visual Execution**: Streamlit executes the query via `DatabaseTool` and formats the outputs directly into interactive tables.
* **Knowledge Agent (RAG)**:
  * Uses `google-genai` embeddings to index project documentation, database guides, and architectural readmes into a localized FAISS database.
  * Provides accurate explanations on design patterns (e.g., "Explain the Medallion Architecture used in this project").
* **Pipeline Agent**:
  * Calls Airflow REST APIs (`http://localhost:8080/api/v1/health`) and parses local dbt execution logs.
  * Generates diagnostic reports (e.g., "Is my Airflow pipeline healthy?").

---

## 🚀 Installation & Local Execution

### Prerequisites
* **Docker & Compose**: Ensure docker daemon is running.
* **Python 3.11**: local runtime virtual environment.

### 1. Launch Platform Containers
Spin up the PostgreSQL database, pgAdmin, and Apache Airflow container stack:
```bash
docker compose up -d
```
Check that the containers are healthy:
```bash
docker compose ps
```

### 2. Setup Local Python Virtual Environment
Navigate to the root directory and configure dependencies:
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run Database Ingestions
Initialize schemas and load CSV datasets + weather measurements into PostgreSQL:
```bash
# Prepare database schemas (bronze, silver, gold)
python warehouse/pipeline.py

# Ingest raw CSV data & fetch Open-Meteo REST API data
python ingestion/pipeline.py
```

### 4. Build Gold Data Models (dbt Core)
Compile SQL models and execute data validations:
```bash
cd dbt_project
dbt run
dbt test
```

### 5. Build RAG Vector Index
Generate the local FAISS index by scraping workspace metadata and documentation files:
```bash
cd ..
python -m agents.rag.load_index
```

### 6. Launch Streamlit BI Dashboard
Launch the web interface (listens on `http://localhost:8501`):
```bash
streamlit run app/Home.py
```

---

## 📈 Dashboard Showcase & BI Highlights

The BI application is designed to look like a modern dashboard (similar to PowerBI/Tableau) and implements performance-focused features:

* **Local Query Caching**: Implements a centralized caching tier (`st.cache_data` with a 10-minute TTL) wrapping PostgreSQL queries. This keeps dashboard loads under **~50ms** and avoids overloading the connection pool.
* **Dynamic Analytics Pages**:
  * **Executive Dashboard**: Displays core KPIs (Revenue, orders, customer acquisition, weather correlations) with visual status indicators.
  * **Customer & Seller Map**: Interactive spatial plots showing geographic distributions of transactions.
  * **Data Quality Auditing**: Real-time auditing comparing record counts between Bronze and Gold layers, highlighting pipeline synchronizations.
* **Interactive AI Assistant**: Features collapsible **Execution Traces** detailing intent classification, RAG source documents, execution runtimes, and auto-generated SQL.

---

## 👨‍💻 Author

**Dheeraj Yadav**  
*B.Tech in Computer Science & Engineering | IIIT Bhagalpur*  
*Specialization: Data Engineering, Analytics Platform Architecture, Agentic AI Systems*  
[LinkedIn](https://www.linkedin.com/in/dheerajyadav1/) | [GitHub](https://github.com/Dheerajyadav1)
