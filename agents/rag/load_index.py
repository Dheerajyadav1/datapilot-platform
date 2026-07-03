from pathlib import Path

from agents.rag.vector_store import VectorStore


INDEX_DIR = Path("agents/rag/index")


_cached_store = None


def load_vector_store():

    global _cached_store
    if _cached_store is not None:
        return _cached_store

    store = VectorStore()

    store.load(

        INDEX_DIR / "index.faiss",

        INDEX_DIR / "documents.pkl",
    )

    _cached_store = store
    return store