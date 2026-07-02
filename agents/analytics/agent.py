from agents.analytics.generator import AnalyticsGenerator
from agents.core.base_agent import BaseAgent
from agents.core.context import AgentContext


class AnalyticsAgent(BaseAgent):

    name = "analytics"

    description = "Business Analytics Agent"

    def __init__(self):

        self.generator = AnalyticsGenerator()

    def can_handle(
        self,
        context: AgentContext,
    ) -> bool:

        return context.dataframe is not None

    def execute(
        self,
        context: AgentContext,
    ) -> AgentContext:

        result = self.generator.generate(
            context.question,
            context.dataframe,
        )

        context.response = result.summary

        context.insights = result.insights

        context.recommendations = (
            result.recommendations
        )

        return context