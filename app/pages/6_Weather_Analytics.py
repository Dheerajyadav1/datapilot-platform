import streamlit as st

from app.components.sidebar import Sidebar
from app.components.charts import Charts
from app.components.tables import Tables
from app.components.footer import Footer
from app.services.weather_service import WeatherService
from app.utils.helpers import load_css


st.set_page_config(
    page_title="Weather Analytics",
    page_icon="🌦️",
    layout="wide",
)

load_css()

Sidebar.render()

service = WeatherService()

st.title("Weather Analytics")
st.caption("Latest environmental observations from data ingestion pipelines.")
st.divider()

# Wrapped in spinner and try-except error boundary
with st.spinner("Loading Weather analytics data..."):
    try:
        weather_df = service.latest_weather()

        # Render Weather Dashboard
        Charts.line(
            weather_df,
            x="time",
            y="temperature_2m",
            title="Temperature (°C)",
        )

        st.divider()

        left, right = st.columns(2)
        with left:
            Charts.line(
                weather_df,
                x="time",
                y="relative_humidity_2m",
                title="Relative Humidity (%)",
            )
        with right:
            Charts.line(
                weather_df,
                x="time",
                y="wind_speed_10m",
                title="Wind Speed (km/h)",
            )

        st.divider()

        Charts.bar(
            weather_df,
            x="time",
            y="precipitation",
            title="Precipitation (mm)",
        )

        st.divider()

        st.subheader("Weather Dataset")
        Tables.dataframe(weather_df)

    except Exception as e:
        st.error(f"An error occurred loading the Weather Analytics: {e}")

Footer.render()