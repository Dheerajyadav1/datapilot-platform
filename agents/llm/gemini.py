"""
Gemini Provider
"""

from __future__ import annotations

import google.generativeai as genai

from agents.llm.provider import BaseLLMProvider
from config.settings import settings


class GeminiProvider(BaseLLMProvider):

    _model = None

    def __init__(self):

        if GeminiProvider._model is None:

            genai.configure(
                api_key=settings.GEMINI_API_KEY
            )

            GeminiProvider._model = genai.GenerativeModel(
                model_name=settings.GEMINI_MODEL
            )

        self.model = GeminiProvider._model

    def generate(
        self,
        prompt: str,
        system_prompt: str | None = None,
    ) -> str:

        if system_prompt:

            prompt = (
                f"{system_prompt}\n\n"
                f"{prompt}"
            )

        response = self.model.generate_content(
            prompt
        )

        return response.text

    def stream(
        self,
        prompt: str,
        system_prompt: str | None = None,
    ):

        if system_prompt:

            prompt = (
                f"{system_prompt}\n\n"
                f"{prompt}"
            )

        response = self.model.generate_content(
            prompt,
            stream=True,
        )

        for chunk in response:

            if chunk.text:

                yield chunk.text

    def embed(
        self,
        text: str,
    ) -> list[float]:

        embedding = genai.embed_content(
            model=settings.EMBEDDING_MODEL,
            content=text,
        )

        return embedding["embedding"]