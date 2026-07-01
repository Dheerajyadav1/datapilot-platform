import pandas as pd
from sqlalchemy import text

from app.database.connection import DatabaseConnection
from app.utils.cache import Cache


class Repository:

    def __init__(self):

        self.engine = DatabaseConnection.get_engine()

    def fetch_dataframe(self, query: str, params: dict | None = None):

        return Cache.dataframe(
            self._fetch_dataframe,
            query,
            params,
        )

    def _fetch_dataframe(self, query: str, params: dict | None = None):

        with self.engine.begin() as connection:

            dataframe = pd.read_sql(
                text(query),
                connection,
                params=params,
            )

        return dataframe

    def fetch_scalar(self, query: str, params: dict | None = None):

        return Cache.scalar(
            self._fetch_scalar,
            query,
            params,
        )

    def _fetch_scalar(self, query: str, params: dict | None = None):

        with self.engine.begin() as connection:

            result = connection.execute(
                text(query),
                params or {},
            ).scalar()

        return result