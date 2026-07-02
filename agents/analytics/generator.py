from agents.analytics.models import AnalyticsResponse
from agents.analytics.prompt import ANALYTICS_PROMPT
from agents.llm import GeminiProvider


class AnalyticsGenerator:

    def __init__(self):

        self.llm = GeminiProvider()

    def generate(
        self,
        question: str,
        dataframe,
    ) -> AnalyticsResponse:

        prompt = ANALYTICS_PROMPT.format(
            question=question,
            data=dataframe.head(20).to_markdown(index=False),
        )

        response = self.llm.generate(
            prompt
        )

        summary = ""
        insights = []
        recommendations = []

        section = None

        for line in response.splitlines():

            line = line.strip()

            if not line:
                continue

            lower = line.lower()

            if lower.startswith("summary"):
                section = "summary"
                continue

            if lower.startswith("insights"):
                section = "insights"
                continue

            if lower.startswith("recommendations"):
                section = "recommendations"
                continue

            if section == "summary":
                summary += line + " "

            elif section == "insights":
                insights.append(line.lstrip("- ").strip())

            elif section == "recommendations":
                recommendations.append(
                    line.lstrip("- ").strip()
                )

        return AnalyticsResponse(
            summary=summary.strip(),
            insights=insights,
            recommendations=recommendations,
        )