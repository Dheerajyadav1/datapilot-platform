from agents.llm import GeminiProvider
from agents.pipeline.models import PipelineResponse
from agents.pipeline.prompt import PIPELINE_PROMPT


class PipelineGenerator:

    def __init__(self):

        self.llm = GeminiProvider()

    def generate(
        self,
        pipeline_status: dict,
    ) -> PipelineResponse:

        prompt = PIPELINE_PROMPT.format(
            status=pipeline_status
        )

        response = self.llm.generate(prompt)

        sections = response.split("Recommendations")

        summary = sections[0].strip()

        recommendation = ""

        if len(sections) > 1:

            recommendation = sections[1].strip()

        return PipelineResponse(
            summary=summary,
            recommendation=recommendation,
        )