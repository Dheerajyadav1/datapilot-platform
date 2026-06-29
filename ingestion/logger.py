import logging
import logging.config

from ingestion.config import Config


class LoggerManager:

    def __init__(self, config: Config):
        self.config = config
        logging.config.dictConfig(self.config.logging)

    def get_logger(self, name: str):
        return logging.getLogger(f"ingestion.{name}")