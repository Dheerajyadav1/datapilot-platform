from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from ingestion.config import Config


class DatabaseConnection:

    _engine: Engine | None = None

    @classmethod
    def get_engine(cls) -> Engine:

        if cls._engine is None:

            config = Config()

            cls._engine = create_engine(
                config.database_url,
                pool_pre_ping=True,
                pool_size=10,
                max_overflow=20,
            )

        return cls._engine