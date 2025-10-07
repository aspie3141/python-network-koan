#!/bin/bash
#
# Run all tests for the Python Koans project
#

echo "======================================================================"
echo "Running Python Koans Test Suite"
echo "======================================================================"
echo ""

# Change to project directory
cd "$(dirname "$0")"

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Track overall success
ALL_PASSED=true

# Function to run a test file
run_test() {
    local test_file=$1
    local test_name=$2

    echo ""
    echo "${YELLOW}Running: ${test_name}${NC}"
    echo "----------------------------------------------------------------------"

    if python3 -m pytest "$test_file" -v 2>/dev/null; then
        echo "${GREEN}✓ ${test_name} PASSED${NC}"
        return 0
    elif python3 -m unittest "$test_file" -v; then
        echo "${GREEN}✓ ${test_name} PASSED${NC}"
        return 0
    else
        echo "${RED}✗ ${test_name} FAILED${NC}"
        ALL_PASSED=false
        return 1
    fi
}

# Run each test suite
run_test "tests/test_koan_structure.py" "Koan Structure Validation"
run_test "tests/test_runner.py" "Runner Unit Tests"
run_test "tests/test_solved_koans.py" "Solved Koans Integration Tests"

# Final summary
echo ""
echo "======================================================================"
if [ "$ALL_PASSED" = true ]; then
    echo "${GREEN}✓ ALL TESTS PASSED!${NC}"
    echo "======================================================================"
    exit 0
else
    echo "${RED}✗ SOME TESTS FAILED${NC}"
    echo "======================================================================"
    exit 1
fi
