from time import perf_counter

from ingestion.config import Config
from ingestion.csv_loader import CSVLoader
from ingestion.database import DatabaseManager
from ingestion.logger import LoggerManager
from ingestion.weather_loader import WeatherLoader


def run_pipeline():

    pipeline_start = perf_counter()

    config = Config()

    database = DatabaseManager(config)

    logger_manager = LoggerManager(config)

    logger = logger_manager.get_logger("Pipeline")

    if not database.test_connection():
        logger.error("Database connection failed.")
        return []

    logger.info("=" * 60)
    logger.info("Starting Data Ingestion Pipeline")
    logger.info("=" * 60)

    csv_loader = CSVLoader(
        config=config,
        database=database,
        logger=logger_manager,
    )

    weather_loader = WeatherLoader(
        config=config,
        database=database,
        logger=logger_manager,
    )

    results = []

    total_rows = 0

    successful = 0

    failed = 0

    # -----------------------------
    # CSV Sources
    # -----------------------------

    for source in config.tables["tables"]:

        result = csv_loader.load(source)

        results.append(result)

        total_rows += result.rows_loaded

        if result.status == "SUCCESS":
            successful += 1
        else:
            failed += 1

    # -----------------------------
    # Weather API
    # -----------------------------

    weather_result = weather_loader.load(
        latitude=-23.5505,
        longitude=-46.6333,
    )

    results.append(weather_result)

    total_rows += weather_result.rows_loaded

    if weather_result.status == "SUCCESS":
        successful += 1
    else:
        failed += 1

    pipeline_execution_time = (
        perf_counter() - pipeline_start
    )

    logger.info("=" * 60)
    logger.info("INGESTION SUMMARY")
    logger.info("=" * 60)

    for result in results:

        logger.info(
            f"{result.source:<25}"
            f"{result.status:<10}"
            f"{result.rows_loaded:>10,} rows"
        )

    logger.info("-" * 60)
    logger.info(f"Successful Sources : {successful}")
    logger.info(f"Failed Sources     : {failed}")
    logger.info(f"Total Rows Loaded  : {total_rows:,}")
    logger.info(
        f"Execution Time     : "
        f"{pipeline_execution_time:.2f} sec"
    )
    logger.info("=" * 60)

    return results