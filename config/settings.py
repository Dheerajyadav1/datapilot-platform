from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    # --------------------------------------------------
    # PostgreSQL
    # --------------------------------------------------

    POSTGRES_HOST = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT")
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")

    # --------------------------------------------------
    # Gemini
    # --------------------------------------------------

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    GEMINI_MODEL = os.getenv(
        "GEMINI_MODEL",
        "gemini-2.5-pro"
    )

    EMBEDDING_MODEL = os.getenv(
        "EMBEDDING_MODEL",
        "models/text-embedding-004"
    )

    # --------------------------------------------------
    # Agent Framework
    # --------------------------------------------------

    MAX_AGENT_ITERATIONS = int(
        os.getenv("MAX_AGENT_ITERATIONS", "10")
    )

    AGENT_LOG_LEVEL = os.getenv(
        "AGENT_LOG_LEVEL",
        "INFO"
    )

    # --------------------------------------------------
    # Vector Store
    # --------------------------------------------------

    VECTOR_STORE_PATH = os.getenv(
        "VECTOR_STORE_PATH",
        "vector_store/faiss_index"
    )

    # --------------------------------------------------
    # Application
    # --------------------------------------------------

    APP_NAME = "DataPilot"

    APP_VERSION = "1.0.0"

    @property
    def DATABASE_URL(self):

        return (
            f"postgresql://"
            f"{self.POSTGRES_USER}:"
            f"{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:"
            f"{self.POSTGRES_PORT}/"
            f"{self.POSTGRES_DB}"
        )


settings = Settings()