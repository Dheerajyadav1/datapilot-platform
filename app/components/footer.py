import streamlit as st


class Footer:

    @staticmethod
    def render():

        st.divider()

        st.caption(
            "© 2026 DataPilot | Built using Python • PostgreSQL • Docker • Airflow • dbt • Streamlit"
        )
