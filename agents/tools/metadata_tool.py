"""
Metadata Tool
"""

from __future__ import annotations

from sqlalchemy import inspect

from app.database.connection import DatabaseConnection
from agents.tools.base_tool import BaseTool


class MetadataTool(BaseTool):

    name = "metadata"

    description = "Read warehouse metadata."

    _cached_metadata = None

    def __init__(self):

        self.inspector = inspect(
            DatabaseConnection.get_engine()
        )

    def execute(self):

        if MetadataTool._cached_metadata is not None:
            return MetadataTool._cached_metadata

        metadata = {}

        for schema in ("gold", "silver", "bronze"):

            try:

                for table in self.inspector.get_table_names(schema=schema):

                    full_table = f"{schema}.{table}"

                    metadata[full_table] = {

                        "columns": [

                            column["name"]

                            for column in self.inspector.get_columns(table, schema=schema)

                        ]
                    }

            except Exception:

                continue

        MetadataTool._cached_metadata = metadata
        return metadata

    def get_columns(
        self,
        table_name: str,
    ) -> list[str]:

        schema = "gold"

        table = table_name

        if "." in table_name:

            schema, table = table_name.split(".", 1)

        try:

            return [

                column["name"]

                for column in self.inspector.get_columns(table, schema=schema)

            ]

        except Exception:

            return []