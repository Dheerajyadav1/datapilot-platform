from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

from ingestion.config import Config
from ingestion.database import DatabaseManager
from ingestion.logger import LoggerManager
from ingestion.weather_loader import WeatherLoader


def ingest_weather():
    """
    Load weather data from Open-Meteo API
    into PostgreSQL.
    """

    config = Config()

    database = DatabaseManager(config)

    logger_manager = LoggerManager(config)

    loader = WeatherLoader(
        config=config,
        database=database,
        logger=logger_manager,
    )

    result = loader.load(
        latitude=-23.5505,
        longitude=-46.6333,
    )

    return result.status


default_args = {
    "owner": "Dheeraj",
    "depends_on_past": False,
    "retries": 3,
    "retry_delay": timedelta(minutes=2),
}

with DAG(
    dag_id="weather_ingestion",
    description="Ingest weather data from Open-Meteo",
    default_args=default_args,
    start_date=datetime(2026, 6, 1),
    schedule="@hourly",
    catchup=False,
    tags=["weather", "ingestion"],
) as dag:

    ingest_weather_task = PythonOperator(
        task_id="ingest_weather",
        python_callable=ingest_weather,
    )