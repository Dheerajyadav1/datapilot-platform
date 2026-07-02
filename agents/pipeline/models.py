from dataclasses import dataclass


@dataclass
class PipelineResponse:

    summary: str

    recommendation: str