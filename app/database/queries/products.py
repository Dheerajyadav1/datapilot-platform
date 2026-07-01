"""
Product Analytics Queries
"""

TOTAL_PRODUCTS = """
SELECT
    COUNT(*) AS total_products
FROM gold.dim_products;
"""

PRODUCTS_BY_CATEGORY = """
SELECT
    product_category_name,
    COUNT(*) AS total_products
FROM gold.dim_products
GROUP BY product_category_name
ORDER BY total_products DESC
LIMIT 20;
"""

CATEGORY_REVENUE = """
SELECT
    p.product_category_name,
    ROUND(SUM(s.payment_value)::numeric, 2) AS revenue
FROM gold.fact_sales s
JOIN gold.dim_products p ON s.product_id = p.product_id
GROUP BY p.product_category_name
ORDER BY revenue DESC
LIMIT 20;
"""

AVERAGE_PRODUCT_PRICE = """
SELECT
    ROUND(AVG(payment_value)::numeric, 2)
FROM gold.fact_sales;
"""

PRODUCT_WEIGHT = """
SELECT
    product_category_name,
    AVG(product_weight_g) AS average_weight
FROM gold.dim_products
GROUP BY product_category_name
ORDER BY average_weight DESC
LIMIT 20;
"""

PRODUCT_DIMENSIONS = """
SELECT
    AVG(product_length_cm) AS avg_length,
    AVG(product_height_cm) AS avg_height,
    AVG(product_width_cm) AS avg_width
FROM gold.dim_products;
"""