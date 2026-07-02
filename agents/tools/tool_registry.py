"""
Tool Registry
"""

from __future__ import annotations

from typing import Type

from agents.tools.base_tool import BaseTool


class ToolRegistry:

    def __init__(self):

        self._tools: dict[str, Type[BaseTool]] = {}

    def register(
        self,
        tool: Type[BaseTool],
    ) -> None:

        self._tools[tool.name] = tool

    def create(
        self,
        tool_name: str,
    ) -> BaseTool:

        if tool_name not in self._tools:
            raise ValueError(f"Tool '{tool_name}' is not registered.")

        return self._tools[tool_name]()

    def list_tools(self) -> list[str]:

        return sorted(self._tools.keys())


tool_registry = ToolRegistry()