"""
Koan 5: Classes and Objects - Building Your Detective Toolkit (HARD) - SOLVED
=====================================================================

This is the solved version for testing purposes.

🔍 THE INVESTIGATION CONTINUES...

After discovering unauthorized configuration changes, you realize you need better
tools to track evidence. You decide to build a proper evidence management system
using Python classes - just like a real detective's case file system!

You'll create:
- Evidence objects to track findings
- A Suspect class to track potential intruders
- A Case class to organize the entire investigation

In this exercise, you'll learn about:
- Classes and objects
- Instance variables and methods
- __init__ constructors
- Object-oriented programming basics
- Working with multiple objects

Replace the __ (underscores) with the correct values or code.
"""

# 🔍 CONCEPT: Classes are blueprints for creating objects
# Think of a class as a template, and objects as instances created from that template

# 🔍 EVIDENCE #1: Creating your first class

class Evidence:
    """A piece of evidence in our investigation"""

    def __init__(self, evidence_type, description, timestamp):
        self.evidence_type = evidence_type
        self.description = description
        self.timestamp = timestamp
        self.severity = "UNKNOWN"

    def get_summary(self):
        return f"[{self.evidence_type}] {self.description} at {self.timestamp}"


# Create your first piece of evidence
evidence1 = Evidence("LOG", "Unknown command executed", "03:45:12")

assert evidence1.evidence_type == "LOG", "Fix this: what is the evidence type?"
assert evidence1.description == "Unknown command executed", "Fix this: what is the description?"
assert evidence1.timestamp == "03:45:12", "Fix this: what is the timestamp?"
assert evidence1.severity == "UNKNOWN", "Fix this: what is the default severity?"

# Test the method
summary = evidence1.get_summary()
assert "[LOG]" in summary, "Fix this: summary should contain evidence type in brackets"
assert "Unknown command" in summary, "Fix this: summary should contain description"

# 🔍 EVIDENCE #2: Creating multiple evidence objects

evidence2 = Evidence("CONFIG", "Unauthorized VLAN change", "03:42:30")
evidence3 = Evidence("ACCESS", "Login from unknown IP", "03:40:00")

# Create a list of evidence
all_evidence = [evidence1, evidence2, evidence3]
assert len(all_evidence) == 3, "Fix this: how many pieces of evidence?"

# Access the second piece of evidence
assert all_evidence[1].evidence_type == "CONFIG", "Fix this: what type is the second evidence?"
assert all_evidence[2].timestamp == "03:40:00", "Fix this: what is the third evidence timestamp?"

# 🔍 EVIDENCE #3: Adding methods to modify objects

class Evidence:
    """Enhanced evidence class with severity assessment"""

    def __init__(self, evidence_type, description, timestamp):
        self.evidence_type = evidence_type
        self.description = description
        self.timestamp = timestamp
        self.severity = "UNKNOWN"

    def set_severity(self, severity_level):
        """Set the severity level: LOW, MEDIUM, HIGH, CRITICAL"""
        self.severity = severity_level

    def is_critical(self):
        """Check if evidence is critical"""
        return self.severity == "CRITICAL"

    def get_summary(self):
        return f"[{self.severity}] {self.evidence_type}: {self.description}"


# Test the enhanced evidence
evidence = Evidence("ACCESS", "Backdoor account created", "03:41:00")
evidence.set_severity("CRITICAL")

assert evidence.severity == "CRITICAL", "Fix this: what is the severity after setting it?"
assert evidence.is_critical() == True, "Fix this: is this evidence critical?"

# 🔍 SUSPECT TRACKING: Create a Suspect class

class Suspect:
    """Track potential suspects in the investigation"""

    def __init__(self, name, ip_address, last_seen):
        self.name = name
        self.ip_address = ip_address
        self.last_seen = last_seen
        self.suspicion_level = 0  # 0-100 scale
        self.evidence_count = 0

    def add_evidence(self):
        """Increment evidence count and increase suspicion"""
        self.evidence_count += 1
        self.suspicion_level += 20  # Each piece of evidence adds 20 points

    def get_threat_level(self):
        """Determine threat level based on suspicion"""
        if self.suspicion_level >= 80:
            return "CRITICAL"
        elif self.suspicion_level >= 50:
            return "HIGH"
        elif self.suspicion_level >= 30:
            return "MEDIUM"
        else:
            return "LOW"

    def get_profile(self):
        return f"{self.name} ({self.ip_address}) - Threat: {self.get_threat_level()}"


# 🔍 CLUE: Tracking our first suspect
suspect1 = Suspect("Unknown User", "192.168.1.50", "03:45:00")

assert suspect1.name == "Unknown User", "Fix this: what is the suspect's name?"
assert suspect1.suspicion_level == 0, "Fix this: what is the initial suspicion level?"
assert suspect1.get_threat_level() == "LOW", "Fix this: what is the initial threat level?"

# Add evidence against the suspect
suspect1.add_evidence()
assert suspect1.evidence_count == 1, "Fix this: how many pieces of evidence after adding one?"
assert suspect1.suspicion_level == 20, "Fix this: what is suspicion level after one evidence?"

# Add more evidence
suspect1.add_evidence()
suspect1.add_evidence()
assert suspect1.evidence_count == 3, "Fix this: total evidence count?"
assert suspect1.suspicion_level == 60, "Fix this: suspicion level after 3 pieces of evidence?"
assert suspect1.get_threat_level() == "HIGH", "Fix this: what threat level now? (60 suspicion)"

# 🔍 CASE FILE: Create a comprehensive Case class

class Case:
    """Main investigation case that holds all evidence and suspects"""

    def __init__(self, case_id, title):
        self.case_id = case_id
        self.title = title
        self.evidence_list = []
        self.suspects = []
        self.status = "OPEN"

    def add_evidence(self, evidence):
        """Add evidence to the case"""
        self.evidence_list.append(evidence)

    def add_suspect(self, suspect):
        """Add suspect to the case"""
        self.suspects.append(suspect)

    def get_evidence_count(self):
        return len(self.evidence_list)

    def get_critical_evidence(self):
        """Return list of critical evidence"""
        critical = []
        for evidence in self.evidence_list:
            if evidence.is_critical():
                critical.append(evidence)
        return critical

    def get_primary_suspect(self):
        """Get the suspect with highest suspicion level"""
        if not self.suspects:
            return None

        primary = self.suspects[0]
        for suspect in self.suspects:
            if suspect.suspicion_level > primary.suspicion_level:
                primary = suspect
        return primary

    def close_case(self):
        self.status = "CLOSED"


# 🔍 BUILD THE CASE: Put it all together!

# Create the case
network_breach = Case("CASE-2025-001", "Unauthorized Network Access")

assert network_breach.case_id == "CASE-2025-001", "Fix this: what is the case ID?"
assert network_breach.title == "Unauthorized Network Access", "Fix this: what is the case title?"
assert network_breach.status == "OPEN", "Fix this: what is the initial status?"

# Add evidence to the case
ev1 = Evidence("LOG", "Unknown command executed", "03:45:12")
ev1.set_severity("CRITICAL")

ev2 = Evidence("CONFIG", "VLAN 999 created", "03:42:30")
ev2.set_severity("HIGH")

ev3 = Evidence("ACCESS", "Failed login attempts", "03:40:00")
ev3.set_severity("MEDIUM")

network_breach.add_evidence(ev1)
network_breach.add_evidence(ev2)
network_breach.add_evidence(ev3)

assert network_breach.get_evidence_count() == 3, "Fix this: how many pieces of evidence?"

# Get critical evidence
critical = network_breach.get_critical_evidence()
assert len(critical) == 1, "Fix this: how many critical pieces of evidence?"
assert critical[0].evidence_type == "LOG", "Fix this: what type is the critical evidence?"

# Add suspects
suspect_alpha = Suspect("Unknown-Alpha", "192.168.1.50", "03:45:00")
suspect_alpha.add_evidence()
suspect_alpha.add_evidence()
suspect_alpha.add_evidence()

suspect_beta = Suspect("Unknown-Beta", "10.0.0.99", "03:40:00")
suspect_beta.add_evidence()

network_breach.add_suspect(suspect_alpha)
network_breach.add_suspect(suspect_beta)

assert len(network_breach.suspects) == 2, "Fix this: how many suspects?"

# Find the primary suspect
primary = network_breach.get_primary_suspect()
assert primary.name == "Unknown-Alpha", "Fix this: who is the primary suspect? (higher suspicion)"
assert primary.suspicion_level == 60, "Fix this: what is the primary suspect's suspicion level?"

# 🔍 ADVANCED: Class with class methods

class InvestigationReport:
    """Generate investigation reports"""

    def __init__(self, case):
        self.case = case

    def generate_summary(self):
        """Generate a text summary of the case"""
        summary = f"""
╔══════════════════════════════════════╗
║      INVESTIGATION REPORT            ║
╚══════════════════════════════════════╝

Case ID: {self.case.case_id}
Title: {self.case.title}
Status: {self.case.status}

Evidence Collected: {self.case.get_evidence_count()}
Critical Evidence: {len(self.case.get_critical_evidence())}
Suspects: {len(self.case.suspects)}
""".strip()

        if self.case.suspects:
            primary = self.case.get_primary_suspect()
            summary += f"\n\nPrimary Suspect: {primary.get_profile()}"

        return summary


# Generate the report
report = InvestigationReport(network_breach)
report_text = report.generate_summary()

assert "CASE-2025-001" in report_text, "Fix this: report should contain case ID"
assert "Evidence Collected: 3" in report_text, "Fix this: should show 3 pieces of evidence"
assert "Unknown-Alpha" in report_text, "Fix this: should mention primary suspect"

# 🔍 BREAKTHROUGH: You've identified the pattern!

class NetworkDevice:
    """Represents a network device for tracking compromise"""

    def __init__(self, hostname, ip):
        self.hostname = hostname
        self.ip = ip
        self.compromised = False
        self.compromise_time = None

    def mark_compromised(self, timestamp):
        self.compromised = True
        self.compromise_time = timestamp

    def is_compromised(self):
        return self.compromised


# Track compromised devices
devices = [
    NetworkDevice("Switch-01", "10.0.1.1"),
    NetworkDevice("Switch-02", "10.0.1.2"),
    NetworkDevice("Router-01", "10.0.0.1")
]

# Mark devices as compromised
devices[0].mark_compromised("03:42:30")
devices[1].mark_compromised("03:43:15")

assert devices[0].is_compromised() == True, "Fix this: is Switch-01 compromised?"
assert devices[2].is_compromised() == False, "Fix this: is Router-01 compromised?"

# Count compromised devices
compromised_count = sum(1 for d in devices if d.is_compromised())
assert compromised_count == 2, "Fix this: how many devices are compromised?"

print("""
✓ Koan 5 completed!

🔍 INVESTIGATION UPDATE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
You've built a complete evidence tracking system!

Your investigation has revealed:
├─ Primary Suspect: Unknown-Alpha (192.168.1.50)
├─ Threat Level: HIGH
├─ Critical Evidence: Configuration changes and unknown commands
├─ Compromised Devices: 2 switches affected
└─ Timeline: All activity occurred between 03:40-03:45 AM

The suspect accessed your network through an unknown IP address.
But how did they get in? What backdoors did they create?

Continue to the next koan to learn about modules and build
more sophisticated investigation tools!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
