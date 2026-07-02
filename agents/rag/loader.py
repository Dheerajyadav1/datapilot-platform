from pathlib import Path


class DocumentLoader:

    def load_folder(
        self,
        folder: str,
    ) -> list[str]:

        documents = []

        for file in Path(folder).rglob("*"):

            # Exclude virtual environments, git repositories, caching, target builds, etc.
            if any(part in file.parts for part in (".venv", ".git", "__pycache__", "target", ".gemini", "logs", ".idea", ".vscode")):
                continue

            if file.suffix.lower() in (
                ".txt",
                ".md",
                ".py",
                ".sql",
                ".yml",
            ):

                try:

                    documents.append(
                        file.read_text(
                            encoding="utf-8",
                            errors="ignore",
                        )
                    )

                except Exception:

                    continue

        return documents