from pathlib import Path

from ingestion.config import Config


class AppConfig:

    def __init__(self):

        self.project_root = Path(__file__).resolve().parents[1]

        self.page_title = "Agentic Data Platform"

        self.page_icon = "🚀"

        self.layout = "wide"

        self.initial_sidebar_state = "expanded"

        self.cache_ttl = 600

        self.theme = {
            "primary_color": "#2563EB",
            "background_color": "#F8FAFC",
            "secondary_background": "#FFFFFF",
            "text_color": "#111827",
        }

        self.database = Config()