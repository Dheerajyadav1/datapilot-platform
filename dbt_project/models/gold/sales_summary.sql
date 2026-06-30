{{ config(materialized='table') }}

SELECT

    DATE(order_purchase_timestamp) AS sales_date,

    COUNT(order_id) AS total_orders,

    SUM(payment_value) AS total_sales,

    AVG(payment_value) AS average_order_value,

    AVG(review_score) AS average_review

FROM {{ ref('fact_sales') }}

GROUP BY sales_date