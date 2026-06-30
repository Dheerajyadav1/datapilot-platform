from warehouse.base import BaseTransformer


class SilverTransformer(BaseTransformer):
    """
    Base class for all Silver transformations.
    """

    SOURCE_SCHEMA = "bronze"

    TARGET_SCHEMA = "silver"