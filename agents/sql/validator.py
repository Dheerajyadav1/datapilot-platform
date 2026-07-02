class SQLValidator:

    BLOCKED = {
        "DROP",
        "DELETE",
        "UPDATE",
        "INSERT",
        "ALTER",
        "TRUNCATE",
        "CREATE",
    }

    @classmethod
    def validate(
        cls,
        sql: str,
    ) -> None:

        upper = sql.upper()

        for keyword in cls.BLOCKED:

            if keyword in upper:
                raise ValueError(
                    f"Blocked SQL keyword: {keyword}"
                )

        if not upper.startswith("SELECT"):
            raise ValueError(
                "Only SELECT queries are allowed."
            )