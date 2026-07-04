import streamlit as st

from app.components.charts import Charts
from app.components.sidebar import Sidebar
from app.components.footer import Footer
from app.services.sales_service import SalesService
from app.utils.helpers import load_css


st.set_page_config(
    page_title="Sales Analytics",
    page_icon=None,
    layout="wide",
)

load_css()

Sidebar.render()

service = SalesService()

st.title("Sales Analytics")
st.caption("Detailed sales performance analysis.")
st.divider()

# Wrapped in spinner and try-except error boundary
with st.spinner("Loading Sales analytics data..."):
    try:
        daily_revenue_df = service.daily_revenue()
        top_categories_df = service.top_categories()
        top_states_df = service.top_states()
        monthly_orders_df = service.monthly_orders()
        payment_dist_df = service.payment_distribution()
        order_status_df = service.order_status()

        # Render Charts
        Charts.line(
            daily_revenue_df,
            x="sales_date",
            y="revenue",
            title="Daily Revenue",
        )

        st.divider()

        left, right = st.columns(2)
        with left:
            Charts.horizontal_bar(
                top_categories_df,
                x="revenue",
                y="product_category_name",
                title="Top Product Categories",
            )
        with right:
            Charts.horizontal_bar(
                top_states_df,
                x="revenue",
                y="customer_state",
                title="Top States by Revenue",
            )

        st.divider()

        left_b, right_b = st.columns(2)
        with left_b:
            Charts.line(
                monthly_orders_df,
                x="month",
                y="orders",
                title="Monthly Orders",
            )
        with right_b:
            Charts.pie(
                payment_dist_df,
                names="payment_type",
                values="revenue",
                title="Payment Distribution",
            )

        st.divider()

        Charts.bar(
            order_status_df,
            x="order_status",
            y="total_orders",
            title="Order Status Distribution",
        )

    except Exception as e:
        st.error(f"An error occurred loading the Sales Analytics: {e}")

Footer.render()