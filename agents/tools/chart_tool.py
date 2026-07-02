"""
Chart Tool
"""

from __future__ import annotations

import plotly.express as px

from agents.tools.base_tool import BaseTool


class ChartTool(BaseTool):

    name = "chart"

    description = "Generate Plotly Charts."

    def execute(
        self,
        dataframe,
        chart_type: str,
        x: str,
        y: str,
    ):

        if chart_type == "line":

            return px.line(
                dataframe,
                x=x,
                y=y,
            )

        if chart_type == "pie":

            return px.pie(
                dataframe,
                names=x,
                values=y,
            )

        return px.bar(
            dataframe,
            x=x,
            y=y,
        )