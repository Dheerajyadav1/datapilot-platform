"""
Weather Tool
"""

from __future__ import annotations

from agents.tools.base_tool import BaseTool


class WeatherTool(BaseTool):

    name = "weather"

    description = "Weather Information"

    def execute(self):

        return {
            "status": "ready"
        }