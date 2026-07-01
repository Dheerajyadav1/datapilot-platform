import streamlit as st


class Footer:

    @staticmethod
    def render():

        st.divider()

        st.caption(
            "© 2026 Agentic Data Platform | Built using Python • PostgreSQL • Docker • Airflow • dbt • Streamlit"
        )
