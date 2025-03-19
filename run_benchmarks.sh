echo "====== COMPUTER BENCHMARKING TOOL ======"
echo "This will run a series of benchmarks to measure your computer's performance."
echo "Warning: These benchmarks may take considerable time to complete."
echo "Make sure your computer is plugged in if it's a laptop."
echo ""
echo "The benchmark will measure:"
echo "- CPU performance (32-bit integer operations)"
echo "- CPU performance (64-bit floating point operations)"
echo "- Memory performance (read/write operations)"
echo "- Disk performance (small block operations)"
echo "- Disk performance (large block operations)"
echo ""
read -p "Press Enter to start the benchmarks or Ctrl+C to cancel..."
# Create a Python virtual environment
python -m venv benchmark_env
source benchmark_env/bin/activate

# Run full suite
python benchmarks.py

# Deactivate virtual environment
deactivate

echo ""
echo "Benchmarks complete!"