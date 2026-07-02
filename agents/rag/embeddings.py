from agents.llm import EmbeddingService


class EmbeddingGenerator:

    def __init__(self):

        self.model = EmbeddingService()

    def generate(
        self,
        chunks,
    ):

        return [

            self.model.generate(chunk)

            for chunk in chunks

        ]