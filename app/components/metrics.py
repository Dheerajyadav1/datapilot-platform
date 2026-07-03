import streamlit as st


class MetricCard:

    @staticmethod
    def show(title, value):

        st.markdown(
            f"""
            <div class="custom-metric-card">
                <div class="custom-metric-title">{title}</div>
                <div class="custom-metric-value">{value}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )