"""
Session Memory
"""

from __future__ import annotations

from collections import defaultdict

from agents.core.context import AgentContext


class Memory:
    """
    Stores AgentContext objects for each session.
    """

    def __init__(self) -> None:
        self._memory: dict[str, list[AgentContext]] = defaultdict(list)

    def save(
        self,
        context: AgentContext,
    ) -> None:
        """
        Save the current context.
        """

        self._memory[context.session_id].append(context)

    def get_history(
        self,
        session_id: str,
    ) -> list[AgentContext]:
        """
        Return complete conversation history.
        """

        return self._memory.get(session_id, [])

    def latest(
        self,
        session_id: str,
    ) -> AgentContext | None:
        """
        Return the latest context.
        """

        history = self.get_history(session_id)

        if not history:
            return None

        return history[-1]

    def clear(
        self,
        session_id: str,
    ) -> None:
        """
        Clear memory for a session.
        """

        self._memory.pop(session_id, None)

    def clear_all(self) -> None:
        """
        Clear all stored sessions.
        """

        self._memory.clear()

    def session_exists(
        self,
        session_id: str,
    ) -> bool:
        """
        Check if a session exists.
        """

        return session_id in self._memory