from dataclasses import dataclass


@dataclass
class SQLResponse:
    sql: str
    confidence: float = 1.0