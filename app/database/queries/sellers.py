"""
Seller Analytics Queries
"""

TOTAL_SELLERS = """
SELECT
    COUNT(*) AS sellers
FROM gold.dim_sellers;
"""

SELLERS_BY_STATE = """
SELECT
    seller_state,
    COUNT(*) AS sellers
FROM gold.dim_sellers
GROUP BY seller_state
ORDER BY sellers DESC;
"""

SELLER_REVENUE = """
SELECT
    seller_id,
    ROUND(SUM(payment_value)::numeric, 2) AS revenue
FROM gold.fact_sales
GROUP BY seller_id
ORDER BY revenue DESC
LIMIT 20;
"""

TOP_SELLER_STATES = """
SELECT
    sel.seller_state,
    ROUND(SUM(s.payment_value)::numeric, 2) AS revenue
FROM gold.fact_sales s
JOIN gold.dim_sellers sel ON s.seller_id = sel.seller_id
GROUP BY sel.seller_state
ORDER BY revenue DESC;
"""

SELLER_ORDERS = """
SELECT
    seller_id,
    COUNT(DISTINCT order_id) AS orders
FROM gold.fact_sales
GROUP BY seller_id
ORDER BY orders DESC
LIMIT 20;
"""