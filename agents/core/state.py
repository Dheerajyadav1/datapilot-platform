from enum import Enum


class ExecutionState(str, Enum):
    """
    Represents the execution state of an agent request.
    """

    CREATED = "created"
    PLANNING = "planning"
    EXECUTING = "executing"
    WAITING = "waiting"
    COMPLETED = "completed"
    FAILED = "failed"