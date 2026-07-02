from agents.llm import EmbeddingService

from agents.rag.load_index import load_vector_store


class Retriever:

    def __init__(self):

        self.embedding = EmbeddingService()

        self.vector_store = load_vector_store()

    def retrieve(
        self,
        question: str,
        k: int = 5,
    ):

        vector = self.embedding.generate(
            question
        )

        return self.vector_store.search(
            vector,
            k,
        )