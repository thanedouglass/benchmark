import time
import argparse
import numpy as np
import timeit
import os

def run_integer_benchmark(iterations=10_000_000_000):
    """
    32-bit Integer Operation Benchmark with configurable iterations
    """
    def integer_ops():
        a = 1234567
        b = 12345
        c = 987654321
        
        # Addition
        for _ in range(iterations // 3):
            a = a + 1
        
        # Multiplication
        for _ in range(iterations // 3):
            b = b * 2
        
        # Division
        for _ in range(iterations // 3):
            c = c // 2

    # Use timeit for more accurate timing
    start_time = time.time()
    timeit.timeit(integer_ops, number=1)
    elapsed_time = time.time() - start_time
    
    # Calculate operations per second
    ops_per_second = iterations / elapsed_time if elapsed_time > 0 else 0
    
    return {
        'elapsed_time': elapsed_time,
        'ops_per_second': ops_per_second
    }

def run_float_benchmark(iterations=10_000_000_000):
    """
    64-bit Floating Point Operation Benchmark with configurable iterations
    """
    def float_ops():
        a = 1234567.0
        b = 12345.0
        c = 987654321.0
        
        # Addition
        for _ in range(iterations // 3):
            a = a + 1.0
        
        # Multiplication
        for _ in range(iterations // 3):
            b = b * 2.0
        
        # Division
        for _ in range(iterations // 3):
            c = c / 2.0

    # Use timeit for more accurate timing
    start_time = time.time()
    timeit.timeit(float_ops, number=1)
    elapsed_time = time.time() - start_time
    
    # Calculate operations per second
    ops_per_second = iterations / elapsed_time if elapsed_time > 0 else 0
    
    return {
        'elapsed_time': elapsed_time,
        'ops_per_second': ops_per_second
    }

def run_memory_benchmark(iterations=5_000_000_000):
    """
    Optimized Memory Benchmark using NumPy
    """
    def numpy_memory_benchmark():
        # Create a large NumPy array
        arr = np.zeros(iterations // 1000, dtype=np.int32)
        
        # Read operations
        for _ in range(1000):
            _ = arr[0]
        
        # Write operations
        for _ in range(1000):
            arr[0] = 42

    # Use timeit for more accurate timing
    start_time = time.time()
    timeit.timeit(numpy_memory_benchmark, number=1)
    elapsed_time = time.time() - start_time
    
    # Calculate memory operations per second
    ops_per_second = iterations / elapsed_time if elapsed_time > 0 else 0
    
    return {
        'elapsed_time': elapsed_time,
        'ops_per_second': ops_per_second
    }

def print_benchmark_results(benchmark_name, results):
    """
    Print benchmark results in a formatted way
    """
    print(f"\n--- {benchmark_name} Benchmark Results ---")
    print(f"Elapsed Time:        {results['elapsed_time']:.2f} seconds")
    print(f"Operations/Second:   {results['ops_per_second']:,.0f} ops/sec")
    print(f"Performance Score:   {100 / results['elapsed_time']:.1f}%")

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Performance Benchmarking Tool")
    parser.add_argument('--integer-iterations', type=int, default=10_000_000_000, 
                        help='Number of iterations for integer benchmark')
    parser.add_argument('--float-iterations', type=int, default=10_000_000_000, 
                        help='Number of iterations for float benchmark')
    parser.add_argument('--memory-iterations', type=int, default=5_000_000_000, 
                        help='Number of iterations for memory benchmark')
    
    args = parser.parse_args()
    
    print("===== PERFORMANCE BENCHMARKING TOOL =====")
    
    # Run Integer Benchmark
    print("\nRunning 32-bit Integer Operations Benchmark...")
    int_results = run_integer_benchmark(args.integer_iterations)
    print_benchmark_results("Integer", int_results)
    
    # Run Float Benchmark
    print("\nRunning 64-bit Floating Point Benchmark...")
    float_results = run_float_benchmark(args.float_iterations)
    print_benchmark_results("Floating Point", float_results)
    
    # Run Memory Benchmark
    print("\nRunning Memory Operations Benchmark...")
    memory_results = run_memory_benchmark(args.memory_iterations)
    print_benchmark_results("Memory", memory_results)

if __name__ == "__main__":
    main()
