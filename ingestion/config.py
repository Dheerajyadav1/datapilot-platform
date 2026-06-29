
from pathlib import Path
import os
import yaml

# pyrefly: ignore [missing-import]
from dotenv import load_dotenv


class Config:
    """
    Central configuration manager for the Agentic Data Platform.
    """

    def __init__(self):

        # Load environment variables
        load_dotenv()

        # -----------------------------
        # Project Paths
        # -----------------------------

        self.project_root = Path(__file__).resolve().parent.parent

        self.data_dir = self.project_root / "data"

        self.raw_data_dir = self.data_dir / "raw"

        self.olist_data_dir = self.raw_data_dir / "olist"

        self.config_dir = Path(__file__).resolve().parent / "config"

        # -----------------------------
        # Database
        # -----------------------------

        self.db_name = os.getenv("POSTGRES_DB", "agentic_db")

        self.db_user = os.getenv("POSTGRES_USER", "postgres")

        self.db_password = os.getenv("POSTGRES_PASSWORD", "postgres")

        self.db_host = os.getenv("POSTGRES_HOST", "localhost")

        self.db_port = int(os.getenv("POSTGRES_PORT", "5432"))

        self.database_url = (
            f"postgresql+psycopg2://"
            f"{self.db_user}:"
            f"{self.db_password}@"
            f"{self.db_host}:"
            f"{self.db_port}/"
            f"{self.db_name}"
        )

        # -----------------------------
        # YAML Configuration
        # -----------------------------

        self.tables = self._load_yaml("tables.yaml")

        self.settings = self._load_yaml("settings.yaml")

        self.logging = self._load_yaml("logging.yaml")

    def _load_yaml(self, filename):

        filepath = self.config_dir / filename

        if not filepath.exists():
            raise FileNotFoundError(f"{filename} not found.")

        with open(filepath, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)