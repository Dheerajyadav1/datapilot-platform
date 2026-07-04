import streamlit as st

from app.components.sidebar import Sidebar
from app.components.metrics import MetricCard
from app.components.charts import Charts
from app.components.footer import Footer
from app.services.seller_service import SellerService
from app.utils.helpers import load_css
from app.utils.formatting import Formatter


st.set_page_config(
    page_title="Seller Analytics",
    page_icon="🏪",
    layout="wide",
)

load_css()

Sidebar.render()

service = SellerService()

st.title("Seller Analytics")
st.caption("Seller performance and revenue distributions.")
st.divider()

# Wrapped in spinner and try-except error boundary
with st.spinner("Loading Seller analytics data..."):
    try:
        total_sellers = service.total_sellers()
        sellers_by_state_df = service.sellers_by_state()
        top_states_df = service.top_states()
        seller_revenue_df = service.seller_revenue()
        seller_orders_df = service.seller_orders()

        MetricCard.show(
            "Total Sellers",
            Formatter.integer(total_sellers)
        )

        st.divider()

        left, right = st.columns(2)
        with left:
            Charts.horizontal_bar(
                sellers_by_state_df,
                x="sellers",
                y="seller_state",
                title="Sellers by State",
            )
        with right:
            Charts.horizontal_bar(
                top_states_df,
                x="revenue",
                y="seller_state",
                title="Revenue by Seller State",
            )

        st.divider()

        Charts.horizontal_bar(
            seller_revenue_df,
            x="revenue",
            y="seller_id",
            title="Top Sellers by Revenue",
        )

        st.divider()

        Charts.horizontal_bar(
            seller_orders_df,
            x="orders",
            y="seller_id",
            title="Top Sellers by Orders",
        )

    except Exception as e:
        st.error(f"An error occurred loading the Seller Analytics: {e}")

Footer.render()