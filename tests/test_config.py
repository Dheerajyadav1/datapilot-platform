from ingestion.config import Config

config = Config()

print(config.project_root)
print(config.database_url)
print(config.tables.keys())