import pandas as pd

from warehouse.silver.base import SilverTransformer


class SilverWeatherTransformer(SilverTransformer):

    SOURCE_TABLE = "weather"

    TARGET_TABLE = "weather"

    def transform(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:

        dataframe = dataframe.copy()

        dataframe.columns = [
            column.strip().lower()
            for column in dataframe.columns
        ]

        dataframe.drop_duplicates(inplace=True)

        dataframe.sort_values(
            by="time",
            inplace=True,
        )

        dataframe.reset_index(
            drop=True,
            inplace=True,
        )

        return dataframe