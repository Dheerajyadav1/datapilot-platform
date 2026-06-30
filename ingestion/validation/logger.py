from ingestion.logger import LoggerManager
from ingestion.validation.report import ValidationReport


class ValidationLogger:

    def __init__(self, logger_manager: LoggerManager):

        self.logger = logger_manager.get_logger(
            "Validation"
        )

    def log(
        self,
        report: ValidationReport,
    ):

        self.logger.info("=" * 60)
        self.logger.info("VALIDATION REPORT")
        self.logger.info("=" * 60)

        self.logger.info(
            f"Rows              : {report.rows:,}"
        )

        self.logger.info(
            f"Duplicate Rows    : {report.duplicate_rows}"
        )

        self.logger.info(
            f"Passed            : {report.passed}"
        )

        self.logger.info(
            f"Execution Time    : "
            f"{report.validation_time:.4f} sec"
        )

        if report.errors:

            self.logger.error("Errors")

            for error in report.errors:
                self.logger.error(f"• {error}")

        self.logger.info("=" * 60)