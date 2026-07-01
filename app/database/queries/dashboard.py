"""
Dashboard Queries
"""

TOTAL_REVENUE = """
SELECT
    ROUND(SUM(payment_value)::numeric, 2) AS revenue
FROM gold.fact_sales;
"""

TOTAL_ORDERS = """
SELECT
    COUNT(DISTINCT order_id) AS total_orders
FROM gold.fact_sales;
"""

TOTAL_CUSTOMERS = """
SELECT
    COUNT(*) AS total_customers
FROM gold.dim_customers;
"""

TOTAL_PRODUCTS = """
SELECT
    COUNT(*) AS total_products
FROM gold.dim_products;
"""

TOTAL_SELLERS = """
SELECT
    COUNT(*) AS total_sellers
FROM gold.dim_sellers;
"""

AVERAGE_ORDER_VALUE = """
SELECT
    ROUND(AVG(payment_value)::numeric, 2) AS average_order_value
FROM gold.fact_sales;
"""

MONTHLY_REVENUE = """
SELECT
    DATE_TRUNC('month', order_purchase_timestamp::timestamp) AS month,
    ROUND(SUM(payment_value)::numeric, 2) AS revenue
FROM gold.fact_sales
GROUP BY month
ORDER BY month;
"""

TOP_CATEGORIES = """
SELECT
    p.product_category_name,
    ROUND(SUM(s.payment_value)::numeric, 2) AS revenue
FROM gold.fact_sales s
JOIN gold.dim_products p ON s.product_id = p.product_id
GROUP BY p.product_category_name
ORDER BY revenue DESC
LIMIT 10;
"""

REVENUE_BY_STATE = """
SELECT
    c.customer_state,
    ROUND(SUM(s.payment_value)::numeric, 2) AS revenue
FROM gold.fact_sales s
JOIN gold.dim_customers c ON s.customer_id = c.customer_id
GROUP BY c.customer_state
ORDER BY revenue DESC;
"""

PAYMENT_DISTRIBUTION = """
SELECT
    payment_type,
    ROUND(SUM(payment_value)::numeric, 2) AS revenue
FROM gold.fact_sales
GROUP BY payment_type
ORDER BY revenue DESC;
"""

RECENT_ORDERS = """
SELECT
    order_purchase_timestamp,
    order_id,
    customer_id,
    payment_type,
    payment_value
FROM gold.fact_sales
ORDER BY order_purchase_timestamp DESC
LIMIT 20;
"""