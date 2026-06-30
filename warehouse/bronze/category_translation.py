from datetime import datetime

import pandas as pd

from warehouse.bronze.base import BronzeTransformer


class BronzeCategoryTranslationTransformer(BronzeTransformer):

    SOURCE_TABLE = "product_category_translation"

    TARGET_TABLE = "product_category_translation"

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