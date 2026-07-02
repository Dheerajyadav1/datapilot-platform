class SQLParser:

    @staticmethod
    def parse(response: str) -> str:

        response = response.strip()

        response = response.replace(
            "```sql",
            ""
        )

        response = response.replace(
            "```",
            ""
        )

        return response.strip()