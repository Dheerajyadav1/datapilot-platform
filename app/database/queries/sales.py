"""
Sales Analytics Queries
"""

DAILY_REVENUE = """
SELECT
    DATE(order_purchase_timestamp::timestamp) AS sales_date,
    ROUND(SUM(payment_value)::numeric, 2) AS revenue
FROM gold.fact_sales
GROUP BY sales_date
ORDER BY sales_date;
"""

MONTHLY_ORDERS = """
SELECT
    DATE_TRUNC('month', order_purchase_timestamp::timestamp) AS month,
    COUNT(DISTINCT order_id) AS orders
FROM gold.fact_sales
GROUP BY month
ORDER BY month;
"""

TOP_PRODUCT_CATEGORIES = """
SELECT
    p.product_category_name,
    ROUND(SUM(s.payment_value)::numeric, 2) AS revenue
FROM gold.fact_sales s
JOIN gold.dim_products p ON s.product_id = p.product_id
GROUP BY p.product_category_name
ORDER BY revenue DESC
LIMIT 15;
"""

PAYMENT_TYPES = """
SELECT
    payment_type,
    ROUND(SUM(payment_value)::numeric, 2) AS revenue
FROM gold.fact_sales
GROUP BY payment_type
ORDER BY revenue DESC;
"""

ORDER_STATUS = """
SELECT
    o.order_status,
    COUNT(DISTINCT s.order_id) AS total_orders
FROM gold.fact_sales s
JOIN silver.orders o ON s.order_id = o.order_id
GROUP BY o.order_status
ORDER BY total_orders DESC;
"""

TOP_STATES = """
SELECT
    c.customer_state,
    ROUND(SUM(s.payment_value)::numeric, 2) AS revenue
FROM gold.fact_sales s
JOIN gold.dim_customers c ON s.customer_id = c.customer_id
GROUP BY c.customer_state
ORDER BY revenue DESC
LIMIT 15;
"""