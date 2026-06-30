FROM apache/airflow:2.10.5-python3.11

USER root

RUN apt-get update && \
    apt-get install -y gcc g++ curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER airflow

ARG AIRFLOW_VERSION=2.10.5
ARG PYTHON_VERSION=3.11
ARG CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

COPY docker/airflow/requirements.txt /tmp/requirements.txt

# Install Airflow-related packages with Airflow constraints
RUN pip install --no-cache-dir \
    --constraint "${CONSTRAINT_URL}" \
    psycopg2-binary \
    requests \
    python-dotenv \
    PyYAML

# Install dbt WITHOUT Airflow constraints
RUN pip install --no-cache-dir \
    "dbt-postgres==1.10.2"

ENV PYTHONPATH="/opt/airflow/project:${PYTHONPATH}"