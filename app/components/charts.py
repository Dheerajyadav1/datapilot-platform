import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


class Charts:

    @staticmethod
    def line(dataframe, x, y, title):

        fig = px.line(
            dataframe,
            x=x,
            y=y,
            markers=True,
        )

        fig.update_layout(
            title=title,
            template="plotly_white",
            height=450,
            hovermode="x unified",
            title_x=0.02,
            margin=dict(l=20, r=20, t=60, b=20),
        )

        fig.update_traces(
            line_width=3,
            marker_size=7,
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    @staticmethod
    def bar(dataframe, x, y, title):

        fig = px.bar(
            dataframe,
            x=x,
            y=y,
            text_auto=".2s",
        )

        fig.update_layout(
            title=title,
            template="plotly_white",
            height=450,
            title_x=0.02,
            margin=dict(l=20, r=20, t=60, b=20),
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    @staticmethod
    def horizontal_bar(dataframe, x, y, title):

        fig = px.bar(
            dataframe,
            x=x,
            y=y,
            orientation="h",
            text_auto=".2s",
        )

        fig.update_layout(
            title=title,
            template="plotly_white",
            height=500,
            title_x=0.02,
            yaxis=dict(
                categoryorder="total ascending"
            ),
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    @staticmethod
    def pie(dataframe, names, values, title):

        fig = px.pie(
            dataframe,
            names=names,
            values=values,
            hole=0.45,
        )

        fig.update_layout(
            title=title,
            template="plotly_white",
            height=450,
            title_x=0.02,
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    @staticmethod
    def scatter(dataframe, x, y, color, title):

        fig = px.scatter(
            dataframe,
            x=x,
            y=y,
            color=color,
        )

        fig.update_layout(
            title=title,
            template="plotly_white",
            height=450,
            title_x=0.02,
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    @staticmethod
    def area(dataframe, x, y, title):

        fig = px.area(
            dataframe,
            x=x,
            y=y,
        )

        fig.update_layout(
            title=title,
            template="plotly_white",
            height=450,
            title_x=0.02,
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    @staticmethod
    def gauge(value, title):

        fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=value,
                title={"text": title},
                gauge={
                    "axis": {"range": [0, value * 1.2]},
                    "bar": {"thickness": 0.4},
                },
            )
        )

        fig.update_layout(
            height=350,
            margin=dict(l=20, r=20, t=50, b=20),
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    @staticmethod
    def heatmap(dataframe, x, y, z, title):

        fig = px.density_heatmap(
            dataframe,
            x=x,
            y=y,
            z=z,
            title=title,
            template="plotly_white",
        )

        fig.update_layout(
            height=450,
            title_x=0.02,
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    @staticmethod
    def box(dataframe, x, y, title):

        fig = px.box(
            dataframe,
            x=x,
            y=y,
            title=title,
            template="plotly_white",
        )

        fig.update_layout(
            height=450,
            title_x=0.02,
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    @staticmethod
    def treemap(dataframe, path, values, title):

        fig = px.treemap(
            dataframe,
            path=path,
            values=values,
            title=title,
            template="plotly_white",
        )

        fig.update_layout(
            height=450,
            title_x=0.02,
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    @staticmethod
    def sunburst(dataframe, path, values, title):

        fig = px.sunburst(
            dataframe,
            path=path,
            values=values,
            title=title,
            template="plotly_white",
        )

        fig.update_layout(
            height=450,
            title_x=0.02,
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    @staticmethod
    def funnel(dataframe, x, y, title):

        fig = px.funnel(
            dataframe,
            x=x,
            y=y,
            title=title,
            template="plotly_white",
        )

        fig.update_layout(
            height=450,
            title_x=0.02,
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )