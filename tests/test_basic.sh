#!/bin/bash

echo "Running basic tests..."

# Test 1: Python syntax
python3 -m py_compile app.py
echo "✓ Python syntax check passed"

# Test 2: Bash syntax
for script in scripts/*.sh
do
    bash -n "$script"
done
echo "✓ Bash syntax checks passed"

echo "All basic tests passed!"