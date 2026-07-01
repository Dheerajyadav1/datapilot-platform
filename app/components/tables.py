import streamlit as st


class Tables:

    @staticmethod
    def dataframe(dataframe):

        st.dataframe(
            dataframe,
            use_container_width=True,
            hide_index=True,
        )