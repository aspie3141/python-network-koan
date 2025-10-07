"""
Koan 4: File I/O and Error Handling - The Mystery Begins (MEDIUM) - SOLVED
===========================================================================

This is the solved version for testing purposes.
"""

# 🔍 CLUE #1: Reading the incident report
# Your manager left you a file called 'incident_report.txt'

incident_report = """INCIDENT REPORT - 2025-10-07
=================================
Time: 03:47 AM
Affected: 3 switches, 1 router
Status: All devices offline
Previous night: System updates scheduled
Last seen: 03:45 AM
Notes: Unusual activity detected before offline
"""

# Simulate reading from a file using a string
lines = incident_report.split("\n")
assert len(lines) == 9, "Fix this: how many lines in the report?"

# Find the critical information
time_line = lines[2]  # "Time: 03:47 AM"
assert "03:47" in time_line, "Fix this: should contain the time"

# Extract just the time value
time_value = time_line.split(": ")[1]
assert time_value == "03:47 AM", "Fix this: what is the extracted time?"

# 🔍 CLUE #2: Reading device logs
# You find a log file from one of the switches

device_log = """2025-10-07 03:40:15 - Switch-01 - Normal operation
2025-10-07 03:42:30 - Switch-01 - Configuration change detected
2025-10-07 03:45:12 - Switch-01 - Unknown command executed
2025-10-07 03:47:05 - Switch-01 - Connection lost"""

log_entries = device_log.strip().split("\n")
assert len(log_entries) == 4, "Fix this: how many log entries?"

# Find the suspicious entry
suspicious_line = log_entries[2]
assert "Unknown command" in suspicious_line, "Fix this: third entry should mention unknown command"

# 🔍 CLUE #3: Error handling - some files might be corrupted
# Not all files on the USB drive are readable. You need to handle errors!

def read_log_safely(log_content, line_number):
    """Try to read a specific line, handle errors if line doesn't exist"""
    try:
        lines = log_content.split("\n")
        return lines[line_number]
    except IndexError:
        return "ERROR: Line not found"

# Test with valid line
result = read_log_safely(device_log, 0)
assert "03:40:15" in result, "Fix this: first line should contain this timestamp"

# Test with invalid line (line 100 doesn't exist)
error_result = read_log_safely(device_log, 100)
assert error_result == "ERROR: Line not found", "Fix this: what error message is returned?"

# 🔍 CLUE #4: Parse suspicious commands
# You need to extract all timestamps where something unusual happened

def extract_suspicious_timestamps(log):
    """Find all log entries with 'Configuration change' or 'Unknown command'"""
    suspicious_times = []
    lines = log.strip().split("\n")

    for line in lines:
        if "Configuration change" in line or "Unknown command" in line:
            # Extract timestamp (first 19 characters: "2025-10-07 03:42:30")
            timestamp = line[:19]
            suspicious_times.append(timestamp)

    return suspicious_times

suspicious = extract_suspicious_timestamps(device_log)
assert len(suspicious) == 2, "Fix this: how many suspicious entries?"
assert suspicious[0] == "2025-10-07 03:42:30", "Fix this: what is the first suspicious timestamp?"
assert suspicious[1] == "2025-10-07 03:45:12", "Fix this: what is the second suspicious timestamp?"

# 🔍 CLUE #5: Writing your investigation notes
# Create an investigation report

def generate_investigation_report(device_name, incident_count, severity):
    """Generate a formatted investigation report"""
    report = f"""INVESTIGATION REPORT
Device: {device_name}
Incidents: {incident_count}
Severity: {severity}
Status: Under Investigation
"""
    return report.strip()

my_report = generate_investigation_report("Switch-01", 2, "HIGH")
assert "Switch-01" in my_report, "Fix this: report should contain device name"
assert "Incidents: 2" in my_report, "Fix this: report should show incident count"

# 🔍 CLUE #6: File operations with error handling
# Sometimes files are locked or missing. Always use try/except!

def safe_file_operation(filename, operation="read"):
    """Safely perform file operations"""
    try:
        if operation == "read":
            # Simulating file read
            if filename == "missing.txt":
                raise FileNotFoundError(f"File {filename} not found")
            return "File content here"
        elif operation == "write":
            return "Write successful"
    except FileNotFoundError as e:
        return f"ERROR: {str(e)}"
    except Exception as e:
        return f"ERROR: Unexpected error - {str(e)}"

# Test reading existing file
result = safe_file_operation("device_log.txt", "read")
assert result == "File content here", "Fix this: what is returned for successful read?"

# Test reading missing file
result = safe_file_operation("missing.txt", "read")
assert "ERROR" in result, "Fix this: error message should contain ERROR"
assert "not found" in result, "Fix this: error should mention file not found"

# 🔍 CLUE #7: Analyzing multiple log files
# You have logs from multiple devices. Process them all!

logs_data = {
    "Switch-01.log": "2025-10-07 03:42:30 - Configuration change detected",
    "Switch-02.log": "2025-10-07 03:43:15 - Configuration change detected",
    "Router-01.log": "2025-10-07 03:44:20 - Configuration change detected",
    "Switch-03.log": "2025-10-07 03:45:00 - Normal operation"
}

def count_configuration_changes(logs_dict):
    """Count how many devices had configuration changes"""
    count = 0
    for filename, content in logs_dict.items():
        if "Configuration change detected" in content:
            count += 1
    return count

change_count = count_configuration_changes(logs_data)
assert change_count == 3, "Fix this: how many devices had config changes?"

# 🔍 CLUE #8: Extract evidence - get device names with issues
def get_affected_devices(logs_dict):
    """Return list of device names that had configuration changes"""
    affected = []
    for filename, content in logs_dict.items():
        if "Configuration change detected" in content:
            # Extract device name from filename (remove .log extension)
            device_name = filename.replace(".log", "")
            affected.append(device_name)
    return affected

affected_devices = get_affected_devices(logs_data)
assert len(affected_devices) == 3, "Fix this: how many affected devices?"
assert "Switch-01" in affected_devices, "Fix this: Switch-01 should be in the list"
assert "Switch-03" not in affected_devices, "Fix this: Switch-03 should NOT be in the list"

# 🔍 CLUE #9: Timeline analysis
# Create a timeline of events

def create_timeline(logs_dict):
    """Create a sorted timeline of all events"""
    timeline = []
    for filename, content in logs_dict.items():
        # Extract timestamp (first 19 characters)
        if len(content) >= 19:
            timestamp = content[:19]
            device = filename.replace(".log", "")
            timeline.append({"time": timestamp, "device": device, "log": content})

    # Sort by timestamp
    timeline.sort(key=lambda x: x["time"])
    return timeline

timeline = create_timeline(logs_data)
assert len(timeline) == 4, "Fix this: how many events in timeline?"
assert timeline[0]["device"] == "Switch-01", "Fix this: which device had the first event?"
assert timeline[-1]["device"] == "Switch-03", "Fix this: which device had the last event?"

# 🔍 MYSTERY UPDATE: Pattern discovered!
# All configuration changes happened within 3 minutes
# Someone (or something) is making unauthorized changes to your network!

print("✓ Koan 4 completed!")
print("""

🔍 INVESTIGATION SUMMARY:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
You've discovered:
1. Multiple devices had configuration changes at 3:42-3:45 AM
2. An "Unknown command" was executed on Switch-01
3. All devices went offline shortly after

The mystery deepens... Someone accessed your network in the early morning.
Who was it? What did they change? Continue to the next koan to investigate!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
