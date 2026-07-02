"""
Shared execution context for all agents.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any
from uuid import uuid4

import pandas as pd

from agents.core.state import ExecutionState


@dataclass
class AgentContext:
    """
    Shared context that flows through the entire agent pipeline.
    """

    # ------------------------------------------------------------------
    # Request Metadata
    # ------------------------------------------------------------------

    session_id: str = field(default_factory=lambda: str(uuid4()))
    request_id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime = field(default_factory=datetime.utcnow)

    # ------------------------------------------------------------------
    # User Request
    # ------------------------------------------------------------------

    question: str = ""
    state: ExecutionState = ExecutionState.CREATED

    # ------------------------------------------------------------------
    # Planning
    # ------------------------------------------------------------------

    intent: str | None = None
    confidence: float = 0.0

    planned_agents: list[str] = field(default_factory=list)
    completed_agents: list[str] = field(default_factory=list)

    # ------------------------------------------------------------------
    # SQL
    # ------------------------------------------------------------------

    generated_sql: str | None = None
    sql_success: bool = False
    sql_error: str | None = None

    # ------------------------------------------------------------------
    # Data
    # ------------------------------------------------------------------

    dataframe: pd.DataFrame | None = None
    dataframe_metadata: dict[str, Any] = field(default_factory=dict)

    # ------------------------------------------------------------------
    # Pipeline
    # ------------------------------------------------------------------

    pipeline_status: dict = field(default_factory=dict)

    dbt_status: dict = field(default_factory=dict)

    airflow_status: dict = field(default_factory=dict)

    # ------------------------------------------------------------------
    # Knowledge / RAG
    # ------------------------------------------------------------------

    retrieved_documents: list[str] = field(default_factory=list)


    # ------------------------------------------------------------------
    # Response
    # ------------------------------------------------------------------

    insights: list[str] = field(default_factory=list)
    recommendations: list[str] = field(default_factory=list)
    response: str = ""
    report: str = ""

    # ------------------------------------------------------------------
    # Execution
    # ------------------------------------------------------------------

    tools_used: list[str] = field(default_factory=list)
    execution_trace: list[str] = field(default_factory=list)
    execution_time: float = 0.0

    # ------------------------------------------------------------------
    # Errors
    # ------------------------------------------------------------------

    errors: list[str] = field(default_factory=list)

    # ------------------------------------------------------------------
    # Conversation
    # ------------------------------------------------------------------

    conversation_history: list[dict[str, str]] = field(default_factory=list)

    # ------------------------------------------------------------------
    # Custom Metadata
    # ------------------------------------------------------------------

    metadata: dict[str, Any] = field(default_factory=dict)