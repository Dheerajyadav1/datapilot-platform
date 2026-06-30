from ingestion.config import Config
from ingestion.database import DatabaseManager
from ingestion.logger import LoggerManager

# Bronze
from warehouse.bronze.category_translation import (
    BronzeCategoryTranslationTransformer,
)
from warehouse.bronze.customers import (
    BronzeCustomersTransformer,
)
from warehouse.bronze.geolocation import (
    BronzeGeolocationTransformer,
)
from warehouse.bronze.order_items import (
    BronzeOrderItemsTransformer,
)
from warehouse.bronze.order_payments import (
    BronzeOrderPaymentsTransformer,
)
from warehouse.bronze.order_reviews import (
    BronzeOrderReviewsTransformer,
)
from warehouse.bronze.orders import (
    BronzeOrdersTransformer,
)
from warehouse.bronze.products import (
    BronzeProductsTransformer,
)
from warehouse.bronze.sellers import (
    BronzeSellersTransformer,
)
from warehouse.bronze.weather import (
    BronzeWeatherTransformer,
)

# Silver
from warehouse.silver.category_translation import (
    SilverCategoryTranslationTransformer,
)
from warehouse.silver.customers import (
    SilverCustomersTransformer,
)
from warehouse.silver.geolocation import (
    SilverGeolocationTransformer,
)
from warehouse.silver.order_items import (
    SilverOrderItemsTransformer,
)
from warehouse.silver.order_payments import (
    SilverOrderPaymentsTransformer,
)
from warehouse.silver.order_reviews import (
    SilverOrderReviewsTransformer,
)
from warehouse.silver.orders import (
    SilverOrdersTransformer,
)
from warehouse.silver.products import (
    SilverProductsTransformer,
)
from warehouse.silver.sellers import (
    SilverSellersTransformer,
)
from warehouse.silver.weather import (
    SilverWeatherTransformer,
)


def run_pipeline():

    config = Config()

    database = DatabaseManager(config)

    logger_manager = LoggerManager(config)

    logger = logger_manager.get_logger("Warehouse")

    logger.info("=" * 60)
    logger.info("Starting Warehouse Pipeline")
    logger.info("=" * 60)

    bronze_transformers = [
        BronzeCustomersTransformer,
        BronzeOrdersTransformer,
        BronzeOrderItemsTransformer,
        BronzeOrderPaymentsTransformer,
        BronzeOrderReviewsTransformer,
        BronzeProductsTransformer,
        BronzeSellersTransformer,
        BronzeGeolocationTransformer,
        BronzeCategoryTranslationTransformer,
        BronzeWeatherTransformer,
    ]

    logger.info("=" * 60)
    logger.info("BRONZE LAYER")
    logger.info("=" * 60)

    for transformer in bronze_transformers:

        transformer(
            config=config,
            database=database,
            logger=logger_manager,
        ).run()

    silver_transformers = [
        SilverCustomersTransformer,
        SilverOrdersTransformer,
        SilverOrderItemsTransformer,
        SilverOrderPaymentsTransformer,
        SilverOrderReviewsTransformer,
        SilverProductsTransformer,
        SilverSellersTransformer,
        SilverGeolocationTransformer,
        SilverCategoryTranslationTransformer,
        SilverWeatherTransformer,
    ]

    logger.info("=" * 60)
    logger.info("SILVER LAYER")
    logger.info("=" * 60)

    for transformer in silver_transformers:

        transformer(
            config=config,
            database=database,
            logger=logger_manager,
        ).run()

    logger.info("=" * 60)
    logger.info("Warehouse Pipeline Completed Successfully")
    logger.info("=" * 60)


if __name__ == "__main__":
    run_pipeline()