from ingestion.config import Config
from ingestion.database import DatabaseManager
from ingestion.logger import LoggerManager
from ingestion.csv_loader import CSVLoader

config = Config()

database = DatabaseManager(config)

logger = LoggerManager(config)

loader = CSVLoader(
    config=config,
    database=database,
    logger=logger,
)

result = loader.load("customers")

print(result)