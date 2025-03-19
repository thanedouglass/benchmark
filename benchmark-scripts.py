# individual_benchmarks.py
# Allows running specific benchmarks individually
import time
from benchmarks import integer_benchmark, float_benchmark, memory_benchmark, disk_benchmark_small_block, disk_benchmark_large_block

def run_integer():
    print("\n===== 32-bit Integer Benchmark =====")
    start = time.time()
    elapsed = integer_benchmark()
    print(f"Completed in {elapsed:.2f} seconds (Reference: 100 seconds)")
    print(f"Performance score: {100 / elapsed * 100:.1f}% of reference")

def run_float():
    print("\n===== 64-bit Floating Point Benchmark =====")
    start = time.time()
    elapsed = float_benchmark()
    print(f"Completed in {elapsed:.2f} seconds (Reference: 100 seconds)")
    print(f"Performance score: {100 / elapsed * 100:.1f}% of reference")

def run_memory():
    print("\n===== Memory Benchmark =====")
    start = time.time()
    elapsed = memory_benchmark()
    print(f"Completed in {elapsed:.2f} seconds (Reference: 100 seconds)")
    print(f"Performance score: {100 / elapsed * 100:.1f}% of reference")

def run_disk_small():
    print("\n===== Disk Benchmark (Small Blocks) =====")
    start = time.time()
    elapsed = disk_benchmark_small_block()
    print(f"Completed in {elapsed:.2f} seconds (Reference: 250 seconds)")
    print(f"Performance score: {250 / elapsed * 100:.1f}% of reference")