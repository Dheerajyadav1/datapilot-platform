import pandas as pd

from warehouse.silver.base import SilverTransformer


class SilverOrderReviewsTransformer(SilverTransformer):

    SOURCE_TABLE = "order_reviews"

    TARGET_TABLE = "order_reviews"

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

        string_columns = dataframe.select_dtypes(
            include="object"
        ).columns

        dataframe[string_columns] = dataframe[
            string_columns
        ].apply(lambda col: col.str.strip())

        return dataframe