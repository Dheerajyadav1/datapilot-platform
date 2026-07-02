"""
Dynamic Agent Orchestrator
"""

from __future__ import annotations

from time import perf_counter

from agents.core.context import AgentContext
from agents.core.logger import ExecutionLogger
from agents.core.memory import Memory
from agents.core.planner import Planner
from agents.core.registry import registry
from agents.core.state import ExecutionState


class AgentOrchestrator:
    """
    Coordinates the execution of agents.
    """

    def __init__(self) -> None:

        self.planner = Planner()

        self.memory = Memory()

        self.logger = ExecutionLogger()

    def execute(
        self,
        context: AgentContext,
    ) -> AgentContext:
        """
        Execute the agent workflow.
        """

        start_time = perf_counter()

        try:

            context.state = ExecutionState.PLANNING

            plan = self.planner.create_plan(context)

            context.intent = plan.reason

            context.planned_agents = plan.queue

            self.logger.info(
                context,
                f"Execution Plan: {plan.queue}",
            )

            context.state = ExecutionState.EXECUTING

            for agent_name in plan.queue:

                agent = registry.create(agent_name)

                self.logger.info(
                    context,
                    f"Executing Agent: {agent.name}",
                )

                try:

                    agent.before_execute(context)

                    if agent.can_handle(context):

                        context = agent.execute(context)

                    else:

                        self.logger.warning(
                            context,
                            f"{agent.name} skipped."
                        )

                    agent.after_execute(context)

                except Exception as exc:

                    agent.on_error(
                        context,
                        exc,
                    )

                    context.state = ExecutionState.FAILED

                    self.logger.exception(
                        context,
                        exc,
                    )

                    break

            if context.state != ExecutionState.FAILED:

                context.state = ExecutionState.COMPLETED

        except Exception as exc:

            context.state = ExecutionState.FAILED

            self.logger.exception(
                context,
                exc,
            )

        finally:

            context.execution_time = (
                perf_counter() - start_time
            )

            self.memory.save(context)

        return context