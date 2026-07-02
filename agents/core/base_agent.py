"""
Abstract Base Agent.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from agents.core.context import AgentContext


class BaseAgent(ABC):
    """
    Base class for every agent.
    """

    name: str = "base"
    description: str = "Base Agent"

    @abstractmethod
    def can_handle(
        self,
        context: AgentContext,
    ) -> bool:
        """
        Determine whether this agent
        can handle the current request.
        """
        raise NotImplementedError

    @abstractmethod
    def execute(
        self,
        context: AgentContext,
    ) -> AgentContext:
        """
        Execute the agent.

        Returns:
            Updated AgentContext.
        """
        raise NotImplementedError

    def before_execute(
        self,
        context: AgentContext,
    ) -> None:
        """
        Hook executed before the agent runs.
        """

        context.execution_trace.append(
            f"{self.name} started"
        )

    def after_execute(
        self,
        context: AgentContext,
    ) -> None:
        """
        Hook executed after successful execution.
        """

        context.completed_agents.append(
            self.name
        )

        context.execution_trace.append(
            f"{self.name} completed"
        )

    def on_error(
        self,
        context: AgentContext,
        error: Exception,
    ) -> None:
        """
        Hook executed if the agent fails.
        """

        context.errors.append(str(error))

        context.execution_trace.append(
            f"{self.name} failed: {error}"
        )