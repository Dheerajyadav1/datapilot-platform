from time import perf_counter

import pandas as pd

from ingestion.config import Config
from ingestion.database import DatabaseManager
from ingestion.logger import LoggerManager
from ingestion.models.load_result import LoadResult
from ingestion.validation import (
    DataValidator,
    NoDuplicateRule,
    NotEmptyRule,
    RequiredColumnsRule,
)
from ingestion.validation.logger import ValidationLogger


class CSVLoader:
    """
    Generic CSV Loader

    Responsible for:
        - Reading table configuration
        - Reading CSV files
        - Validating data
        - Loading into PostgreSQL
    """

    def __init__(
        self,
        config: Config,
        database: DatabaseManager,
        logger: LoggerManager,
    ):
        self.config = config
        self.database = database
        self.engine = database.get_engine()

        self.logger = logger.get_logger(
            self.__class__.__name__
        )

        self.validation_logger = ValidationLogger(
            logger
        )

    def load(
        self,
        source_name: str,
    ) -> LoadResult:

        start_time = perf_counter()

        try:

            table_config = self._get_table_config(
                source_name
            )

            dataframe = self._read_csv(
                table_config["file"]
            )

            # 1. Deduplicate if configured
            drop_duplicates = self.config.settings["validation"]["drop_duplicates"]
            primary_key = table_config.get("primary_key", [])

            if drop_duplicates:
                subset = primary_key if primary_key else None
                dataframe = dataframe.drop_duplicates(subset=subset)

            # 2. Build dynamic validation rules
            rules = [
                NotEmptyRule(),
                RequiredColumnsRule(
                    list(dataframe.columns)
                ),
            ]

            # Only enforce uniqueness if the table has a primary key
            if primary_key:
                rules.append(NoDuplicateRule(columns=primary_key))

            validator = DataValidator(rules=rules)

            report = validator.validate(
                dataframe
            )

            self.validation_logger.log(
                report
            )

            if not report.passed:
                raise ValueError(
                    "CSV validation failed."
                )

            self._write_to_database(
                dataframe=dataframe,
                schema=table_config["schema"],
                table=table_config["table"],
            )

            execution_time = (
                perf_counter() - start_time
            )

            self.logger.info(
                f"{len(dataframe):,} rows loaded into "
                f"{table_config['schema']}.{table_config['table']}"
            )

            return LoadResult(
                source=source_name,
                table=table_config["table"],
                rows_loaded=len(dataframe),
                execution_time=execution_time,
                status="SUCCESS",
            )

        except Exception as error:

            execution_time = (
                perf_counter() - start_time
            )

            self.logger.exception(error)

            return LoadResult(
                source=source_name,
                table=source_name,
                rows_loaded=0,
                execution_time=execution_time,
                status="FAILED",
                message=str(error),
            )

    def _get_table_config(
        self,
        source_name: str,
    ) -> dict:

        return self.config.tables["tables"][
            source_name
        ]

    def _read_csv(
        self,
        filename: str,
    ) -> pd.DataFrame:

        filepath = (
            self.config.olist_data_dir
            / filename
        )

        if not filepath.exists():
            raise FileNotFoundError(filepath)

        self.logger.info(
            f"Reading {filepath.name}"
        )

        return pd.read_csv(filepath)

    def _write_to_database(
        self,
        dataframe: pd.DataFrame,
        schema: str,
        table: str,
    ):

        self.logger.info(
            f"Loading into {schema}.{table}"
        )

        dataframe.to_sql(
            name=table,
            schema=schema,
            con=self.engine,
            if_exists=self.config.settings["load"]["if_exists"],
            index=self.config.settings["load"]["index"],
            chunksize=self.config.settings["load"]["chunksize"],
            method=self.config.settings["load"]["method"],
        )