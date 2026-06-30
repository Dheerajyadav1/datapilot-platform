from dataclasses import dataclass, field


@dataclass(slots=True)
class ValidationReport:
    """
    Result of dataframe validation.
    """

    passed: bool

    rows: int

    duplicate_rows: int

    validation_time: float

    missing_columns: list[str] = field(default_factory=list)

    null_columns: dict[str, int] = field(default_factory=dict)

    errors: list[str] = field(default_factory=list)

    @property
    def error_count(self) -> int:
        return len(self.errors)