# Koan Tests

This directory contains comprehensive tests for the Python Koans project.

## Test Structure

```
tests/
├── README.md                    # This file
├── __init__.py                  # Python package marker
│
├── test_koan_structure.py       # Validates koan format and structure
├── test_runner.py              # Unit tests for the runner
├── test_solved_koans.py        # Integration tests for solved koans
│
└── solved_koans/               # Correct solutions for testing
    ├── basic_python/
    │   ├── 01_variables_and_strings.py
    │   ├── 02_lists_and_loops.py
    │   └── 03_functions_and_dictionaries.py
    └── network_automation/
        ├── 01_ip_address_validation.py
        ├── 02_device_inventory.py
        └── 03_network_monitoring.py
```

## Running Tests

### Run All Tests

**Option 1: Python script (cross-platform)**
```bash
python3 run_tests.py
```

**Option 2: Bash script (Mac/Linux)**
```bash
./run_tests.sh
```

**Option 3: Direct unittest**
```bash
python3 -m unittest discover tests
```

### Run Specific Test Suite

```bash
python3 run_tests.py structure     # Validate koan structure
python3 run_tests.py runner        # Test the runner
python3 run_tests.py integration   # Test solved koans
```

### Run Individual Test File

```bash
python3 -m unittest tests/test_koan_structure.py
python3 -m unittest tests/test_runner.py
python3 -m unittest tests/test_solved_koans.py
```

## Test Coverage

### 1. Structure Validation (`test_koan_structure.py`)

Tests that koans are properly formatted:
- ✅ All expected koans exist
- ✅ Koans have docstrings
- ✅ Unsolved koans have `__` placeholders
- ✅ Koans use `assert` statements
- ✅ Assert statements have helpful messages
- ✅ Koans have completion messages
- ✅ Naming convention is followed (NN_name.py)
- ✅ Koans are numbered sequentially
- ✅ Difficulty levels are indicated
- ✅ Network koans reference course goals

### 2. Runner Tests (`test_runner.py`)

Tests the koan runner logic:
- ✅ Runner can execute solved koans
- ✅ Runner detects assertion failures
- ✅ Runner detects syntax errors
- ✅ Runner detects undefined variables (NameError)
- ✅ Runner handles print statements
- ✅ All solved koans pass

### 3. Integration Tests (`test_solved_koans.py`)

Tests that solved koans work end-to-end:
- ✅ Each solved koan runs successfully
- ✅ Koans print completion messages
- ✅ All assertions pass
- ✅ Learning objectives are covered

## What Gets Tested

### Basic Python Koans
1. **Variables & Strings** - string operations, formatting, methods
2. **Lists & Loops** - lists, for loops, comprehensions
3. **Functions & Dicts** - functions, dictionaries, complex data

### Network Automation Koans
4. **IP Validation** - IP addresses, CIDR, subnets, MAC addresses
5. **Device Inventory** - inventory management, CSV, data handling
6. **Network Monitoring** - log parsing, metrics, alerting

## CI/CD Usage

These tests can be integrated into CI/CD pipelines:

```yaml
# Example GitHub Actions
- name: Run Koan Tests
  run: python3 run_tests.py
```

## Expected Output

When all tests pass:
```
======================================================================
Running Python Koans Test Suite
======================================================================

test_all_koans_exist (__main__.TestKoanStructure) ... ok
test_koans_have_docstrings (__main__.TestKoanStructure) ... ok
...
----------------------------------------------------------------------
Ran 30 tests in 2.345s

OK

======================================================================
✓ ALL TESTS PASSED!
======================================================================
```

## Troubleshooting

### Import Errors
Make sure you're running tests from the project root:
```bash
cd /path/to/koan
python3 run_tests.py
```

### Test Failures
If tests fail:
1. Read the error message carefully
2. Check the specific test that failed
3. Verify the koan file being tested
4. Ensure solved koans match ANSWER_KEY.md

### Missing Dependencies
Tests use only Python standard library, no external dependencies needed.

## Adding New Tests

To add new tests:

1. Create a new test class in the appropriate file
2. Follow the naming convention: `test_*`
3. Use descriptive test names
4. Add docstrings explaining what's being tested

Example:
```python
class TestNewFeature(unittest.TestCase):
    """Test description"""

    def test_specific_behavior(self):
        """Test that X does Y"""
        # Test code here
        self.assertEqual(actual, expected)
```

## Test Philosophy

These tests ensure:
- **Quality**: Koans are well-structured and error-free
- **Pedagogy**: Koans teach the intended concepts
- **Correctness**: Solutions are accurate
- **Completeness**: All koans can be completed
- **Consistency**: Formatting and style are uniform

---

**For questions or issues, contact Johan Saldes**
