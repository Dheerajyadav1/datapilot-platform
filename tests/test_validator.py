import pandas as pd

from ingestion.validation import (
    DataValidator,
    NotEmptyRule,
    NoDuplicateRule,
)


def test_empty_dataframe():

    validator = DataValidator(
        [
            NotEmptyRule(),
        ]
    )

    report = validator.validate(
        pd.DataFrame()
    )

    assert not report.passed


def test_duplicate_rows():

    df = pd.DataFrame(
        {
            "id": [1, 1]
        }
    )

    validator = DataValidator(
        [
            NoDuplicateRule(),
        ]
    )

    report = validator.validate(df)

    assert not report.passed


def test_success():

    df = pd.DataFrame(
        {
            "id": [1, 2]
        }
    )

    validator = DataValidator(
        [
            NotEmptyRule(),
            NoDuplicateRule(),
        ]
    )

    report = validator.validate(df)

    assert report.passed