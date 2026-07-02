from agents.core.base_agent import BaseAgent
from agents.core.context import AgentContext
from agents.sql.generator import SQLGenerator
from agents.sql.validator import SQLValidator
from agents.tools.database_tool import DatabaseTool


class SQLAgent(BaseAgent):

    name = "sql"

    description = "Generate and execute SQL."

    def __init__(self):

        self.generator = SQLGenerator()

        self.database = DatabaseTool()

    def can_handle(
        self,
        context: AgentContext,
    ) -> bool:

        return True

    def execute(
        self,
        context: AgentContext,
    ) -> AgentContext:

        response = self.generator.generate(
            context.question
        )

        SQLValidator.validate(
            response.sql
        )

        df = self.database.execute(
            response.sql
        )

        context.generated_sql = response.sql

        context.sql_success = True

        context.dataframe = df

        context.tools_used.append(
            "database"
        )

        return context