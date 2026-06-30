from time import perf_counter

from pandas import DataFrame

from ingestion.validation.report import ValidationReport
from ingestion.validation.rules import ValidationRule


class DataValidator:

    def __init__(self, rules: list[ValidationRule]):
        self.rules = rules

    def validate(self, dataframe: DataFrame) -> ValidationReport:

        start = perf_counter()

        errors = []

        duplicate_rows = dataframe.duplicated().sum()

        for rule in self.rules:

            try:
                rule.validate(dataframe)

            except Exception as error:
                errors.append(str(error))

        execution_time = perf_counter() - start

        return ValidationReport(
            passed=len(errors) == 0,
            rows=len(dataframe),
            duplicate_rows=int(duplicate_rows),
            validation_time=execution_time,
            errors=errors,
        )