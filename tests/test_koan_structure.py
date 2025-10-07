"""
Tests to validate koan structure and format
Ensures koans have proper placeholders, documentation, etc.
"""

import unittest
from pathlib import Path
import re


class TestKoanStructure(unittest.TestCase):
    """Test that koans are properly structured"""

    def setUp(self):
        """Set up test fixtures"""
        self.koan_dir = Path(__file__).parent.parent
        self.basic_python_dir = self.koan_dir / "basic_python"
        self.network_dir = self.koan_dir / "network_automation"

    def test_all_koans_exist(self):
        """Test that all expected koans are present"""
        expected_basic = [
            "01_variables_and_strings.py",
            "02_lists_and_loops.py",
            "03_functions_and_dictionaries.py"
        ]

        expected_network = [
            "01_ip_address_validation.py",
            "02_device_inventory.py",
            "03_network_monitoring.py"
        ]

        for filename in expected_basic:
            filepath = self.basic_python_dir / filename
            self.assertTrue(filepath.exists(), f"Missing koan: {filename}")

        for filename in expected_network:
            filepath = self.network_dir / filename
            self.assertTrue(filepath.exists(), f"Missing koan: {filename}")

    def test_koans_have_docstrings(self):
        """Test that all koans have docstrings"""
        all_koans = (
            list(self.basic_python_dir.glob("*.py")) +
            list(self.network_dir.glob("*.py"))
        )

        for koan_file in all_koans:
            with self.subTest(koan=koan_file.name):
                content = koan_file.read_text()
                # Check for docstring at start of file
                self.assertTrue(
                    content.strip().startswith('"""') or content.strip().startswith("'''"),
                    f"{koan_file.name} should have a docstring"
                )

    def test_unsolved_koans_have_placeholders(self):
        """Test that unsolved koans contain __ placeholders"""
        all_koans = (
            list(self.basic_python_dir.glob("*.py")) +
            list(self.network_dir.glob("*.py"))
        )

        for koan_file in all_koans:
            with self.subTest(koan=koan_file.name):
                content = koan_file.read_text()
                # Should contain __ (double underscore) as placeholder
                self.assertIn("__", content, f"{koan_file.name} should have __ placeholders")

    def test_koans_have_assert_statements(self):
        """Test that all koans use assert for testing"""
        all_koans = (
            list(self.basic_python_dir.glob("*.py")) +
            list(self.network_dir.glob("*.py"))
        )

        for koan_file in all_koans:
            with self.subTest(koan=koan_file.name):
                content = koan_file.read_text()
                self.assertIn("assert", content, f"{koan_file.name} should have assert statements")

    def test_koans_have_helpful_messages(self):
        """Test that assert statements have helpful error messages"""
        all_koans = (
            list(self.basic_python_dir.glob("*.py")) +
            list(self.network_dir.glob("*.py"))
        )

        for koan_file in all_koans:
            with self.subTest(koan=koan_file.name):
                content = koan_file.read_text()
                # Find assert statements
                assert_lines = [line for line in content.split('\n') if 'assert' in line and not line.strip().startswith('#')]

                # At least some should have messages
                has_messages = any(',' in line and '"' in line for line in assert_lines)
                self.assertTrue(has_messages, f"{koan_file.name} should have helpful error messages")

    def test_koans_have_completion_message(self):
        """Test that koans have a completion print statement"""
        all_koans = (
            list(self.basic_python_dir.glob("*.py")) +
            list(self.network_dir.glob("*.py"))
        )

        for koan_file in all_koans:
            with self.subTest(koan=koan_file.name):
                content = koan_file.read_text()
                # Should have a print statement indicating completion
                self.assertIn('print("✓', content, f"{koan_file.name} should have completion message")

    def test_koan_naming_convention(self):
        """Test that koans follow naming convention"""
        all_koans = (
            list(self.basic_python_dir.glob("*.py")) +
            list(self.network_dir.glob("*.py"))
        )

        pattern = re.compile(r'^\d{2}_[a-z_]+\.py$')

        for koan_file in all_koans:
            with self.subTest(koan=koan_file.name):
                self.assertTrue(
                    pattern.match(koan_file.name),
                    f"{koan_file.name} doesn't follow naming convention (NN_name.py)"
                )

    def test_koans_are_numbered_sequentially(self):
        """Test that koans in each folder are numbered 01, 02, 03..."""
        for directory in [self.basic_python_dir, self.network_dir]:
            koan_files = sorted(directory.glob("*.py"))
            numbers = [int(f.name[:2]) for f in koan_files]

            with self.subTest(directory=directory.name):
                self.assertEqual(
                    numbers,
                    list(range(1, len(numbers) + 1)),
                    f"Koans in {directory.name} should be numbered sequentially"
                )

    def test_koans_have_difficulty_indicators(self):
        """Test that koans indicate their difficulty level"""
        all_koans = (
            list(self.basic_python_dir.glob("*.py")) +
            list(self.network_dir.glob("*.py"))
        )

        for koan_file in all_koans:
            with self.subTest(koan=koan_file.name):
                content = koan_file.read_text()
                # Check for difficulty indicators in docstring
                has_difficulty = any(
                    keyword in content[:500]  # Check first 500 chars
                    for keyword in ["EASY", "MEDIUM", "HARD", "Easy", "Medium", "Hard"]
                )
                self.assertTrue(
                    has_difficulty,
                    f"{koan_file.name} should indicate difficulty level"
                )

    def test_network_koans_reference_course_goals(self):
        """Test that network automation koans reference course goals"""
        network_koans = list(self.network_dir.glob("*.py"))

        for koan_file in network_koans:
            with self.subTest(koan=koan_file.name):
                content = koan_file.read_text()
                # Should reference course goals (K1-K13, F1-F6, A1)
                has_course_ref = re.search(r'[KFA]\d+:', content) is not None
                self.assertTrue(
                    has_course_ref,
                    f"{koan_file.name} should reference course goals"
                )


class TestProjectStructure(unittest.TestCase):
    """Test overall project structure"""

    def setUp(self):
        self.project_dir = Path(__file__).parent.parent

    def test_required_directories_exist(self):
        """Test that required directories exist"""
        required = ["basic_python", "network_automation", "tests"]

        for dirname in required:
            dir_path = self.project_dir / dirname
            self.assertTrue(dir_path.exists(), f"Missing directory: {dirname}")
            self.assertTrue(dir_path.is_dir(), f"{dirname} should be a directory")

    def test_required_files_exist(self):
        """Test that required files exist"""
        required = [
            "README.md",
            "QUICKSTART.md",
            "OVERVIEW.md",
            "ANSWER_KEY.md",
            "run_koans.py"
        ]

        for filename in required:
            file_path = self.project_dir / filename
            self.assertTrue(file_path.exists(), f"Missing file: {filename}")

    def test_runner_is_executable(self):
        """Test that runner script is executable"""
        runner = self.project_dir / "run_koans.py"
        self.assertTrue(runner.exists(), "run_koans.py should exist")

        # Check if it has shebang
        content = runner.read_text()
        self.assertTrue(
            content.startswith("#!/usr/bin/env python"),
            "run_koans.py should have shebang"
        )


if __name__ == "__main__":
    unittest.main()
