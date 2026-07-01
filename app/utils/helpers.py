from pathlib import Path

import streamlit as st


def load_css():

    css_file = (
        Path(__file__).parents[1]
        / "assets"
        / "styles.css"
    )

    with open(css_file) as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True,
        )
