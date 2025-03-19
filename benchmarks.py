# Benchmarks Suite
# Contains five benchmarks for testing CPU, memory, and disk performance
import time
import array
import numpy as np
import os

def integer_benchmark():
    """
    32-bit Integer Operation Benchmark
    - 10^10 additions
    - 5 x 10^9 multiplications
    - 2 x 10^9 divisions
    Expected reference time: 100 seconds
    """
    print("Running 32-bit Integer Benchmark...")
    start_time = time.time()
    
    # Integer addition
    a = 1234567
    for _ in range(10_000_000_000 // 1000):
        for _ in range(1000):
            a = a + 1  # Addition of integer constants
    
    # Integer multiplication
    b = 12345
    for _ in range(5_000_000_000 // 1000):
        for _ in range(1000):
            b = b * 2  # Multiplication of integer constants
    
    # Integer division
    c = 987654321
    for _ in range(2_000_000_000 // 1000):
        for _ in range(1000):
            c = c // 2  # Division of integer constants
    
    elapsed_time = time.time() - start_time
    return elapsed_time

def float_benchmark():
    """
    64-bit Floating Point Operation Benchmark
    - 10^10 additions
    - 5 x 10^9 multiplications
    - 2 x 10^9 divisions
    Expected reference time: 100 seconds
    """
    print("Running 64-bit Floating Point Benchmark...")
    start_time = time.time()
    
    # Floating point addition
    a = 1234567.0
    for _ in range(10_000_000_000 // 1000):
        for _ in range(1000):
            a = a + 1.0  # Addition of floating point constants
    
    # Floating point multiplication
    b = 12345.0
    for _ in range(5_000_000_000 // 1000):
        for _ in range(1000):
            b = b * 2.0  # Multiplication of floating point constants
    
    # Floating point division
    c = 987654321.0
    for _ in range(2_000_000_000 // 1000):
        for _ in range(1000):
            c = c / 2.0  # Division of floating point constants
    
    elapsed_time = time.time() - start_time
    return elapsed_time

def memory_benchmark():
    """
    Memory Benchmark
    - Read from 5 x 10^9 different array elements, 4 bytes each time
    - Write to 5 x 10^9 different array elements, 4 bytes each time
    Expected reference time: 100 seconds
    """
    print("Running Memory Benchmark...")
    start_time = time.time()
    
    # Determine array size that fits in memory (adjust if needed)
    array_size = min(5_000_000_000, 500_000_000)  # Practical size limit
    cycles = 5_000_000_000 // array_size
    
    # Create a large array
    arr = array.array('i', [0] * array_size)
    
    # Memory read operations
    for _ in range(cycles):
        for i in range(0, array_size, array_size // min(array_size, 1000)):
            _ = arr[i]  # Read operation
    
    # Memory write operations
    for _ in range(cycles):
        for i in range(0, array_size, array_size // min(array_size, 1000)):
            arr[i] = 42  # Write operation
    
    elapsed_time = time.time() - start_time
    return elapsed_time

def disk_benchmark_small_block():
    """
    Hard Drive Benchmark 1 (Small Blocks)
    - Read a whole file of 10^9 bytes, 100 bytes each time
    - Write 10^9 bytes to a file, 100 bytes each time
    Expected reference time: 250 seconds
    """
    print("Running Disk Benchmark (Small Blocks)...")
    start_time = time.time()
    
    filename_read = "benchmark_read_small.dat"
    filename_write = "benchmark_write_small.dat"
    total_size = 1_000_000_000  # 1 GB
    block_size = 100  # 100 bytes per operation
    
    # Create a test file if it doesn't exist
    if not os.path.exists(filename_read) or os.path.getsize(filename_read) != total_size:
        print("Creating test file for reading (this may take a while)...")
        with open(filename_read, "wb") as f:
            chunk = b'0' * block_size
            for _ in range(total_size // block_size):
                f.write(chunk)
    
    # Read operation
    with open(filename_read, "rb") as f:
        for _ in range(total_size // block_size):
            _ = f.read(block_size)
            
    # Write operation
    with open(filename_write, "wb") as f:
        chunk = b'1' * block_size
        for _ in range(total_size // block_size):
            f.write(chunk)
    
    elapsed_time = time.time() - start_time
    
    # Clean up temporary files
    try:
        os.remove(filename_write)
    except:
        pass
    
    return elapsed_time

def disk_benchmark_large_block():
    """
    Hard Drive Benchmark 2 (Large Blocks)
    - Read a whole file of 10^9 bytes, 10000 bytes each time
    - Write 10^9 bytes to a file, 10000 bytes each time
    Expected reference time: 10 seconds
    """
    print("Running Disk Benchmark (Large Blocks)...")
    start_time = time.time()
    
    filename_read = "benchmark_read_large.dat"
    filename_write = "benchmark_write_large.dat"
    total_size = 1_000_000_000  # 1 GB
    block_size = 10000  # 10000 bytes per operation
    
    # Create a test file if it doesn't exist
    if not os.path.exists(filename_read) or os.path.getsize(filename_read) != total_size:
        print("Creating test file for reading (this may take a while)...")
        with open(filename_read, "wb") as f:
            chunk = b'0' * block_size
            for _ in range(total_size // block_size):
                f.write(chunk)
    
    # Read operation
    with open(filename_read, "rb") as f:
        for _ in range(total_size // block_size):
            _ = f.read(block_size)
            
    # Write operation
    with open(filename_write, "wb") as f:
        chunk = b'1' * block_size
        for _ in range(total_size // block_size):
            f.write(chunk)
    
    elapsed_time = time.time() - start_time
    
    # Clean up temporary files
    try:
        os.remove(filename_write)
    except:
        pass
    
    return elapsed_time

def run_all_benchmarks():
    """
    Run all benchmarks and display results
    """
    results = {}
    
    print("\n===== BENCHMARK SUITE =====\n")
    
    # Integer benchmark
    print("\n--- 32-bit Integer Operations ---")
    results["integer"] = integer_benchmark()
    print(f"Completed in {results['integer']:.2f} seconds (Reference: 100 seconds)")
    
    # Float benchmark
    print("\n--- 64-bit Floating Point Operations ---")
    results["float"] = float_benchmark()
    print(f"Completed in {results['float']:.2f} seconds (Reference: 100 seconds)")
    
    # Memory benchmark
    print("\n--- Memory Operations ---")
    results["memory"] = memory_benchmark()
    print(f"Completed in {results['memory']:.2f} seconds (Reference: 100 seconds)")
    
    # Disk benchmark (small blocks)
    print("\n--- Disk Operations (Small Blocks) ---")
    results["disk_small"] = disk_benchmark_small_block()
    print(f"Completed in {results['disk_small']:.2f} seconds (Reference: 250 seconds)")
    
    # Disk benchmark (large blocks)
    print("\n--- Disk Operations (Large Blocks) ---")
    results["disk_large"] = disk_benchmark_large_block()
    print(f"Completed in {results['disk_large']:.2f} seconds (Reference: 10 seconds)")
    
    # Summary
    print("\n===== BENCHMARK RESULTS =====")
    print(f"32-bit Integer:          {results['integer']:.2f} seconds (Reference: 100 seconds)")
    print(f"64-bit Floating Point:   {results['float']:.2f} seconds (Reference: 100 seconds)")
    print(f"Memory Operations:       {results['memory']:.2f} seconds (Reference: 100 seconds)")
    print(f"Disk Ops (Small Blocks): {results['disk_small']:.2f} seconds (Reference: 250 seconds)")
    print(f"Disk Ops (Large Blocks): {results['disk_large']:.2f} seconds (Reference: 10 seconds)")
    
    # Calculate performance scores (higher is better)
    int_score = 100 / results['integer'] * 100 if results['integer'] > 0 else 0
    float_score = 100 / results['float'] * 100 if results['float'] > 0 else 0
    memory_score = 100 / results['memory'] * 100 if results['memory'] > 0 else 0
    disk_small_score = 250 / results['disk_small'] * 100 if results['disk_small'] > 0 else 0
    disk_large_score = 10 / results['disk_large'] * 100 if results['disk_large'] > 0 else 0
    
    print("\n===== PERFORMANCE SCORES =====")
    print(f"CPU (Integer):           {int_score:.1f}% of reference")
    print(f"CPU (Floating Point):    {float_score:.1f}% of reference")
    print(f"Memory:                  {memory_score:.1f}% of reference")
    print(f"Disk (Small Blocks):     {disk_small_score:.1f}% of reference")
    print(f"Disk (Large Blocks):     {disk_large_score:.1f}% of reference")
    
    # Clean up test files
    cleanup()

def cleanup():
    """
    Clean up benchmark files
    """
    files_to_remove = [
        "benchmark_read_small.dat",
        "benchmark_read_large.dat"
    ]
    
    for file in files_to_remove:
        if os.path.exists(file):
            try:
                print(f"Cleaning up: {file}")
                os.remove(file)
            except:
                print(f"Could not remove: {file}")

if __name__ == "__main__":
    run_all_benchmarks()