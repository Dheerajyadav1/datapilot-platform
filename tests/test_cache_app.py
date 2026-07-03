"""
Test: Streamlit cache integration with DashboardService.
Run with: streamlit run tests/test_cache_app.py
"""

import streamlit as st
from app.services.dashboard_service import DashboardService

st.title("DataPilot – Cache Test")

service = DashboardService()
try:
    rev = service.get_total_revenue()
    st.success(f"✅ Total Revenue: {rev}")
except Exception as e:
    st.exception(e)
