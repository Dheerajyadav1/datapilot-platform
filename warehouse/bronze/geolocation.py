from datetime import datetime

import pandas as pd

from warehouse.bronze.base import BronzeTransformer


class BronzeGeolocationTransformer(BronzeTransformer):

    SOURCE_TABLE = "geolocation"

    TARGET_TABLE = "geolocation"

    def transform(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:

        dataframe = dataframe.copy()

        dataframe.columns = [
            column.lower()
            for column in dataframe.columns
        ]

        dataframe["bronze_loaded_at"] = datetime.utcnow()

        return dataframe