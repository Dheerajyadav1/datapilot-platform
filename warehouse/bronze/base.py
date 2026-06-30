from warehouse.base import BaseTransformer


class BronzeTransformer(BaseTransformer):
    """
    Base class for all Bronze transformations.
    """

    SOURCE_SCHEMA = "raw"

    TARGET_SCHEMA = "bronze"