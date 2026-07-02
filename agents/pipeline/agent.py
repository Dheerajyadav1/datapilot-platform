from agents.core import context
from agents.core.base_agent import BaseAgent
from agents.core.context import AgentContext
from agents.pipeline.generator import PipelineGenerator
from agents.tools.pipeline_tool import PipelineTool


class PipelineAgent(BaseAgent):

    name = "pipeline"

    description = "Pipeline Monitoring Agent"

    def __init__(self):

        self.tool = PipelineTool()

        self.generator = PipelineGenerator()

    def can_handle(
        self,
        context: AgentContext,
    ) -> bool:

        return True

    def execute(
        self,
        context: AgentContext,
    ) -> AgentContext:

        status = self.tool.execute()

        context.pipeline_status = status

        context.dbt_status = status.get(
            "dbt",
            {},
        )

        context.airflow_status = status.get(
            "airflow",
            {},
        )

        result = self.generator.generate(
            status
        )

        context.response = result.summary

        context.recommendations = [
            result.recommendation
        ]

        context.tools_used.append(
            "pipeline"
        )

        return context