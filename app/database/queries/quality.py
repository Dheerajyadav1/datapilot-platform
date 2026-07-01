"""
Data Quality Queries
"""

BRONZE_TABLE_COUNTS = """
SELECT
'customers' table_name,
COUNT(*) rows_loaded
FROM bronze.customers

UNION ALL

SELECT
'orders',
COUNT(*)
FROM bronze.orders

UNION ALL

SELECT
'order_items',
COUNT(*)
FROM bronze.order_items

UNION ALL

SELECT
'products',
COUNT(*)
FROM bronze.products

UNION ALL

SELECT
'sellers',
COUNT(*)
FROM bronze.sellers

UNION ALL

SELECT
'weather',
COUNT(*)
FROM bronze.weather;
"""


GOLD_TABLE_COUNTS = """
SELECT
'dim_customers',
COUNT(*)
FROM gold.dim_customers

UNION ALL

SELECT
'dim_products',
COUNT(*)
FROM gold.dim_products

UNION ALL

SELECT
'dim_sellers',
COUNT(*)
FROM gold.dim_sellers

UNION ALL

SELECT
'fact_sales',
COUNT(*)
FROM gold.fact_sales

UNION ALL

SELECT
'fact_weather',
COUNT(*)
FROM gold.fact_weather;
"""