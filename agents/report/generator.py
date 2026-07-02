from agents.llm import GeminiProvider
from agents.report.models import ReportResponse
from agents.report.prompt import REPORT_PROMPT


class ReportGenerator:

    def __init__(self):

        self.llm = GeminiProvider()

    def generate(
        self,
        question: str,
        summary: str,
        insights: list[str],
        recommendations: list[str],
    ) -> ReportResponse:

        prompt = REPORT_PROMPT.format(
            question=question,
            summary=summary,
            insights="\n".join(insights),
            recommendations="\n".join(recommendations),
        )

        response = self.llm.generate(prompt)

        return ReportResponse(
            report=response.strip()
        )