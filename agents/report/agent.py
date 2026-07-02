from agents.core import context
from agents.core.base_agent import BaseAgent
from agents.core.context import AgentContext
from agents.report.generator import ReportGenerator


class ReportAgent(BaseAgent):

    name = "report"

    description = "Executive Report Generator"

    def __init__(self):

        self.generator = ReportGenerator()

    def can_handle(
        self,
        context: AgentContext,
    ) -> bool:

        return (
            len(context.insights) > 0
        )

    def execute(
        self,
        context: AgentContext,
    ) -> AgentContext:

        report = self.generator.generate(

            question=context.question,

            summary=context.response,

            insights=context.insights,

            recommendations=context.recommendations,
        )

        context.report = report.report

        context.response = report.report
 
        return context