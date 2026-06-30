from datetime import datetime

import pandas as pd

from warehouse.bronze.base import BronzeTransformer


class BronzeOrdersTransformer(BronzeTransformer):

    SOURCE_TABLE = "orders"

    TARGET_TABLE = "orders"

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