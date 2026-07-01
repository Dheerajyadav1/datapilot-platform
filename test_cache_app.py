import streamlit as st
from app.services.dashboard_service import DashboardService

st.title("Test Caching")

service = DashboardService()
try:
    rev = service.get_total_revenue()
    st.write("Revenue:", rev)
except Exception as e:
    st.exception(e)
