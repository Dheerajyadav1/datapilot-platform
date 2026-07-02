"""
Base Tool
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class BaseTool(ABC):

    name: str = "base"
    description: str = ""

    @abstractmethod
    def execute(self, *args, **kwargs):
        raise NotImplementedError