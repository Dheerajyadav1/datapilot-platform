from app.database.repository import Repository
from app.database.queries import quality


class QualityService:

    def __init__(self):

        self.repository = Repository()

    def bronze_tables(self):

        return self.repository.fetch_dataframe(
            quality.BRONZE_TABLE_COUNTS
        )

    def gold_tables(self):

        return self.repository.fetch_dataframe(
            quality.GOLD_TABLE_COUNTS
        )