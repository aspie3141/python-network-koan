"""
Unit tests for the koan runner
Tests the runner logic without running actual koans
"""

import unittest
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from run_koans import run_koan


class TestKoanRunner(unittest.TestCase):
    """Test the koan runner functions"""

    def setUp(self):
        """Set up test fixtures"""
        self.test_dir = Path(__file__).parent
        self.solved_dir = self.test_dir / "solved_koans"

    def test_runner_can_run_solved_koan(self):
        """Test that runner can execute a solved koan"""
        koan_path = self.solved_dir / "basic_python" / "01_variables_and_strings.py"
        passed, message = run_koan(koan_path)

        self.assertTrue(passed, f"Solved koan should pass: {message}")
        self.assertIn("Passed", message)

    def test_runner_detects_failed_assertion(self):
        """Test that runner detects assertion failures"""
        # Create a temporary koan with a failing assertion
        temp_koan = self.test_dir / "temp_failing_koan.py"
        temp_koan.write_text("assert False, 'This should fail'")

        try:
            passed, message = run_koan(temp_koan)

            self.assertFalse(passed, "Failing koan should not pass")
            self.assertIn("Failed", message)
            self.assertIn("This should fail", message)
        finally:
            temp_koan.unlink()  # Clean up

    def test_runner_detects_syntax_error(self):
        """Test that runner detects syntax errors"""
        temp_koan = self.test_dir / "temp_syntax_error.py"
        temp_koan.write_text("this is not valid python $$$$")

        try:
            passed, message = run_koan(temp_koan)

            self.assertFalse(passed, "Koan with syntax error should not pass")
            self.assertIn("Error", message)
        finally:
            temp_koan.unlink()

    def test_runner_detects_name_error(self):
        """Test that runner detects NameError (undefined variables)"""
        temp_koan = self.test_dir / "temp_name_error.py"
        temp_koan.write_text("assert undefined_variable == 'value'")

        try:
            passed, message = run_koan(temp_koan)

            self.assertFalse(passed, "Koan with undefined variable should not pass")
            self.assertIn("Error", message)
            self.assertIn("undefined_variable", message)
        finally:
            temp_koan.unlink()

    def test_runner_handles_print_statements(self):
        """Test that runner handles koans with print statements"""
        temp_koan = self.test_dir / "temp_print_koan.py"
        temp_koan.write_text("""
print("Test message")
assert True
""")

        try:
            passed, message = run_koan(temp_koan)

            self.assertTrue(passed, "Koan with print should pass")
        finally:
            temp_koan.unlink()


class TestSolvedKoansPass(unittest.TestCase):
    """Test that all solved koans pass"""

    def setUp(self):
        self.solved_dir = Path(__file__).parent / "solved_koans"

    def test_all_basic_python_koans_pass(self):
        """Test that all basic Python solved koans pass"""
        basic_python_dir = self.solved_dir / "basic_python"
        koan_files = sorted(basic_python_dir.glob("*.py"))

        self.assertGreater(len(koan_files), 0, "Should have basic Python koans")

        for koan_file in koan_files:
            with self.subTest(koan=koan_file.name):
                passed, message = run_koan(koan_file)
                self.assertTrue(passed, f"{koan_file.name} should pass: {message}")

    def test_all_network_automation_koans_pass(self):
        """Test that all network automation solved koans pass"""
        network_dir = self.solved_dir / "network_automation"
        koan_files = sorted(network_dir.glob("*.py"))

        self.assertGreater(len(koan_files), 0, "Should have network automation koans")

        for koan_file in koan_files:
            with self.subTest(koan=koan_file.name):
                passed, message = run_koan(koan_file)
                self.assertTrue(passed, f"{koan_file.name} should pass: {message}")


if __name__ == "__main__":
    unittest.main()
