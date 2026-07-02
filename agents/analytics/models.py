from dataclasses import dataclass


@dataclass
class AnalyticsResponse:

    summary: str

    insights: list[str]

    recommendations: list[str]