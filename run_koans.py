#!/usr/bin/env python3
"""
Python Koans Runner
Runs all koan tests and shows progress
"""

import sys
import os
from pathlib import Path

def run_koan(koan_path):
    """Run a single koan and return results"""
    try:
        with open(koan_path, 'r', encoding='utf-8') as f:
            code = f.read()

        # Create a namespace for the koan
        namespace = {}
        exec(code, namespace)

        return True, "✓ Passed"
    except AssertionError as e:
        return False, f"✗ Failed: {str(e)}"
    except Exception as e:
        return False, f"✗ Error: {str(e)}"

def main():
    print("=" * 60)
    print("PYTHON KOANS - Network Technician Edition")
    print("=" * 60)
    print()

    # Find all koan files
    koan_dirs = ['basic_python', 'network_automation']
    all_passed = True

    for koan_dir in koan_dirs:
        dir_path = Path(koan_dir)
        if not dir_path.exists():
            continue

        print(f"\n📁 {koan_dir.replace('_', ' ').title()}")
        print("-" * 60)

        koan_files = sorted(dir_path.glob('*.py'))

        for koan_file in koan_files:
            koan_name = koan_file.stem.replace('_', ' ').title()
            passed, message = run_koan(koan_file)

            if passed:
                print(f"  {message} {koan_name}")
            else:
                print(f"  {message}")
                print(f"  File: {koan_file}")
                all_passed = False
                # Stop at first failure
                print("\n" + "=" * 60)
                print("Fix the failing koan above, then run again!")
                print("=" * 60)
                return 1

    if all_passed:
        print("\n" + "=" * 60)
        print("🎉 CONGRATULATIONS! All koans completed!")
        print("=" * 60)
        return 0

    return 1

if __name__ == "__main__":
    sys.exit(main())
