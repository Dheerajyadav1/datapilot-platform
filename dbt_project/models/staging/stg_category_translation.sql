{{ config(materialized='view') }}

SELECT *

FROM {{ source('silver', 'product_category_translation') }}