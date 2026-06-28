from dataclasses import dataclass


@dataclass
class LoadResult:
    source: str
    table: str
    rows_loaded: int
    execution_time: float
    status: str
    message: str = ""