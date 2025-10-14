"""
Koan 6: Modules and Imports - Advanced Investigation Tools (MEDIUM-HARD)
=========================================================================

🔍 THE PLOT THICKENS...

You've collected evidence and tracked suspects. Now you need to use Python's
powerful built-in modules to dig deeper. The suspect's IP address (192.168.1.50)
keeps appearing in logs. You need to analyze timestamps, calculate time windows,
and use specialized tools to crack this case!

In this exercise, you'll learn about:
- Importing built-in modules
- Working with datetime for time analysis
- Using json for structured data
- Using re (regular expressions) for pattern matching
- Creating your own utility functions
- The hashlib module for cryptographic analysis

Replace the __ (underscores) with the correct values or code.
"""

# 🔍 TOOL #1: DateTime module for timeline analysis
from datetime import datetime, timedelta

# Parse timestamps from logs
timestamp1 = "2025-10-07 03:42:30"
timestamp2 = "2025-10-07 03:45:12"

# Convert strings to datetime objects
dt1 = datetime.strptime(timestamp1, "%Y-%m-%d %H:%M:%S")
dt2 = datetime.strptime(timestamp2, "%Y-%m-%d %H:%M:%S")

assert dt1.hour == 3, "Fix this: what hour was the first event?"
assert dt1.minute == 42, "Fix this: what minute was the first event?"

# Calculate time difference - How fast did the attack happen?
time_diff = dt2 - dt1
seconds_elapsed = time_diff.total_seconds()

assert seconds_elapsed == 162, "Fix this: how many seconds between events? (162)"

# 🔍 CLUE: The attack window was very short!
minutes_elapsed = seconds_elapsed / 60
assert minutes_elapsed < 3, "Fix this: attack happened in less than 3 minutes"

# 🔍 TOOL #2: JSON module for structured evidence data
import json

# Evidence stored in JSON format (common for network device configs)
evidence_json = """
{
    "case_id": "CASE-2025-001",
    "compromised_devices": [
        {"hostname": "Switch-01", "ip": "10.0.1.1", "vlan": 999},
        {"hostname": "Switch-02", "ip": "10.0.1.2", "vlan": 999}
    ],
    "attacker_ip": "192.168.1.50",
    "unauthorized_changes": [
        "VLAN 999 created",
        "Backdoor account: admin2",
        "SNMP community changed"
    ]
}
"""

# Parse JSON data
evidence_data = json.loads(evidence_json)

assert evidence_data["case_id"] == "CASE-2025-001", "Fix this: what is the case ID?"
assert evidence_data["attacker_ip"] == "192.168.1.50", "Fix this: what is the attacker's IP?"

# Access nested data
compromised = evidence_data["compromised_devices"]
assert len(compromised) == 2, "Fix this: how many compromised devices?"
assert compromised[0]["vlan"] == 999, "Fix this: what VLAN was created?"

# Access list of changes
changes = evidence_data["unauthorized_changes"]
assert len(changes) == 3, "Fix this: how many unauthorized changes?"
assert "admin2" in changes[1], "Fix this: second change should mention admin2"

# 🔍 TOOL #3: Convert Python data to JSON (for reports)
investigation_report = {
    "timestamp": "2025-10-07 09:00:00",
    "investigator": "You",
    "findings": {
        "threat_level": "CRITICAL",
        "suspects": 1,
        "evidence_count": 5
    }
}

# Convert to JSON string
json_output = json.dumps(investigation_report, indent=2)
assert "CRITICAL" in json_output, "Fix this: JSON should contain threat level"
assert "evidence_count" in json_output, "Fix this: JSON should have evidence count"

# Parse it back
parsed_report = json.loads(json_output)
assert parsed_report["findings"]["suspects"] == 1, "Fix this: how many suspects in report?"

# 🔍 TOOL #4: Regular expressions for pattern matching
import re

# Search through raw log data for IP addresses
raw_log = """
2025-10-07 03:42:30 Connection from 192.168.1.50
2025-10-07 03:43:15 Connection from 192.168.1.50
2025-10-07 03:45:00 Connection from 10.0.0.99
2025-10-07 03:45:12 Connection from 192.168.1.50
"""

# Find all IP addresses in the log
ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
ip_addresses = re.findall(ip_pattern, raw_log)

assert len(ip_addresses) == 4, "Fix this: how many IP addresses found?"
assert "192.168.1.50" in ip_addresses, "Fix this: should contain suspect IP"

# Count occurrences of the suspect IP
suspect_ip = "192.168.1.50"
suspect_count = ip_addresses.count(suspect_ip)
assert suspect_count == 3, "Fix this: how many times does suspect IP appear?"

# 🔍 TOOL #5: Search for specific patterns
# Check if logs contain backdoor indicators

backdoor_indicators = ["admin2", "user_backdoor", "hidden_account"]

def check_for_backdoors(log_text, indicators):
    """Search for backdoor indicators in logs"""
    found_indicators = []
    for indicator in indicators:
        if re.search(indicator, log_text):
            found_indicators.append(indicator)
    return found_indicators

suspicious_log = "User admin2 logged in successfully. VLAN 999 configured."
found = check_for_backdoors(suspicious_log, backdoor_indicators)

assert len(found) == 1, "Fix this: how many backdoor indicators found?"
assert "admin2" in found, "Fix this: admin2 should be detected"

# 🔍 TOOL #6: Hashlib for password analysis
import hashlib

# You found a suspicious hash in the configuration backup
# The attacker might have changed passwords

def calculate_md5(text):
    """Calculate MD5 hash of text"""
    return hashlib.md5(text.encode()).hexdigest()

# Original password hash (from backup)
original_password = "cisco123"
original_hash = calculate_md5(original_password)

# Current password hash (from compromised device)
current_hash = "e10adc3949ba59abbe56e057f20f883e"

# Check if password was changed
password_changed = (original_hash != current_hash)
assert password_changed == True, "Fix this: was the password changed?"

# 🔍 CLUE: Try to find what the new password is
# Common passwords to test
common_passwords = ["password", "admin", "123456", "password123"]

def find_password_match(target_hash, password_list):
    """Try to find which password matches the hash"""
    for pwd in password_list:
        if calculate_md5(pwd) == target_hash:
            return pwd
    return None

# The hash e10adc3949ba59abbe56e057f20f883e is MD5 of "123456"
cracked_password = find_password_match(current_hash, common_passwords)
assert cracked_password == "123456", "Fix this: what is the attacker's password? (hint: very common)"

# 🔍 TOOL #7: Collections module for advanced data structures
from collections import Counter

# Analyze which devices were accessed most frequently
access_log = [
    "Switch-01", "Switch-01", "Switch-02", "Router-01",
    "Switch-01", "Switch-02", "Switch-01", "Switch-03"
]

# Count accesses
access_counts = Counter(access_log)
assert access_counts["Switch-01"] == 4, "Fix this: how many times was Switch-01 accessed?"

# Find most commonly accessed device
most_common = access_counts.most_common(1)
most_accessed_device = most_common[0][0]
assert most_accessed_device == "Switch-01", "Fix this: which device was accessed most?"

# 🔍 TOOL #8: Random module (simulate forensic data generation)
import random

# Generate unique case evidence IDs
random.seed(42)  # Fixed seed for consistent results

def generate_evidence_id():
    """Generate unique evidence ID"""
    return f"EV-{random.randint(1000, 9999)}"

# With seed 42, first random int between 1000-9999 is deterministic
evidence_id = generate_evidence_id()
assert "EV-" in evidence_id, "Fix this: ID should start with EV-"
assert len(evidence_id) == 7, "Fix this: ID should be 7 characters (EV-XXXX)"

# 🔍 TOOL #9: Os and sys modules for system information
import os
import sys

# Get Python version info
python_version = sys.version_info
assert python_version.major >= 3, "Fix this: should be using Python 3+"

# 🔍 TOOL #10: Putting it all together - Complete analysis

class ForensicAnalyzer:
    """Advanced forensic analysis tool using multiple modules"""

    def __init__(self):
        self.evidence = []
        self.timeline = []

    def analyze_log_entry(self, log_line):
        """Parse and analyze a log entry"""
        # Extract timestamp
        timestamp_match = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', log_line)
        if timestamp_match:
            timestamp = timestamp_match.group()
            dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")

            # Extract IP addresses
            ips = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', log_line)

            analysis = {
                "timestamp": timestamp,
                "hour": dt.hour,
                "minute": dt.minute,
                "ip_addresses": ips,
                "raw_log": log_line
            }

            self.timeline.append(analysis)
            return analysis
        return None

    def get_timeline_summary(self):
        """Get summary of timeline"""
        if not self.timeline:
            return {"total_events": 0}

        hours = [entry["hour"] for entry in self.timeline]
        ip_list = []
        for entry in self.timeline:
            ip_list.extend(entry["ip_addresses"])

        return {
            "total_events": len(self.timeline),
            "unique_ips": len(set(ip_list)),
            "hours_covered": len(set(hours))
        }


# 🔍 FINAL ANALYSIS: Use the forensic analyzer

analyzer = ForensicAnalyzer()

# Analyze multiple log entries
logs = [
    "2025-10-07 03:42:30 Connection from 192.168.1.50",
    "2025-10-07 03:43:15 Connection from 192.168.1.50",
    "2025-10-07 04:00:00 Connection from 10.0.0.99"
]

for log in logs:
    analyzer.analyze_log_entry(log)

assert len(analyzer.timeline) == 3, "Fix this: how many entries analyzed?"

# Get first entry
first_entry = analyzer.timeline[0]
assert first_entry["hour"] == 3, "Fix this: what hour was the first entry?"
assert len(first_entry["ip_addresses"]) == 1, "Fix this: how many IPs in first entry?"

# Get summary
summary = analyzer.get_timeline_summary()
assert summary["total_events"] == 3, "Fix this: how many total events?"
assert summary["unique_ips"] == 2, "Fix this: how many unique IPs? (2 unique IPs)"
assert summary["hours_covered"] == 2, "Fix this: how many hours covered? (3 AM and 4 AM)"

# 🔍 BREAKTHROUGH: Calculate attack timeframe
first_timestamp = datetime.strptime("2025-10-07 03:42:30", "%Y-%m-%d %H:%M:%S")
last_timestamp = datetime.strptime("2025-10-07 03:45:12", "%Y-%m-%d %H:%M:%S")
attack_duration = (last_timestamp - first_timestamp).total_seconds()

assert attack_duration == 162, "Fix this: how long did the attack last in seconds?"

# Add 24 hours to timestamp (for when you discovered the breach)
discovery_time = first_timestamp + timedelta(hours=24)
assert discovery_time.day == 8, "Fix this: what day did you discover the breach? (next day)"

print("✓ Koan 6 completed!")
print("""

🔍 MAJOR BREAKTHROUGH!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Your forensic analysis has revealed:

┌─ ATTACK TIMELINE ─────────────────────────┐
│ Start: 2025-10-07 03:42:30                │
│ End: 2025-10-07 03:45:12                  │
│ Duration: 162 seconds (2.7 minutes)       │
│ Discovery: 24 hours later                 │
└───────────────────────────────────────────┘

┌─ ATTACKER PROFILE ────────────────────────┐
│ IP Address: 192.168.1.50                  │
│ Access Count: 3 times                     │
│ Primary Target: Switch-01                 │
│ Password Used: 123456 (weak!)            │
└───────────────────────────────────────────┘

┌─ UNAUTHORIZED CHANGES ────────────────────┐
│ ✗ Created VLAN 999                        │
│ ✗ Added backdoor account: admin2          │
│ ✗ Changed SNMP community strings          │
│ ✗ Modified device passwords               │
└───────────────────────────────────────────┘

You now have the tools and evidence! Time to investigate
the actual network configurations to find what they changed.

Continue to Network Koan 4: Configuration Management!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
