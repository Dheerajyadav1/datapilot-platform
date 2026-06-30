class ValidationError(Exception):
    """Base validation exception."""


class EmptyDataFrameError(ValidationError):
    """Raised when dataframe is empty."""


class MissingColumnsError(ValidationError):
    """Raised when required columns are missing."""


class DuplicateRowsError(ValidationError):
    """Raised when duplicate rows exist."""


class NullValuesError(ValidationError):
    """Raised when excessive null values exist."""


class DataTypeError(ValidationError):
    """Raised when datatype validation fails."""