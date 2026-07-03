import streamlit as st
from datetime import date


class Sidebar:

    @staticmethod
    def render():

        with st.sidebar:

            st.image(
                "https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png",
                width=80,
            )

            st.title("DataPilot")

            st.caption(
                "AI-Powered Data Engineering Platform"
            )

            st.divider()

            st.success("🟢 Pipeline Healthy")

            st.info("PostgreSQL Connected")

            st.info("Airflow Running")

            st.info("dbt Models Ready")

            st.info("Warehouse Updated")

            st.divider()

            # Interactive Filters
            st.subheader("📊 Interactive Filters")

            # 1. Date Range (Historically Olist data covers 2016 to 2018)
            start_date = st.date_input("Start Date", date(2016, 9, 1))
            end_date = st.date_input("End Date", date(2018, 9, 30))

            # 2. Customer State
            states = ["All", "SP", "RJ", "MG", "RS", "PR", "SC", "BA", "DF", "ES", "GO", "PE", "CE", "PA", "MT", "MA", "MS", "PB", "RN", "AL", "PI", "SE", "RO", "TO", "AC", "AP", "RR"]
            customer_state = st.multiselect("Customer State", states, default="All")

            # 3. Seller State
            seller_state = st.multiselect("Seller State", states, default="All")

            # 4. Product Category
            categories = ["All", "bed_bath_table", "health_beauty", "sports_leisure", "computers_accessories", "housewares", "watches_gifts", "telephony", "garden_tools", "auto", "toys", "cool_stuff", "perfumery", "baby"]
            product_category = st.multiselect("Product Category", categories, default="All")

            if st.button("🔄 Refresh Data"):
                st.cache_data.clear()
                st.rerun()

            st.divider()

            st.caption("Version 1.0")

            # Store filters in session state for cross-page persistence
            st.session_state["filter_start_date"] = start_date
            st.session_state["filter_end_date"] = end_date
            st.session_state["filter_customer_state"] = customer_state
            st.session_state["filter_seller_state"] = seller_state
            st.session_state["filter_product_category"] = product_category