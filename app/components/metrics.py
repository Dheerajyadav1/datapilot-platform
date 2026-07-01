import streamlit as st


class MetricCard:

    @staticmethod
    def show(title, value):

        st.metric(
            label=title,
            value=value,
            border=True,
        )