"""
Customer Analytics Queries
"""

TOTAL_CUSTOMERS = """
SELECT
    COUNT(*) AS customers
FROM gold.dim_customers;
"""

CUSTOMERS_BY_STATE = """
SELECT
    customer_state,
    COUNT(*) AS customers
FROM gold.dim_customers
GROUP BY customer_state
ORDER BY customers DESC;
"""

CUSTOMERS_BY_CITY = """
SELECT
    customer_city,
    COUNT(*) AS customers
FROM gold.dim_customers
GROUP BY customer_city
ORDER BY customers DESC
LIMIT 20;
"""

CUSTOMER_REVENUE = """
SELECT
    c.customer_state,
    ROUND(SUM(s.payment_value)::numeric, 2) AS revenue
FROM gold.fact_sales s
JOIN gold.dim_customers c ON s.customer_id = c.customer_id
GROUP BY c.customer_state
ORDER BY revenue DESC;
"""

NEW_CUSTOMERS_MONTHLY = """
WITH customer_first_purchase AS (
    SELECT
        customer_id,
        MIN(order_purchase_timestamp::timestamp) AS first_purchase
    FROM gold.fact_sales
    GROUP BY customer_id
)
SELECT
    DATE_TRUNC('month', first_purchase) AS month,
    COUNT(*) AS customers
FROM customer_first_purchase
GROUP BY month
ORDER BY month;
"""