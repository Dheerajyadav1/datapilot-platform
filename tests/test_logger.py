from ingestion.config import Config
from ingestion.logger import LoggerManager

config = Config()

logger = LoggerManager(config).get_logger("Test")

logger.info("Logger initialized successfully.")
logger.warning("This is a warning.")
logger.error("This is an error.")