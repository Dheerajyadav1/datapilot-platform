from pathlib import Path

from agents.rag.loader import DocumentLoader
from agents.rag.splitter import TextSplitter
from agents.rag.embeddings import EmbeddingGenerator
from agents.rag.vector_store import VectorStore


INDEX_DIR = Path("agents/rag/index")

INDEX_DIR.mkdir(
    parents=True,
    exist_ok=True,
)


loader = DocumentLoader()

documents = loader.load_folder(".")

splitter = TextSplitter()

chunks = splitter.split(documents)

embedding_model = EmbeddingGenerator()

embeddings = embedding_model.generate(chunks)

store = VectorStore()

store.build(
    embeddings,
    chunks,
)

store.save(

    INDEX_DIR / "index.faiss",

    INDEX_DIR / "documents.pkl",
)

print("Knowledge Base Created Successfully")