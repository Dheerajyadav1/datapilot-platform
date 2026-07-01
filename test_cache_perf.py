import time
import os
import sys

# Ensure project root is in path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../Desktop/agentic-data-platform")))

from app.database.repository import Repository
from app.database.queries import dashboard

repo = Repository()

# Warm up/First run
print("Running query 1...")
start = time.time()
df1 = repo.fetch_dataframe(dashboard.TOP_CATEGORIES)
time1 = time.time() - start
print(f"Query 1 took {time1:.4f} seconds, rows={len(df1)}")

# Second run (should be cached)
print("Running query 2 (cached)...")
start = time.time()
df2 = repo.fetch_dataframe(dashboard.TOP_CATEGORIES)
time2 = time.time() - start
print(f"Query 2 took {time2:.4f} seconds, rows={len(df2)}")

# Verify equality
print("Are dataframes equal?", df1.equals(df2))
