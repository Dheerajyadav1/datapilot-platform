import pandas as pd

from ingestion.config import Config
from ingestion.database import DatabaseManager
from ingestion.logger import LoggerManager


class DatabaseWriter:
    """
    Generic PostgreSQL writer.
    """

    def __init__(
        self,
        config: Config,
        database: DatabaseManager,
        logger: LoggerManager,
    ):
        self.config = config

        self.engine = database.get_engine()

        self.logger = logger.get_logger(
            self.__class__.__name__
        )

    def write(
        self,
        dataframe: pd.DataFrame,
        schema: str,
        table: str,
    ):

        self.logger.info(
            f"Writing {len(dataframe):,} rows "
            f"to {schema}.{table}"
        )

        if self.config.settings["load"]["if_exists"] == "replace":
            from sqlalchemy import text
            with self.engine.begin() as connection:
                connection.execute(text(f"DROP TABLE IF EXISTS {schema}.{table} CASCADE"))

        dataframe.to_sql(
            name=table,
            schema=schema,
            con=self.engine,
            if_exists=self.config.settings["load"]["if_exists"],
            index=self.config.settings["load"]["index"],
            chunksize=self.config.settings["load"]["chunksize"],
            method=self.config.settings["load"]["method"],
        )

        self.logger.info(
            "Write completed successfully."
        )