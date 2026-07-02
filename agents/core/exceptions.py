"""
Custom exceptions for the Agent Framework.
"""


class AgentError(Exception):
    """Base exception for all agent-related errors."""


class PlanningError(AgentError):
    """Raised when the planner fails to generate an execution plan."""


class AgentNotFoundError(AgentError):
    """Raised when an agent is not registered."""


class ToolExecutionError(AgentError):
    """Raised when a tool execution fails."""


class SQLGenerationError(AgentError):
    """Raised when SQL generation fails."""


class SQLValidationError(AgentError):
    """Raised when generated SQL is invalid or unsafe."""


class DatabaseExecutionError(AgentError):
    """Raised when SQL execution against the database fails."""


class LLMError(AgentError):
    """Raised when the LLM provider fails."""


class RAGError(AgentError):
    """Raised when document retrieval fails."""


class PipelineError(AgentError):
    """Raised when pipeline status retrieval fails."""