import streamlit as st


@st.cache_data(ttl=600)
def _cache_dataframe(_func, *args, **kwargs):

    return _func(*args, **kwargs)


@st.cache_data(ttl=600)
def _cache_scalar(_func, *args, **kwargs):

    return _func(*args, **kwargs)


class Cache:

    @staticmethod
    def dataframe(func, *args, **kwargs):

        return _cache_dataframe(func, *args, **kwargs)

    @staticmethod
    def scalar(func, *args, **kwargs):

        return _cache_scalar(func, *args, **kwargs)
