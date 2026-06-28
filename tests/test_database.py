from ingestion.config import Config
from ingestion.database import DatabaseManager

config = Config()

db = DatabaseManager(config)

print("Connected:", db.test_connection())