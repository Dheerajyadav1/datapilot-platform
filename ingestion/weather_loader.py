from time import perf_counter

import httpx
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


class WeatherLoader:

    BASE_URL = "https://api.open-meteo.com/v1/forecast"

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

        self.validator = DataValidator(
            rules=[
                NotEmptyRule(),
                NoDuplicateRule(),
                RequiredColumnsRule(
                    [
                        "time",
                        "temperature_2m",
                        "relative_humidity_2m",
                        "precipitation",
                        "wind_speed_10m",
                    ]
                ),
            ]
        )

    def load(
        self,
        latitude: float,
        longitude: float,
    ) -> LoadResult:

        start_time = perf_counter()

        try:

            weather_json = self._fetch_weather(
                latitude,
                longitude,
            )

            dataframe = self._to_dataframe(
                weather_json
            )

            report = self.validator.validate(
                dataframe
            )

            self.validation_logger.log(
                report
            )

            if not report.passed:
                raise ValueError(
                    "Weather validation failed."
                )

            self._write_to_database(
                dataframe
            )

            execution_time = (
                perf_counter() - start_time
            )

            self.logger.info(
                f"{len(dataframe):,} weather records loaded."
            )

            return LoadResult(
                source="weather",
                table="weather",
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
                source="weather",
                table="weather",
                rows_loaded=0,
                execution_time=execution_time,
                status="FAILED",
                message=str(error),
            )

    def _fetch_weather(
        self,
        latitude: float,
        longitude: float,
    ) -> dict:

        params = {
            "latitude": latitude,
            "longitude": longitude,
            "hourly": (
                "temperature_2m,"
                "relative_humidity_2m,"
                "precipitation,"
                "wind_speed_10m"
            ),
            "forecast_days": 1,
        }

        response = httpx.get(
            self.BASE_URL,
            params=params,
            timeout=30,
        )

        response.raise_for_status()

        return response.json()

    def _to_dataframe(
        self,
        weather_json: dict,
    ) -> pd.DataFrame:

        dataframe = pd.DataFrame(
            weather_json["hourly"]
        )

        dataframe["time"] = pd.to_datetime(
            dataframe["time"]
        )

        return dataframe

    def _write_to_database(
        self,
        dataframe: pd.DataFrame,
    ):

        dataframe.to_sql(
            name="weather",
            schema="raw",
            con=self.engine,
            if_exists=self.config.settings["load"]["if_exists"],
            index=False,
            chunksize=self.config.settings["load"]["chunksize"],
            method=self.config.settings["load"]["method"],
        )