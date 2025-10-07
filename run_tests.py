#!/usr/bin/env python3
"""
Cross-platform test runner for Python Koans
Runs all test suites and reports results
"""

import sys
import unittest
from pathlib import Path

# Add tests directory to path
sys.path.insert(0, str(Path(__file__).parent / "tests"))


def run_all_tests():
    """Run all test suites"""
    print("=" * 70)
    print("Running Python Koans Test Suite")
    print("=" * 70)
    print()

    # Discover and run all tests
    loader = unittest.TestLoader()
    start_dir = Path(__file__).parent / "tests"

    suite = loader.discover(
        start_dir=str(start_dir),
        pattern="test_*.py"
    )

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print()
    print("=" * 70)
    if result.wasSuccessful():
        print("✓ ALL TESTS PASSED!")
        print("=" * 70)
        return 0
    else:
        print("✗ SOME TESTS FAILED")
        print(f"  Failures: {len(result.failures)}")
        print(f"  Errors: {len(result.errors)}")
        print("=" * 70)
        return 1


def run_specific_suite(suite_name):
    """Run a specific test suite"""
    test_modules = {
        "structure": "test_koan_structure",
        "runner": "test_runner",
        "integration": "test_solved_koans"
    }

    if suite_name not in test_modules:
        print(f"Unknown test suite: {suite_name}")
        print(f"Available suites: {', '.join(test_modules.keys())}")
        return 1

    module_name = test_modules[suite_name]
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromName(module_name)

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Run specific suite
        exit_code = run_specific_suite(sys.argv[1])
    else:
        # Run all tests
        exit_code = run_all_tests()

    sys.exit(exit_code)
