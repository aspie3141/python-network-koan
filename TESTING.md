# Testing Documentation

## Overview

The Python Koans project now has **comprehensive automated testing** to ensure quality and correctness.

## Test Suite Summary

✅ **33 Tests** - All passing
✅ **3 Test Categories** - Structure, Unit, Integration
✅ **6 Solved Koans** - Complete solutions for validation
✅ **Cross-platform** - Works on Mac, Linux, Windows

## Quick Start

### Run All Tests

```bash
# Python (cross-platform)
python3 run_tests.py

# Bash (Mac/Linux)
./run_tests.sh

# Direct unittest
python3 -m unittest discover tests
```

### Run Specific Tests

```bash
python3 run_tests.py structure     # Validate structure
python3 run_tests.py runner        # Test runner logic
python3 run_tests.py integration   # Test solutions
```

## Test Categories

### 1. Structure Validation (13 tests)

**File:** `tests/test_koan_structure.py`

Validates that koans are properly formatted:
- All expected files exist
- Docstrings present
- `__` placeholders in unsolved koans
- Assert statements with helpful messages
- Completion messages
- Naming conventions (NN_name.py)
- Sequential numbering
- Difficulty indicators
- Course goal references

### 2. Runner Unit Tests (7 tests)

**File:** `tests/test_runner.py`

Tests the koan runner logic:
- Executes solved koans successfully
- Detects assertion failures
- Detects syntax errors
- Detects undefined variables
- Handles print statements
- All solved koans pass

### 3. Integration Tests (13 tests)

**File:** `tests/test_solved_koans.py`

End-to-end testing:
- Each solved koan runs successfully
- Completion messages printed
- Learning objectives covered
- Concepts properly taught

## Test Coverage

```
Koans:           6/6 (100%)
Solved Koans:    6/6 (100%)
Documentation:   4/4 (README, QUICKSTART, OVERVIEW, ANSWER_KEY)
Scripts:         3/3 (run_koans, run_tests.py, run_tests.sh)
```

## Solved Koans (Golden Files)

Located in `tests/solved_koans/`, these are complete working solutions:

**Basic Python:**
1. `01_variables_and_strings.py` - String operations
2. `02_lists_and_loops.py` - Lists and iteration
3. `03_functions_and_dictionaries.py` - Functions and dicts

**Network Automation:**
4. `01_ip_address_validation.py` - IP/MAC validation
5. `02_device_inventory.py` - Device management
6. `03_network_monitoring.py` - Log analysis

## Expected Output

```
======================================================================
Running Python Koans Test Suite
======================================================================

test_all_koans_exist ... ok
test_koans_have_docstrings ... ok
test_runner_can_run_solved_koan ... ok
...

----------------------------------------------------------------------
Ran 33 tests in 0.333s

OK

======================================================================
✓ ALL TESTS PASSED!
======================================================================
```

## CI/CD Integration

### GitHub Actions Example

```yaml
name: Test Koans
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.11'
      - name: Run tests
        run: python3 run_tests.py
```

### GitLab CI Example

```yaml
test:
  image: python:3.11
  script:
    - python3 run_tests.py
```

## Maintenance

### Adding New Koans

When adding a new koan:

1. Create the koan file (e.g., `04_new_topic.py`)
2. Create solved version in `tests/solved_koans/`
3. Run tests: `python3 run_tests.py`
4. Update `ANSWER_KEY.md`

### Updating Existing Koans

1. Modify the koan
2. Update solved version
3. Run tests to verify: `python3 run_tests.py`
4. Update answer key if needed

## Troubleshooting

### Tests Fail

1. **Read error message** - Usually indicates the problem
2. **Check which test failed** - Gives context
3. **Verify solved koans** - Match ANSWER_KEY.md
4. **Run specific test** - `python3 run_tests.py [suite]`

### Import Errors

Run from project root:
```bash
cd /path/to/koan
python3 run_tests.py
```

### One Test Fails

Run just that test:
```bash
python3 -m unittest tests.test_runner.TestKoanRunner.test_runner_can_run_solved_koan
```

## Test Philosophy

The tests ensure:

**Quality** ✅ Well-structured, error-free koans
**Pedagogy** ✅ Teach intended concepts
**Correctness** ✅ Accurate solutions
**Completeness** ✅ All koans solvable
**Consistency** ✅ Uniform style

## Benefits

### For Teachers
- ✅ Confidence koans work correctly
- ✅ Easy to verify changes
- ✅ Quick validation of updates
- ✅ Automated quality checks

### For Students
- ✅ Koans tested before use
- ✅ Consistent experience
- ✅ Clear completion criteria
- ✅ Reliable learning path

### For Development
- ✅ Catch regressions early
- ✅ Safe refactoring
- ✅ Documentation validation
- ✅ CI/CD ready

## Statistics

```
Total Tests:               33
  Structure Tests:         13
  Runner Tests:            7
  Integration Tests:       13

Test Execution Time:       ~0.3s
Lines of Test Code:        ~500
Test Coverage:             100%

Files Tested:
  Koans:                   6
  Solved Koans:            6
  Runner:                  1
  Documentation:           4
```

## Next Steps

1. ✅ All tests passing
2. ✅ Solved koans validated
3. ✅ Structure validated
4. ✅ Ready for students

---

**For questions:** Johan Saldes - johan.saldes@lararvikarie.nu

**Last updated:** October 2025
