import streamlit as st

from app.components.sidebar import Sidebar
from app.components.metrics import MetricCard
from app.components.charts import Charts
from app.components.tables import Tables
from app.components.footer import Footer
from app.services.product_service import ProductService
from app.utils.helpers import load_css
from app.utils.formatting import Formatter


st.set_page_config(
    page_title="Product Analytics",
    page_icon=None,
    layout="wide",
)

load_css()

Sidebar.render()

service = ProductService()

st.title("Product Analytics")
st.caption("Analyze product performance and categories.")
st.divider()

# Wrapped in spinner and try-except error boundary
with st.spinner("Loading Product analytics data..."):
    try:
        total_products = service.total_products()
        avg_price = service.average_price()
        products_by_category_df = service.products_by_category()
        category_revenue_df = service.category_revenue()
        product_weight_df = service.product_weight()
        dimensions_df = service.dimensions()

        left, right = st.columns(2)
        with left:
            MetricCard.show(
                "Products",
                Formatter.integer(total_products)
            )
        with right:
            MetricCard.show(
                "Average Price",
                Formatter.currency(avg_price)
            )

        st.divider()

        Charts.horizontal_bar(
            products_by_category_df,
            x="total_products",
            y="product_category_name",
            title="Products by Category",
        )

        st.divider()

        Charts.horizontal_bar(
            category_revenue_df,
            x="revenue",
            y="product_category_name",
            title="Revenue by Category",
        )

        st.divider()

        Charts.bar(
            product_weight_df,
            x="product_category_name",
            y="average_weight",
            title="Average Product Weight",
        )

        st.divider()

        st.subheader("Average Dimensions")
        Tables.dataframe(dimensions_df)

    except Exception as e:
        st.error(f"An error occurred loading the Product Analytics: {e}")

Footer.render()