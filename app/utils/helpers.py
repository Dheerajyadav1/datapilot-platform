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


def render_header(title, subtitle=None):
    st.markdown(f'<h1 class="gradient-title">{title}</h1>', unsafe_allow_html=True)
    if subtitle:
        st.markdown(f'<p class="gradient-subtitle">{subtitle}</p>', unsafe_allow_html=True)
    else:
        st.markdown('<div style="margin-bottom: 1.5rem;"></div>', unsafe_allow_html=True)
