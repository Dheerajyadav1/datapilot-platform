"""
LLM-powered Planner
"""

from __future__ import annotations

from dataclasses import dataclass, field

from agents.core.context import AgentContext
from agents.core.state import ExecutionState
from agents.llm import GeminiProvider, PromptLibrary


@dataclass
class ExecutionPlan:

    queue: list[str] = field(default_factory=list)
    reason: str = ""


class Planner:

    def __init__(self):

        self.llm = GeminiProvider()

    def create_plan(
        self,
        context: AgentContext,
    ) -> ExecutionPlan:

        context.state = ExecutionState.PLANNING

        response = self.llm.generate(
            prompt=context.question,
            system_prompt=PromptLibrary.ROUTER_SYSTEM,
        )

        intent = response.strip().lower()

        context.intent = intent

        mapping = {

            "sql": [
                "sql",
            ],

            "analytics": [
                "sql",
                "analytics",
            ],

            "knowledge": [
                "knowledge",
            ],

            "pipeline": [
                "pipeline",
            ],

            "report": [
                "sql",
                "analytics",
                "report",
            ],
        }

        queue = mapping.get(
            intent,
            ["knowledge"],
        )

        return ExecutionPlan(

            queue=queue,

            reason=intent,
        )