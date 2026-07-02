from pathlib import Path

from agents.rag.vector_store import VectorStore


INDEX_DIR = Path("agents/rag/index")


def load_vector_store():

    store = VectorStore()

    store.load(

        INDEX_DIR / "index.faiss",

        INDEX_DIR / "documents.pkl",
    )

    return store