"""
Abstract LLM Provider
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class BaseLLMProvider(ABC):

    @abstractmethod
    def generate(
        self,
        prompt: str,
        system_prompt: str | None = None,
    ) -> str:
        """
        Generate a response.
        """
        raise NotImplementedError

    @abstractmethod
    def stream(
        self,
        prompt: str,
        system_prompt: str | None = None,
    ):
        """
        Stream a response.
        """
        raise NotImplementedError

    @abstractmethod
    def embed(
        self,
        text: str,
    ) -> list[float]:
        """
        Generate embeddings.
        """
        raise NotImplementedError