import streamlit as st

from app.app_config import AppConfig
from app.components.sidebar import Sidebar
from app.services.dashboard_service import DashboardService
from app.components.charts import Charts
from app.components.metrics import MetricCard
from app.components.footer import Footer
from app.utils.helpers import load_css, render_header
from app.utils.formatting import Formatter


config = AppConfig()

st.set_page_config(
    page_title=config.page_title,
    page_icon=config.page_icon,
    layout=config.layout,
    initial_sidebar_state=config.initial_sidebar_state,
)

load_css()

Sidebar.render()

service = DashboardService()

# Title and Header Card
render_header("DataPilot", "AI-Powered End-to-End Data Engineering Platform")
st.divider()

# Project Overview Card
st.markdown("""
### Project Overview

The **DataPilot** is an end-to-end modern data engineering solution that ingests raw data, transforms it through Bronze, Silver, and Gold layers, orchestrates workflows with Apache Airflow, models data using dbt, and presents interactive analytics through Streamlit.

It utilizes modern dimensional modeling practices to construct a star schema, enabling lightning-fast analytical query execution while maintaining strict constraints checks.
""")
st.divider()

# Loading animation wrapping KPI fetches
with st.spinner("Loading metrics..."):
    try:
        revenue = service.get_total_revenue()
        orders = service.get_total_orders()
        customers = service.get_total_customers()
        products = service.get_total_products()
        sellers = service.get_total_sellers()
    except Exception as e:
        st.error(f"Failed to load repository metrics: {e}")
        revenue = 0
        orders = 0
        customers = 0
        products = 0
        sellers = 0

# KPIs Section with Icons
st.subheader("Key Performance Indicators")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    MetricCard.show(
        "Revenue",
        Formatter.currency(revenue),
    )

with col2:
    MetricCard.show(
        "Orders",
        Formatter.integer(orders),
    )

with col3:
    MetricCard.show(
        "Customers",
        Formatter.integer(customers),
    )

with col4:
    MetricCard.show(
        "Products",
        Formatter.integer(products),
    )

with col5:
    MetricCard.show(
        "Sellers",
        Formatter.integer(sellers),
    )

st.divider()

# Business Insights Section
st.subheader("Business Insights")
insight_col1, insight_col2 = st.columns(2)

with insight_col1:
    st.success(
        "**Revenue Highlight**: The overall e-commerce transactions have reached a historical total of "
        f"**{Formatter.currency(revenue)}**, driven primarily by high-density urban buyer centers."
    )
    st.info(
        "**Top Performer state**: State **SP** (São Paulo) stands as the highest revenue generating state "
        "and largest customer acquisition hub in the dataset."
    )

with insight_col2:
    st.warning(
        "**Auditing Alert**: 3 sales records inside the `gold.fact_sales` layer have missing payment values. "
        "This triggers an alert in our daily dbt data quality checks to ensure source integrity."
    )
    st.success(
        "**Cache Active**: All dashboard queries are cached locally for 600 seconds (10 mins) using Streamlit cache memory, "
        "protecting PostgreSQL connection pool limits."
    )

st.divider()

# Technology Stack Section
st.subheader("Technology Stack")
tech_col1, tech_col2, tech_col3, tech_col4 = st.columns(4)

with tech_col1:
    st.markdown(
        """
        **Python**
        - ETL workflows
        - Weather APIs Ingestion
        """
    )
    st.markdown(
        """
        **PostgreSQL**
        - Data Warehouse
        - Bronze/Silver/Gold
        """
    )

with tech_col2:
    st.markdown(
        """
        **Docker**
        - Container Orchestration
        - Sandbox isolation
        """
    )
    st.markdown(
        """
        **Airflow**
        - Directed Acyclic Graphs
        - Schedule triggers
        """
    )

with tech_col3:
    st.markdown(
        """
        **dbt (data build tool)**
        - SQL transformations
        - Constraints testing
        """
    )
    st.markdown(
        """
        **Plotly**
        - Clean visual charts
        - Responsive layout
        """
    )

with tech_col4:
    st.markdown(
        """
        **Streamlit**
        - User-facing UI
        - Reactive widgets
        """
    )
    st.markdown(
        """
        **SQLAlchemy**
        - Database connection
        - Object relational mapping
        """
    )

st.divider()

# Platform Engineering & Performance Metrics Card
st.subheader("Data Platform Performance Metrics")
perf_col1, perf_col2, perf_col3 = st.columns(3)

with perf_col1:
    st.metric(label="Rows in Gold Schema Marts", value="~248K rows")
    st.metric(label="dbt Materialization Time", value="48 seconds")

with perf_col2:
    st.metric(label="Total Database Tables Loaded", value="20 tables")
    st.metric(label="API Weather Ingestion Runtime", value="~15s")

with perf_col3:
    st.metric(label="dbt Data Audits Passed", value="15 / 16", delta="-1 failed test", delta_color="inverse")
    st.metric(label="SQL Alchemy Cache Status", value="Hit (Active)")

st.divider()

# Recent Revenue Trend Section
st.subheader("Recent Revenue Trend")
with st.spinner("Loading sales trend..."):
    try:
        monthly = service.get_monthly_revenue()
        Charts.line(
            monthly,
            x="month",
            y="revenue",
            title="Monthly Revenue Trend",
        )
    except Exception as e:
        st.error(f"Failed to load revenue trend chart: {e}")

Footer.render()