from agents.knowledge.models import KnowledgeResponse
from agents.knowledge.prompt import KNOWLEDGE_PROMPT
from agents.llm import GeminiProvider


class KnowledgeGenerator:

    def __init__(self):

        self.llm = GeminiProvider()

    def generate(
        self,
        question: str,
        context: str,
    ) -> KnowledgeResponse:

        prompt = KNOWLEDGE_PROMPT.format(

            question=question,

            context=context,
        )

        answer = self.llm.generate(prompt)

        return KnowledgeResponse(
            answer=answer.strip()
        )