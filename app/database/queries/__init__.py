from app.database.queries.dashboard import (
    TOTAL_REVENUE,
    TOTAL_ORDERS,
    TOTAL_CUSTOMERS,
    TOTAL_PRODUCTS,
    TOTAL_SELLERS,
    AVERAGE_ORDER_VALUE,
    MONTHLY_REVENUE,
    TOP_CATEGORIES,
    REVENUE_BY_STATE,
    PAYMENT_DISTRIBUTION,
    RECENT_ORDERS,
)
from app.database.queries.sales import (
    DAILY_REVENUE,
    MONTHLY_ORDERS,
    TOP_PRODUCT_CATEGORIES,
    PAYMENT_TYPES,
    ORDER_STATUS,
    TOP_STATES,
)
from app.database.queries.customers import (
    TOTAL_CUSTOMERS as CUSTOMERS_TOTAL,
    CUSTOMERS_BY_STATE,
    CUSTOMERS_BY_CITY,
    CUSTOMER_REVENUE,
    NEW_CUSTOMERS_MONTHLY,
)
from app.database.queries.products import (
    TOTAL_PRODUCTS as PRODUCTS_TOTAL,
    PRODUCTS_BY_CATEGORY,
    CATEGORY_REVENUE,
    AVERAGE_PRODUCT_PRICE,
    PRODUCT_WEIGHT,
    PRODUCT_DIMENSIONS,
)
from app.database.queries.sellers import (
    TOTAL_SELLERS as SELLERS_TOTAL,
    SELLERS_BY_STATE,
    SELLER_REVENUE,
    TOP_SELLER_STATES,
    SELLER_ORDERS,
)
from app.database.queries.weather import (
    LATEST_WEATHER,
    AVERAGE_WEATHER,
)
from app.database.queries.quality import (
    BRONZE_TABLE_COUNTS,
    GOLD_TABLE_COUNTS,
)
