{{ config(materialized='view') }}

SELECT *

FROM {{ source('silver', 'order_items') }}