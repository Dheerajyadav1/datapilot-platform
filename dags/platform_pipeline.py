from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from ingestion.pipeline import run_pipeline as run_ingestion_pipeline
from warehouse.pipeline import run_pipeline as run_warehouse_pipeline


default_args = {
    "owner": "Dheeraj",
    "depends_on_past": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=2),
}


with DAG(
    dag_id="agentic_data_platform",
    description="End-to-End Agentic Data Platform",
    start_date=datetime(2026, 6, 1),
    schedule="@hourly",
    catchup=False,
    default_args=default_args,
    tags=[
        "platform",
        "ingestion",
        "warehouse",
        "dbt",
    ],
) as dag:

    ingestion_task = PythonOperator(
        task_id="ingestion_pipeline",
        python_callable=run_ingestion_pipeline,
    )

    warehouse_task = PythonOperator(
        task_id="warehouse_pipeline",
        python_callable=run_warehouse_pipeline,
    )

    dbt_run_task = BashOperator(
        task_id="dbt_run",
        bash_command="""
        export DBT_PROFILES_DIR=/opt/airflow/project/dbt_project
        cd /opt/airflow/project/dbt_project
        dbt run
        """,
    )

    dbt_test_task = BashOperator(
        task_id="dbt_test",
        bash_command="""
        export DBT_PROFILES_DIR=/opt/airflow/project/dbt_project
        cd /opt/airflow/project/dbt_project
        dbt test
        """,
    )

    (
        ingestion_task
        >> warehouse_task
        >> dbt_run_task
        >> dbt_test_task
    )