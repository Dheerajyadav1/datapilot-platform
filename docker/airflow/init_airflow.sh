#!/bin/bash
set -e

echo "Initializing Airflow..."

airflow db migrate

echo "Checking admin user..."

if airflow users list | grep -q "${AIRFLOW_USER}"; then
    echo "Admin user already exists."
else
    airflow users create \
        --username "${AIRFLOW_USER}" \
        --password "${AIRFLOW_PASSWORD}" \
        --firstname Dheeraj \
        --lastname Yadav \
        --role Admin \
        --email admin@example.com
fi

echo "Initialization complete."