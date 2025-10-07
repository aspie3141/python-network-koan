"""
Network Koan 3: Network Monitoring and Log Analysis (HARD)
==========================================================

In this exercise, you'll learn about:
- Parsing network logs
- Analyzing network traffic patterns
- Monitoring network performance
- Generating alerts and reports

This koan relates to course goals:
- K12: Redogöra för nätverksdrift
- K13: Redogöra för metoder för att övervaka nätverkskommunikation
- F3: Övervaka nätverksprestanda och hantera incidenter/problem
- F4: Diagnostisera och lösa nätverksrelaterade problem
"""

from datetime import datetime

# Sample network log entries
network_logs = [
    "2025-10-07 09:15:23 | CORE-SW-01 | INFO | Port Gi0/1 is UP",
    "2025-10-07 09:16:45 | CORE-SW-01 | WARNING | High CPU usage: 85%",
    "2025-10-07 09:17:12 | DIST-SW-01 | ERROR | Port Gi0/5 is DOWN",
    "2025-10-07 09:18:30 | EDGE-RTR-01 | INFO | BGP neighbor 203.0.113.2 established",
    "2025-10-07 09:19:05 | DIST-SW-01 | ERROR | VLAN 100 spanning-tree loop detected",
    "2025-10-07 09:20:15 | CORE-SW-01 | WARNING | Memory usage: 78%",
    "2025-10-07 09:21:40 | FW-01 | ERROR | Unauthorized access attempt from 192.168.1.50",
]

# Parse a log entry
def parse_log_entry(log_line):
    parts = log_line.split(" | ")
    return {
        "timestamp": parts[0],
        "device": parts[1],
        "level": parts[2],
        "message": parts[3]
    }

first_log = parse_log_entry(network_logs[0])
assert first_log["device"] == __, "Fix this: what device generated the first log?"
assert first_log["level"] == __, "Fix this: what is the log level?"
assert first_log["message"] == __, "Fix this: what is the log message?"

# Parse all logs
def parse_all_logs(log_list):
    return [parse_log_entry(log) for log in log_list]

parsed_logs = parse_all_logs(network_logs)
assert len(parsed_logs) == __, "Fix this: how many logs were parsed?"

# Filter logs by severity level
def filter_by_level(logs, level):
    result = []
    for log in logs:
        if log["level"] == level:
            result.append(log)
    return result

errors = filter_by_level(parsed_logs, "ERROR")
assert len(errors) == __, "Fix this: how many ERROR logs?"

warnings = filter_by_level(parsed_logs, "WARNING")
assert len(warnings) == __, "Fix this: how many WARNING logs?"

# Find logs for a specific device
def get_device_logs(logs, device_name):
    return [log for log in logs if log["device"] == device_name]

core_switch_logs = get_device_logs(parsed_logs, "CORE-SW-01")
assert len(core_switch_logs) == __, "Fix this: how many logs from CORE-SW-01?"

# Count logs by device
def count_logs_by_device(logs):
    counts = {}
    for log in logs:
        device = log["device"]
        counts[device] = counts.get(device, 0) + 1
    return counts

device_log_counts = count_logs_by_device(parsed_logs)
assert device_log_counts["DIST-SW-01"] == __, "Fix this: how many logs from DIST-SW-01?"

# Detect critical issues
def detect_critical_issues(logs):
    critical = []
    keywords = ["DOWN", "loop detected", "Unauthorized", "failed"]

    for log in logs:
        for keyword in keywords:
            if keyword in log["message"]:
                critical.append(log)
                break
    return critical

critical_issues = detect_critical_issues(parsed_logs)
assert len(critical_issues) == __, "Fix this: how many critical issues?"

# Network performance metrics
performance_data = [
    {"device": "CORE-SW-01", "timestamp": "09:00", "cpu": 45, "memory": 60, "bandwidth": 250},
    {"device": "CORE-SW-01", "timestamp": "09:15", "cpu": 85, "memory": 78, "bandwidth": 780},
    {"device": "CORE-SW-01", "timestamp": "09:30", "cpu": 42, "memory": 62, "bandwidth": 320},
    {"device": "DIST-SW-01", "timestamp": "09:00", "cpu": 35, "memory": 55, "bandwidth": 180},
    {"device": "DIST-SW-01", "timestamp": "09:15", "cpu": 38, "memory": 57, "bandwidth": 210},
]

# Calculate average CPU usage
def calculate_average_cpu(metrics, device_name):
    device_metrics = [m for m in metrics if m["device"] == device_name]
    if not device_metrics:
        return 0

    total_cpu = sum(m["cpu"] for m in device_metrics)
    return total_cpu / len(device_metrics)

avg_cpu_core = calculate_average_cpu(performance_data, "CORE-SW-01")
assert avg_cpu_core == __, "Fix this: what is average CPU for CORE-SW-01? (57.33...)"

# Find performance anomalies (CPU > 80%)
def find_high_cpu_events(metrics, threshold=80):
    return [m for m in metrics if m["cpu"] > threshold]

high_cpu = find_high_cpu_events(performance_data)
assert len(high_cpu) == __, "Fix this: how many high CPU events?"
assert high_cpu[0]["device"] == __, "Fix this: which device had high CPU?"

# Generate performance alert
def generate_alert(metric):
    if metric["cpu"] > 80:
        severity = "CRITICAL"
    elif metric["cpu"] > 60:
        severity = "WARNING"
    else:
        severity = "INFO"

    return {
        "device": metric["device"],
        "severity": severity,
        "message": f"CPU usage at {metric['cpu']}%",
        "timestamp": metric["timestamp"]
    }

alert = generate_alert(performance_data[1])  # High CPU entry
assert alert["severity"] == __, "Fix this: what is the alert severity?"
assert "85%" in alert["message"], "Fix this: alert message should contain CPU percentage"

# Bandwidth analysis
def calculate_total_bandwidth(metrics):
    return sum(m["bandwidth"] for m in metrics)

total_bw = calculate_total_bandwidth(performance_data)
assert total_bw == __, "Fix this: what is total bandwidth? (1740)"

# Find peak bandwidth usage
def find_peak_bandwidth(metrics):
    if not metrics:
        return None

    peak = metrics[0]
    for metric in metrics:
        if metric["bandwidth"] > peak["bandwidth"]:
            peak = metric
    return peak

peak = find_peak_bandwidth(performance_data)
assert peak["bandwidth"] == __, "Fix this: what is peak bandwidth?"
assert peak["device"] == __, "Fix this: which device had peak bandwidth?"

# Generate monitoring report
def generate_monitoring_report(logs, metrics):
    error_count = len(filter_by_level(logs, "ERROR"))
    warning_count = len(filter_by_level(logs, "WARNING"))
    critical_count = len(detect_critical_issues(logs))

    avg_cpu_all = sum(m["cpu"] for m in metrics) / len(metrics) if metrics else 0

    report = {
        "total_logs": len(logs),
        "errors": error_count,
        "warnings": warning_count,
        "critical_issues": critical_count,
        "average_cpu": round(avg_cpu_all, 2),
        "devices_monitored": len(set(m["device"] for m in metrics))
    }
    return report

report = generate_monitoring_report(parsed_logs, performance_data)
assert report["errors"] == __, "Fix this: how many errors in report?"
assert report["critical_issues"] == __, "Fix this: how many critical issues?"
assert report["devices_monitored"] == __, "Fix this: how many devices monitored?"

# Uptime calculation (in minutes)
def calculate_uptime(start_time, end_time):
    """Calculate uptime in minutes from HH:MM format"""
    start_hour, start_min = map(int, start_time.split(":"))
    end_hour, end_min = map(int, end_time.split(":"))

    start_total = start_hour * 60 + start_min
    end_total = end_hour * 60 + end_min

    return end_total - start_total

uptime = calculate_uptime("09:00", "09:30")
assert uptime == __, "Fix this: how many minutes of uptime?"

# Network health score (0-100)
def calculate_health_score(metrics):
    """
    Health score based on:
    - CPU usage (lower is better)
    - Memory usage (lower is better)
    Weight: 50% CPU, 50% Memory
    """
    if not metrics:
        return 0

    avg_cpu = sum(m["cpu"] for m in metrics) / len(metrics)
    avg_memory = sum(m["memory"] for m in metrics) / len(metrics)

    # Invert percentages (100 - usage = health)
    cpu_health = 100 - avg_cpu
    memory_health = 100 - avg_memory

    health_score = (cpu_health * 0.5) + (memory_health * 0.5)
    return round(health_score, 2)

core_metrics = [m for m in performance_data if m["device"] == "CORE-SW-01"]
health = calculate_health_score(core_metrics)
assert health > 0, "Fix this: health score should be positive"
# The score should be around 36.33 based on avg CPU 57.33 and avg memory 66.67

# Log summary by hour
def summarize_logs_by_hour(logs):
    summary = {}
    for log in logs:
        hour = log["timestamp"].split(":")[0] + ":00"  # Get hour
        if hour not in summary:
            summary[hour] = {"INFO": 0, "WARNING": 0, "ERROR": 0}
        summary[hour][log["level"]] += 1
    return summary

summary = summarize_logs_by_hour(parsed_logs)
assert len(summary) == __, "Fix this: how many hours in summary?"
# All logs are from 09:xx so should be 1 hour
assert "2025-10-07 09:00" in summary, "Fix this: summary should have the hour key"

print("✓ Network Koan 3 completed! You can monitor and analyze network performance.")
