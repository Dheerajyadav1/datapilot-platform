import pandas as pd

from ingestion.database import DatabaseManager
from ingestion.logger import LoggerManager


class DatabaseReader:
    """
    Generic PostgreSQL reader.
    """

    def __init__(
        self,
        database: DatabaseManager,
        logger: LoggerManager,
    ):
        self.engine = database.get_engine()
        self.logger = logger.get_logger(
            self.__class__.__name__
        )

    def read(
        self,
        schema: str,
        table: str,
    ) -> pd.DataFrame:

        self.logger.info(
            f"Reading {schema}.{table}"
        )

        query = f"""
        SELECT *
        FROM {schema}.{table}
        """

        return pd.read_sql(
            query,
            self.engine,
        )