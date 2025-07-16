#!/bin/bash

echo "Running AI Pair Programming Tool tests..."

# Run test examples
jac run test_examples.jac

# Run individual test files
for test_file in tests/test_*.jac; do
    echo "Running $test_file..."
    jac run "$test_file"
done

echo "All tests completed!"