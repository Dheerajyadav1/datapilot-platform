{{ config(materialized='view') }}

SELECT *

FROM {{ source('silver', 'products') }}