"""
Test: Query caching performance benchmark.
Verifies that repeated queries return cached results significantly faster.

Run with: python -m tests.test_cache_perf
"""

import os
import sys
import time

# Ensure project root is in path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.database.repository import Repository
from app.database.queries import dashboard


def run_benchmark():
    repo = Repository()

    print("=" * 50)
    print("DataPilot – Cache Performance Benchmark")
    print("=" * 50)

    # Warm-up / First run (cold cache)
    print("\n[1] Running query (cold cache)...")
    start = time.time()
    df1 = repo.fetch_dataframe(dashboard.TOP_CATEGORIES)
    time1 = time.time() - start
    print(f"    ⏱  First run : {time1:.4f}s | rows={len(df1)}")

    # Second run (should be cached)
    print("\n[2] Running query (warm cache)...")
    start = time.time()
    df2 = repo.fetch_dataframe(dashboard.TOP_CATEGORIES)
    time2 = time.time() - start
    print(f"    ⏱  Second run: {time2:.4f}s | rows={len(df2)}")

    # Verification
    equal = df1.equals(df2)
    speedup = time1 / time2 if time2 > 0 else float("inf")

    print("\n" + "=" * 50)
    print(f"  Results match : {equal}")
    print(f"  Speed-up      : {speedup:.1f}x")
    print("=" * 50)


if __name__ == "__main__":
    run_benchmark()
