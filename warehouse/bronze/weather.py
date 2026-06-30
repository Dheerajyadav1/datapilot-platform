from datetime import datetime

import pandas as pd

from warehouse.bronze.base import BronzeTransformer


class BronzeWeatherTransformer(BronzeTransformer):

    SOURCE_TABLE = "weather"

    TARGET_TABLE = "weather"

    def transform(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:

        dataframe = dataframe.copy()

        dataframe.columns = [
            column.lower()
            for column in dataframe.columns
        ]

        dataframe["source"] = "open-meteo"

        dataframe["bronze_loaded_at"] = datetime.utcnow()

        return dataframe