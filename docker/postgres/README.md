# PostgreSQL Initialization

This directory contains the PostgreSQL initialization scripts for the **DataPilot** platform.

When the PostgreSQL container is started **for the first time** (i.e., when no existing database volume is present), Docker automatically executes every SQL file inside the `init/` directory in **alphabetical order**.

This ensures that every developer gets an identical database setup without performing any manual configuration.

---

## Directory Structure

```text
postgres/
├── README.md
└── init/
    ├── 01_extensions.sql
    ├── 02_schemas.sql
    └── 03_roles.sql
```

---

## Execution Order

### 01_extensions.sql

Enables the PostgreSQL extensions required by the platform.

Currently:

* `pgvector` — Stores and searches vector embeddings for the AI/RAG layer.

---

### 02_schemas.sql

Creates the logical warehouse schemas used throughout the project.

| Schema       | Purpose                                                                             |
| ------------ | ----------------------------------------------------------------------------------- |
| `raw`        | Stores data exactly as received from APIs and CSV files.                            |
| `staging`    | Contains cleaned and standardized data models created with dbt.                     |
| `marts`      | Stores business-ready analytical tables used for reporting and Text-to-SQL queries. |
| `embeddings` | Stores vector embeddings and metadata for the RAG pipeline.                         |

---

### 03_roles.sql

Creates database roles and permissions.

Currently it creates:

* `readonly_user`

This account has:

* Database connection permission
* Schema usage permission
* Read-only (`SELECT`) access

The Text-to-SQL agent will use this account so that AI-generated SQL cannot modify or delete data.

---

## Why Initialization Scripts?

Instead of manually creating schemas, extensions, and roles after every installation, Docker automatically provisions the database during initialization.

Benefits include:

* Reproducible environments
* Zero manual setup
* Version-controlled database configuration
* Easier onboarding for new contributors
* Consistent local development

---

## Important Note

Initialization scripts are executed **only once**, when PostgreSQL creates a new database cluster.

If the database volume already exists, these scripts are **not executed again**.

To re-run the initialization scripts during development:

```bash
docker compose down -v
docker compose up
```

> **Warning:** Removing the Docker volume deletes all database data.

---

## Future Enhancements

As the project evolves, additional initialization scripts may be added, such as:

* Creating application-specific users
* Configuring database indexes
* Loading seed/reference data
* Creating extensions required by future features

---

## Related Components

These scripts provide the foundation for the rest of the platform:

* **Milestone 3:** Data ingestion into the `raw` schema
* **Milestone 4:** Airflow orchestration
* **Milestone 5:** dbt transformations (`raw → staging → marts`)
* **Milestone 6:** AI/RAG layer using the `embeddings` schema
* **Milestone 7:** Streamlit analytics interface
