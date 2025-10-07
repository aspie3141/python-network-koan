"""
Integration tests for solved koans
Tests that all solved versions work correctly and teach the right concepts
"""

import unittest
from pathlib import Path
import subprocess
import sys


class TestSolvedKoansIntegration(unittest.TestCase):
    """Integration tests for solved koans"""

    def setUp(self):
        self.solved_dir = Path(__file__).parent / "solved_koans"
        self.python = sys.executable

    def run_koan_as_script(self, koan_path):
        """Run a koan as a standalone script"""
        result = subprocess.run(
            [self.python, str(koan_path)],
            capture_output=True,
            text=True
        )
        return result

    def test_basic_python_01_runs_successfully(self):
        """Test that solved koan 01 runs without errors"""
        koan = self.solved_dir / "basic_python" / "01_variables_and_strings.py"
        result = self.run_koan_as_script(koan)

        self.assertEqual(result.returncode, 0, f"Koan should run successfully. Error: {result.stderr}")
        self.assertIn("✓", result.stdout, "Should print completion message")

    def test_basic_python_02_runs_successfully(self):
        """Test that solved koan 02 runs without errors"""
        koan = self.solved_dir / "basic_python" / "02_lists_and_loops.py"
        result = self.run_koan_as_script(koan)

        self.assertEqual(result.returncode, 0, f"Koan should run successfully. Error: {result.stderr}")
        self.assertIn("✓", result.stdout, "Should print completion message")

    def test_basic_python_03_runs_successfully(self):
        """Test that solved koan 03 runs without errors"""
        koan = self.solved_dir / "basic_python" / "03_functions_and_dictionaries.py"
        result = self.run_koan_as_script(koan)

        self.assertEqual(result.returncode, 0, f"Koan should run successfully. Error: {result.stderr}")
        self.assertIn("✓", result.stdout, "Should print completion message")

    def test_network_01_runs_successfully(self):
        """Test that solved network koan 01 runs without errors"""
        koan = self.solved_dir / "network_automation" / "01_ip_address_validation.py"
        result = self.run_koan_as_script(koan)

        self.assertEqual(result.returncode, 0, f"Koan should run successfully. Error: {result.stderr}")
        self.assertIn("✓", result.stdout, "Should print completion message")

    def test_network_02_runs_successfully(self):
        """Test that solved network koan 02 runs without errors"""
        koan = self.solved_dir / "network_automation" / "02_device_inventory.py"
        result = self.run_koan_as_script(koan)

        self.assertEqual(result.returncode, 0, f"Koan should run successfully. Error: {result.stderr}")
        self.assertIn("✓", result.stdout, "Should print completion message")

    def test_network_03_runs_successfully(self):
        """Test that solved network koan 03 runs without errors"""
        koan = self.solved_dir / "network_automation" / "03_network_monitoring.py"
        result = self.run_koan_as_script(koan)

        self.assertEqual(result.returncode, 0, f"Koan should run successfully. Error: {result.stderr}")
        self.assertIn("✓", result.stdout, "Should print completion message")

    def test_all_solved_koans_pass(self):
        """Test that all solved koans pass when run"""
        all_koans = list(self.solved_dir.rglob("*.py"))

        self.assertGreaterEqual(len(all_koans), 6, "Should have at least 6 solved koans")

        for koan in all_koans:
            with self.subTest(koan=koan.name):
                result = self.run_koan_as_script(koan)
                self.assertEqual(
                    result.returncode,
                    0,
                    f"{koan.name} failed: {result.stderr}"
                )


class TestLearningObjectives(unittest.TestCase):
    """Test that koans cover the intended learning objectives"""

    def setUp(self):
        self.koan_dir = Path(__file__).parent.parent
        self.basic_dir = self.koan_dir / "basic_python"
        self.network_dir = self.koan_dir / "network_automation"

    def test_koan_01_teaches_strings(self):
        """Test that koan 01 teaches string manipulation"""
        koan = self.basic_dir / "01_variables_and_strings.py"
        content = koan.read_text()

        # Should teach these concepts
        concepts = [
            "concatenation",  # String concatenation
            "len(",          # String length
            ".upper()",      # String methods
            ".lower()",
            "f\"",           # F-strings or formatting
            "["              # String slicing
        ]

        for concept in concepts:
            self.assertIn(concept, content, f"Koan 01 should teach {concept}")

    def test_koan_02_teaches_lists_and_loops(self):
        """Test that koan 02 teaches lists and loops"""
        koan = self.basic_dir / "02_lists_and_loops.py"
        content = koan.read_text()

        concepts = [
            "for ",          # For loops
            ".append(",      # List methods
            ".remove(",
            "[",             # List indexing
            "len(",          # List length
            "for n in",      # List comprehension indicator
            ".split(",       # String split
            ".join("         # String join
        ]

        for concept in concepts:
            self.assertIn(concept, content, f"Koan 02 should teach {concept}")

    def test_koan_03_teaches_functions_and_dicts(self):
        """Test that koan 03 teaches functions and dictionaries"""
        koan = self.basic_dir / "03_functions_and_dictionaries.py"
        content = koan.read_text()

        concepts = [
            "def ",          # Function definition
            "return",        # Return statement
            "{",             # Dictionary
            '["',            # Dictionary key access
            "in device",     # Dictionary membership
        ]

        for concept in concepts:
            self.assertIn(concept, content, f"Koan 03 should teach {concept}")

    def test_network_koan_01_teaches_ip_validation(self):
        """Test that network koan 01 teaches IP validation"""
        koan = self.network_dir / "01_ip_address_validation.py"
        content = koan.read_text()

        concepts = [
            ".split(",       # IP parsing
            "192.168",       # Private IP examples
            "/",             # CIDR notation
            "255.255",       # Subnet mask
            "MAC",           # MAC address
        ]

        for concept in concepts:
            self.assertIn(concept, content, f"Network koan 01 should teach {concept}")

    def test_network_koan_02_teaches_inventory(self):
        """Test that network koan 02 teaches device inventory"""
        koan = self.network_dir / "02_device_inventory.py"
        content = koan.read_text()

        concepts = [
            "hostname",      # Device properties
            "CSV",           # CSV handling
            "export",        # Export functionality
            "parse",         # Parsing
            "[d for d",      # List comprehension
        ]

        for concept in concepts:
            self.assertIn(concept, content, f"Network koan 02 should teach {concept}")

    def test_network_koan_03_teaches_monitoring(self):
        """Test that network koan 03 teaches monitoring"""
        koan = self.network_dir / "03_network_monitoring.py"
        content = koan.read_text()

        concepts = [
            "log",           # Logging
            "ERROR",         # Log levels
            "WARNING",
            "cpu",           # Performance metrics
            "bandwidth",
            "alert",         # Alerting
        ]

        for concept in concepts:
            self.assertIn(concept, content, f"Network koan 03 should teach {concept}")


if __name__ == "__main__":
    unittest.main()
