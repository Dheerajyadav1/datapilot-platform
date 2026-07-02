"""
Database Tool
"""

from __future__ import annotations

import pandas as pd
from sqlalchemy import text

from app.database.connection import DatabaseConnection
from agents.tools.base_tool import BaseTool


class DatabaseTool(BaseTool):

    name = "database"

    description = "Execute SQL queries."

    def __init__(self):

        self.engine = DatabaseConnection.get_engine()

    def execute(
        self,
        sql: str,
        params: dict | None = None,
    ) -> pd.DataFrame:

        with self.engine.connect() as connection:

            return pd.read_sql(
                text(sql),
                connection,
                params=params,
            )

    def execute_scalar(
        self,
        sql: str,
    ):

        with self.engine.connect() as connection:

            return connection.execute(
                text(sql)
            ).scalar()

    def execute_non_query(
        self,
        sql: str,
    ) -> None:

        with self.engine.begin() as connection:

            connection.execute(text(sql))