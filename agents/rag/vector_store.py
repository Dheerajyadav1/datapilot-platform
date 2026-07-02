import faiss
import pickle
import numpy as np


class VectorStore:

    def __init__(self):

        self.index = None
        self.documents = []

    def build(
        self,
        embeddings,
        documents,
    ):

        vectors = np.array(
            embeddings,
            dtype="float32",
        )

        self.index = faiss.IndexFlatL2(
            vectors.shape[1]
        )

        self.index.add(vectors)

        self.documents = documents

    def save(
        self,
        index_path,
        docs_path,
    ):

        faiss.write_index(
            self.index,
            str(index_path),
        )

        with open(
            str(docs_path),
            "wb",
        ) as file:

            pickle.dump(
                self.documents,
                file,
            )

    def load(
        self,
        index_path,
        docs_path,
    ):

        self.index = faiss.read_index(
            str(index_path)
        )

        with open(
            str(docs_path),
            "rb",
        ) as file:

            self.documents = pickle.load(
                file
            )

    def search(
        self,
        embedding,
        k=5,
    ):

        vector = np.array(
            [embedding],
            dtype="float32",
        )

        _, indices = self.index.search(
            vector,
            k,
        )

        return [

            self.documents[i]

            for i in indices[0]
        ]