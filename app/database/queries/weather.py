"""
Weather Analytics Queries
"""

LATEST_WEATHER = """
SELECT
    time,
    temperature_2m,
    relative_humidity_2m,
    wind_speed_10m,
    precipitation
FROM gold.fact_weather
ORDER BY time DESC
LIMIT 100;
"""

AVERAGE_WEATHER = """
SELECT
    ROUND(AVG(temperature_2m)::numeric, 2) AS avg_temp,
    ROUND(AVG(relative_humidity_2m)::numeric, 2) AS avg_humidity,
    ROUND(AVG(wind_speed_10m)::numeric, 2) AS avg_wind,
    ROUND(SUM(precipitation)::numeric, 2) AS total_precip
FROM gold.fact_weather;
"""