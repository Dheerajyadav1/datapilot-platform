{{ config(materialized='table') }}

SELECT

    oi.order_id,

    o.customer_id,

    oi.product_id,

    oi.seller_id,

    o.order_purchase_timestamp,

    oi.price,

    oi.freight_value,

    op.payment_type,

    op.payment_value,

    r.review_score

FROM {{ ref('stg_order_items') }} oi

JOIN {{ ref('stg_orders') }} o

ON oi.order_id = o.order_id

LEFT JOIN {{ ref('stg_order_payments') }} op

ON oi.order_id = op.order_id

LEFT JOIN {{ ref('stg_order_reviews') }} r

ON oi.order_id = r.order_id