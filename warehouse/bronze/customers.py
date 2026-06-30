from datetime import datetime

import pandas as pd

from warehouse.bronze.base import BronzeTransformer


class BronzeCustomersTransformer(BronzeTransformer):

    SOURCE_TABLE = "customers"

    TARGET_TABLE = "customers"

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