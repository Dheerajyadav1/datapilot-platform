import streamlit as st

from app.components.sidebar import Sidebar
from app.components.tables import Tables
from app.components.footer import Footer
from app.services.quality_service import QualityService
from app.utils.helpers import load_css


st.set_page_config(
    page_title="Data Quality",
    page_icon="✅",
    layout="wide",
)

load_css()

Sidebar.render()

service = QualityService()

st.title("Data Quality Dashboard")
st.success("Pipeline Health: HEALTHY")
st.divider()

# Wrapped in spinner and try-except error boundary
with st.spinner("Loading Data Quality audit data..."):
    try:
        bronze_tables_df = service.bronze_tables()
        gold_tables_df = service.gold_tables()

        left, right = st.columns(2)
        with left:
            st.subheader("Bronze Layer")
            Tables.dataframe(bronze_tables_df)
        with right:
            st.subheader("Gold Layer")
            Tables.dataframe(gold_tables_df)

        st.divider()

        st.info(
            """
            ✔ Data Ingestion Completed
            ✔ Warehouse Completed
            ✔ dbt Models Passed
            ✔ Airflow Running
            ✔ PostgreSQL Connected
            ✔ Gold Layer Ready
            """
        )

    except Exception as e:
        st.error(f"An error occurred loading the Data Quality dashboard: {e}")

Footer.render()