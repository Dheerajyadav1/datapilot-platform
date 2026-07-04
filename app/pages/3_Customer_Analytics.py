import streamlit as st

from app.components.sidebar import Sidebar
from app.components.charts import Charts
from app.components.metrics import MetricCard
from app.components.tables import Tables
from app.components.footer import Footer
from app.services.customer_service import CustomerService
from app.utils.helpers import load_css
from app.utils.formatting import Formatter


st.set_page_config(
    page_title="Customer Analytics",
    page_icon="👥",
    layout="wide",
)

load_css()

Sidebar.render()

service = CustomerService()

st.title("Customer Analytics")
st.caption("Customer acquisition and geographic analysis.")
st.divider()

# Wrapped in spinner and try-except error boundary
with st.spinner("Loading Customer analytics data..."):
    try:
        total_customers = service.total_customers()
        monthly_customers_df = service.monthly_customers()
        customers_by_state_df = service.customers_by_state()
        customer_revenue_df = service.customer_revenue()
        customers_by_city_df = service.customers_by_city()

        MetricCard.show(
            "Total Customers",
            Formatter.integer(total_customers)
        )

        st.divider()

        Charts.line(
            monthly_customers_df,
            x="month",
            y="customers",
            title="Monthly Customer Growth",
        )

        st.divider()

        left, right = st.columns(2)
        with left:
            Charts.horizontal_bar(
                customers_by_state_df,
                x="customers",
                y="customer_state",
                title="Customers by State",
            )
        with right:
            Charts.horizontal_bar(
                customer_revenue_df,
                x="revenue",
                y="customer_state",
                title="Revenue by State",
            )

        st.divider()

        st.subheader("Top Cities")
        Tables.dataframe(customers_by_city_df)

    except Exception as e:
        st.error(f"An error occurred loading the Customer Analytics: {e}")

Footer.render()