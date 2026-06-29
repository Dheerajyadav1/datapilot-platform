from ingestion.config import Config
from ingestion.database import DatabaseManager
from ingestion.logger import LoggerManager
from ingestion.weather_loader import WeatherLoader

config = Config()

database = DatabaseManager(config)

logger = LoggerManager(config)

loader = WeatherLoader(
    config,
    database,
    logger,
)

result = loader.load(
    latitude=-23.5505,
    longitude=-46.6333,
)

print(result)