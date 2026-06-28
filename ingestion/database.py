from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError

from ingestion.config import Config


class DatabaseManager:
    """
    PostgreSQL connection manager.
    """

    def __init__(self, config: Config):

        self.config = config

        self.engine: Engine = create_engine(
            self.config.database_url,
            pool_pre_ping=True,
            future=True,
        )

    def test_connection(self) -> bool:

        try:

            with self.engine.connect() as connection:

                connection.execute(text("SELECT 1"))

            return True

        except SQLAlchemyError as error:

            print(f"Database connection failed:\n{error}")

            return False

    def get_engine(self) -> Engine:

        return self.engine