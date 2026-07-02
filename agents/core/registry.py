"""
Agent Registry
"""

from __future__ import annotations

from typing import Type

from agents.core.base_agent import BaseAgent
from agents.core.exceptions import AgentNotFoundError


class AgentRegistry:
    """
    Registry for all available agents.
    """

    def __init__(self) -> None:
        self._agents: dict[str, Type[BaseAgent]] = {}

    def register(
        self,
        agent_class: Type[BaseAgent],
    ) -> None:
        """
        Register an agent class.
        """

        self._agents[agent_class.name] = agent_class

    def unregister(
        self,
        agent_name: str,
    ) -> None:
        """
        Remove an agent from the registry.
        """

        self._agents.pop(agent_name, None)

    def create(
        self,
        agent_name: str,
    ) -> BaseAgent:
        """
        Create a new instance of an agent.
        """

        agent_class = self._agents.get(agent_name)

        if agent_class is None:
            raise AgentNotFoundError(
                f"Agent '{agent_name}' is not registered."
            )

        return agent_class()

    def exists(
        self,
        agent_name: str,
    ) -> bool:
        """
        Check if an agent is registered.
        """

        return agent_name in self._agents

    def list_agents(
        self,
    ) -> list[str]:
        """
        Return all registered agent names.
        """

        return sorted(self._agents.keys())

    def clear(
        self,
    ) -> None:
        """
        Remove all registered agents.
        """

        self._agents.clear()

    def registered(self) -> dict:

        return self._agents.copy()

    def count(self) -> int:

        return len(self._agents)

registry = AgentRegistry()