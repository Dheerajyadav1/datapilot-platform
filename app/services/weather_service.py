from app.database.repository import Repository
from app.database.queries import weather


class WeatherService:

    def __init__(self):

        self.repository = Repository()

    def latest_weather(self):

        return self.repository.fetch_dataframe(
            weather.LATEST_WEATHER
        )

    def average_weather(self):

        return self.repository.fetch_dataframe(
            weather.AVERAGE_WEATHER
        )