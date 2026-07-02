from agents.llm import GeminiProvider
from agents.sql.models import SQLResponse
from agents.sql.parser import SQLParser
from agents.sql.prompt import SQL_PROMPT
from agents.tools.metadata_tool import MetadataTool
import json


class SQLGenerator:

    def __init__(self):

        self.llm = GeminiProvider()
        self.metadata = MetadataTool()

    def generate(
        self,
        question: str,
    ) -> SQLResponse:

        schema_data = self.metadata.execute()
        schema_info = json.dumps(schema_data, indent=2)

        prompt = SQL_PROMPT.format(
            question=question,
            schema_info=schema_info
        )

        response = self.llm.generate(
            prompt
        )

        sql = SQLParser.parse(
            response
        )

        return SQLResponse(
            sql=sql
        )