from pandas import DataFrame

from ingestion.validation.exceptions import (
    DuplicateRowsError,
    EmptyDataFrameError,
    MissingColumnsError,
)


class ValidationRule:

    def validate(self, dataframe: DataFrame):
        raise NotImplementedError


class NotEmptyRule(ValidationRule):

    def validate(self, dataframe: DataFrame):

        if dataframe.empty:
            raise EmptyDataFrameError(
                "DataFrame is empty."
            )


class RequiredColumnsRule(ValidationRule):

    def __init__(self, columns: list[str]):
        self.columns = columns

    def validate(self, dataframe: DataFrame):

        missing = set(self.columns) - set(dataframe.columns)

        if missing:
            raise MissingColumnsError(
                f"Missing columns: {sorted(missing)}"
            )


class NoDuplicateRule(ValidationRule):

    def __init__(self, columns: list[str] = None):
        self.columns = columns

    def validate(self, dataframe: DataFrame):

        subset = self.columns if self.columns else None
        duplicates = dataframe.duplicated(subset=subset).sum()

        if duplicates:
            col_desc = f"on columns {self.columns}" if self.columns else "across all columns"
            raise DuplicateRowsError(
                f"{duplicates} duplicate rows detected {col_desc}."
            )