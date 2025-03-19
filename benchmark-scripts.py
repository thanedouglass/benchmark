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

def run_disk_large():
    print("\n===== Disk Benchmark (Large Blocks) =====")
    start = time.time()
    elapsed = disk_benchmark_large_block()
    print(f"Completed in {elapsed:.2f} seconds (Reference: 10 seconds)")
    print(f"Performance score: {10 / elapsed * 100:.1f}% of reference")

if __name__ == "__main__":
    print("Select a benchmark to run:")
    print("1. 32-bit Integer Operations")
    print("2. 64-bit Floating Point Operations")
    print("3. Memory Operations")
    print("4. Disk Operations (Small Blocks)")
    print("5. Disk Operations (Large Blocks)")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == "1":
        run_integer()
    elif choice == "2":
        run_float()
    elif choice == "3":
        run_memory()
    elif choice == "4":
        run_disk_small()
    elif choice == "5":
        run_disk_large()
    else:
        print("Invalid choice!")
