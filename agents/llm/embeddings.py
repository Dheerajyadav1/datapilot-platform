"""
Embedding Service
"""

from __future__ import annotations

from agents.llm.gemini import GeminiProvider


class EmbeddingService:

    def __init__(self):

        self.provider = GeminiProvider()

    def generate(
        self,
        text: str,
    ) -> list[float]:

        return self.provider.embed(
            text
        )