from abc import ABC, abstractmethod
from time import perf_counter

import pandas as pd

from ingestion.config import Config
from ingestion.database import DatabaseManager
from ingestion.logger import LoggerManager
from warehouse.reader import DatabaseReader
from warehouse.writer import DatabaseWriter


class BaseTransformer(ABC):

    SOURCE_SCHEMA = ""
    TARGET_SCHEMA = ""

    SOURCE_TABLE = ""
    TARGET_TABLE = ""

    def __init__(
        self,
        config: Config,
        database: DatabaseManager,
        logger: LoggerManager,
    ):
        self.config = config

        self.logger = logger.get_logger(
            self.__class__.__name__
        )

        self.reader = DatabaseReader(
            database=database,
            logger=logger,
        )

        self.writer = DatabaseWriter(
            config=config,
            database=database,
            logger=logger,
        )

    def run(self):

        start = perf_counter()

        self.logger.info("=" * 60)
        self.logger.info(
            f"Running {self.__class__.__name__}"
        )
        self.logger.info("=" * 60)

        dataframe = self.reader.read(
            schema=self.SOURCE_SCHEMA,
            table=self.SOURCE_TABLE,
        )

        dataframe = self.transform(
            dataframe
        )

        self.writer.write(
            dataframe=dataframe,
            schema=self.TARGET_SCHEMA,
            table=self.TARGET_TABLE,
        )

        execution_time = (
            perf_counter() - start
        )

        self.logger.info(
            f"{len(dataframe):,} rows transformed."
        )

        self.logger.info(
            f"Execution Time : "
            f"{execution_time:.2f} sec"
        )

        self.logger.info("=" * 60)

        return dataframe

    @abstractmethod
    def transform(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Child classes implement transformation.
        """
        ...