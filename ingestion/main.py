from ingestion.config import Config
from ingestion.database import DatabaseManager
from ingestion.logger import LoggerManager
from ingestion.csv_loader import CSVLoader


def main():

    # Initialize core components
    config = Config()

    database = DatabaseManager(config)

    logger_manager = LoggerManager(config)

    logger = logger_manager.get_logger("Main")

    # Test database connection
    if not database.test_connection():
        logger.error("Database connection failed. Exiting...")
        return

    logger.info("=" * 60)
    logger.info("Starting Olist CSV Ingestion")
    logger.info("=" * 60)

    loader = CSVLoader(
        config=config,
        database=database,
        logger=logger_manager,
    )

    results = []

    total_rows = 0

    for source in config.tables["tables"]:

        result = loader.load(source)

        results.append(result)

        total_rows += result.rows_loaded

    logger.info("=" * 60)
    logger.info("INGESTION SUMMARY")
    logger.info("=" * 60)

    successful = 0
    failed = 0

    for result in results:

        if result.status == "SUCCESS":
            successful += 1
        else:
            failed += 1

        logger.info(
            f"{result.source:<25}"
            f"{result.status:<10}"
            f"{result.rows_loaded:>10,} rows"
        )

    logger.info("-" * 60)
    logger.info(f"Successful Tables : {successful}")
    logger.info(f"Failed Tables     : {failed}")
    logger.info(f"Total Rows Loaded : {total_rows:,}")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()