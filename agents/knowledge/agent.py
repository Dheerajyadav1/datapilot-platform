from agents.core.base_agent import BaseAgent
from agents.core.context import AgentContext
from agents.knowledge.generator import KnowledgeGenerator
from agents.rag.retriever import Retriever


class KnowledgeAgent(BaseAgent):

    name = "knowledge"

    description = "Knowledge Agent"

    def __init__(self):

        self.generator = KnowledgeGenerator()

        self.retriever = Retriever()

    def can_handle(
        self,
        context: AgentContext,
    ) -> bool:

        return True

    def execute(
        self,
        context: AgentContext,
    ) -> AgentContext:

        documents = self.retriever.retrieve(
            context.question
        )

        context.retrieved_documents = documents

        rag_context = "\n\n".join(documents)

        response = self.generator.generate(

            question=context.question,

            context=rag_context,
        )

        context.response = response.answer

        return context