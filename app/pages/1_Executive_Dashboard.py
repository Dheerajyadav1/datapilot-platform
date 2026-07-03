import streamlit as st

from app.components.sidebar import Sidebar
from app.components.metrics import MetricCard
from app.components.charts import Charts
from app.components.tables import Tables
from app.components.footer import Footer
from app.services.dashboard_service import DashboardService
from app.utils.helpers import load_css, render_header
from app.utils.formatting import Formatter


st.set_page_config(
    page_title="Executive Dashboard",
    page_icon="📊",
    layout="wide",
)

load_css()

Sidebar.render()

service = DashboardService()

render_header("📊 Executive Dashboard", "High-level overview of the business.")
st.divider()

# Wrapped in spinner and try-except error boundary
with st.spinner("Loading Executive dashboard data..."):
    try:
        revenue = service.get_total_revenue()
        orders = service.get_total_orders()
        aov = service.get_average_order_value()
        customers = service.get_total_customers()
        sellers = service.get_total_sellers()

        monthly_revenue_df = service.get_monthly_revenue()
        top_categories_df = service.get_top_categories()
        revenue_by_state_df = service.get_revenue_by_state()
        payment_dist_df = service.get_payment_distribution()
        recent_orders_df = service.get_recent_orders()

        # Render KPI Section
        col1, col2, col3 = st.columns(3)
        with col1:
            MetricCard.show("💰 Revenue", Formatter.currency(revenue))
        with col2:
            MetricCard.show("🛒 Orders", Formatter.integer(orders))
        with col3:
            MetricCard.show("💳 Average Order Value", Formatter.currency(aov))

        col4, col5 = st.columns(2)
        with col4:
            MetricCard.show("👥 Customers", Formatter.integer(customers))
        with col5:
            MetricCard.show("🏪 Sellers", Formatter.integer(sellers))

        st.divider()

        # Monthly Revenue
        Charts.line(
            dataframe=monthly_revenue_df,
            x="month",
            y="revenue",
            title="Monthly Revenue Trend"
        )

        st.divider()

        # Revenue Analysis
        left, right = st.columns(2)
        with left:
            Charts.bar(
                dataframe=top_categories_df,
                x="product_category_name",
                y="revenue",
                title="Top Product Categories"
            )
        with right:
            Charts.bar(
                dataframe=revenue_by_state_df,
                x="customer_state",
                y="revenue",
                title="Revenue by State"
            )

        st.divider()

        # Payment Distribution
        Charts.pie(
            dataframe=payment_dist_df,
            names="payment_type",
            values="revenue",
            title="Revenue by Payment Type"
        )

        st.divider()

        # Recent Orders
        st.subheader("Recent Orders")
        Tables.dataframe(recent_orders_df)

    except Exception as e:
        st.error(f"An error occurred loading the Executive Dashboard: {e}")

Footer.render()