"""
Execution Logger
"""

from __future__ import annotations

import logging

from agents.core.context import AgentContext


class ExecutionLogger:
    """
    Logs agent execution details and updates the execution trace.
    """

    def __init__(
        self,
        logger_name: str = "agent_framework",
    ) -> None:

        self.logger = logging.getLogger(logger_name)

    def info(
        self,
        context: AgentContext,
        message: str,
    ) -> None:
        """
        Log an info message.
        """

        context.execution_trace.append(message)

        self.logger.info(message)

    def warning(
        self,
        context: AgentContext,
        message: str,
    ) -> None:
        """
        Log a warning message.
        """

        context.execution_trace.append(
            f"WARNING: {message}"
        )

        self.logger.warning(message)

    def error(
        self,
        context: AgentContext,
        message: str,
    ) -> None:
        """
        Log an error message.
        """

        context.errors.append(message)

        context.execution_trace.append(
            f"ERROR: {message}"
        )

        self.logger.error(message)

    def exception(
        self,
        context: AgentContext,
        exception: Exception,
    ) -> None:
        """
        Log an exception.
        """

        self.error(
            context,
            str(exception),
        )