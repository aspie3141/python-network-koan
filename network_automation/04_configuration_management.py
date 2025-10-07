"""
Network Koan 4: Configuration Management - Finding the Backdoor (MEDIUM-HARD)
==============================================================================

🔍 DEEP DIVE: CONFIGURATION FORENSICS

Armed with your investigation tools, you now need to examine the actual network
device configurations. You have backups from before the attack and current configs
from after. By comparing them, you can find exactly what the attacker changed!

The attacker was clever - they made subtle changes designed to be hidden.
Can you spot all the unauthorized modifications?

In this exercise, you'll learn about:
- Network device configuration parsing
- Configuration comparison (diff)
- VLAN management
- Access control lists (ACL)
- Configuration templates
- Configuration backup and restore

This koan relates to course goals:
- F6: Dokumentera nätverksarkitektur och konfigurationer
- K11: Redogöra för Python-script för att kunna automatisera nätverksdrift
- F3: Övervaka nätverksprestanda och hantera incidenter/problem

Replace the __ (underscores) with the correct values or code.
"""

# 🔍 EVIDENCE: Original configuration backup (before attack)
original_config = """hostname Switch-01
!
vlan 10
 name Engineering
!
vlan 20
 name Marketing
!
vlan 30
 name Finance
!
interface GigabitEthernet0/1
 description Uplink to Core
 switchport mode trunk
!
interface GigabitEthernet0/2
 description User Access Port
 switchport access vlan 10
!
snmp-server community public RO
snmp-server community private RW
!
username admin privilege 15 secret Cisco123!
!
line vty 0 4
 login local
 transport input ssh
!
end"""

# 🔍 EVIDENCE: Current configuration (after attack)
current_config = """hostname Switch-01
!
vlan 10
 name Engineering
!
vlan 20
 name Marketing
!
vlan 30
 name Finance
!
vlan 999
 name HIDDEN
!
interface GigabitEthernet0/1
 description Uplink to Core
 switchport mode trunk
!
interface GigabitEthernet0/2
 description User Access Port
 switchport access vlan 10
!
interface GigabitEthernet0/24
 description Backdoor Port
 switchport access vlan 999
 switchport mode access
!
snmp-server community public RO
snmp-server community private RW
snmp-server community secret123 RW
!
username admin privilege 15 secret Cisco123!
username admin2 privilege 15 secret 123456
!
line vty 0 4
 login local
 transport input ssh
!
line vty 5 15
 login local
 transport input telnet
 no password required
!
end"""

# 🔍 TASK 1: Parse configuration into lines
def parse_config(config_text):
    """Split configuration into lines, remove empty lines"""
    lines = config_text.strip().split("\n")
    return [line for line in lines if line.strip()]

original_lines = parse_config(original_config)
current_lines = parse_config(current_config)

assert len(original_lines) == __, "Fix this: how many non-empty lines in original?"
assert len(current_lines) == __, "Fix this: how many non-empty lines in current?"

# 🔍 CLUE: Current config has MORE lines (attacker added things!)
lines_added = len(current_lines) - len(original_lines)
assert lines_added == __, "Fix this: how many lines were added?"

# 🔍 TASK 2: Find lines that exist in current but not in original
def find_added_lines(original, current):
    """Find lines that were added"""
    original_set = set(original)
    current_set = set(current)
    added = current_set - original_set
    return sorted(list(added))

added_lines = find_added_lines(original_lines, current_lines)
assert len(added_lines) == __, "Fix this: how many unique lines were added?"

# Check for suspicious additions
assert "vlan 999" in added_lines, "Fix this: VLAN 999 should be in added lines"
assert "username admin2 privilege 15 secret 123456" in added_lines, "Fix this: backdoor user should be detected"

# 🔍 TASK 3: Extract VLANs from configuration
def extract_vlans(config_lines):
    """Extract all VLAN numbers from config"""
    vlans = []
    for line in config_lines:
        line = line.strip()
        if line.startswith("vlan ") and line.split()[1].isdigit():
            vlan_number = int(line.split()[1])
            vlans.append(vlan_number)
    return vlans

original_vlans = extract_vlans(original_lines)
current_vlans = extract_vlans(current_lines)

assert len(original_vlans) == __, "Fix this: how many VLANs in original?"
assert len(current_vlans) == __, "Fix this: how many VLANs in current?"

# Find the rogue VLAN
rogue_vlan = [v for v in current_vlans if v not in original_vlans]
assert len(rogue_vlan) == __, "Fix this: how many unauthorized VLANs?"
assert rogue_vlan[0] == __, "Fix this: what is the unauthorized VLAN number?"

# 🔍 TASK 4: Extract usernames
def extract_usernames(config_lines):
    """Extract all configured usernames"""
    usernames = []
    for line in config_lines:
        line = line.strip()
        if line.startswith("username "):
            parts = line.split()
            username = parts[1]
            usernames.append(username)
    return usernames

original_users = extract_usernames(original_lines)
current_users = extract_usernames(current_lines)

assert len(original_users) == __, "Fix this: how many users in original?"
assert len(current_users) == __, "Fix this: how many users in current?"

# Find backdoor account
backdoor_users = [u for u in current_users if u not in original_users]
assert len(backdoor_users) == __, "Fix this: how many unauthorized users?"
assert backdoor_users[0] == __, "Fix this: what is the backdoor username?"

# 🔍 TASK 5: Extract SNMP communities (passwords for network management)
def extract_snmp_communities(config_lines):
    """Extract SNMP community strings"""
    communities = []
    for line in config_lines:
        line = line.strip()
        if "snmp-server community" in line:
            parts = line.split()
            if len(parts) >= 3:
                community_string = parts[2]
                communities.append(community_string)
    return communities

original_snmp = extract_snmp_communities(original_lines)
current_snmp = extract_snmp_communities(current_lines)

assert len(original_snmp) == __, "Fix this: how many SNMP communities originally?"
assert len(current_snmp) == __, "Fix this: how many SNMP communities now?"

# Find added SNMP community (backdoor access!)
added_snmp = [c for c in current_snmp if c not in original_snmp]
assert len(added_snmp) == __, "Fix this: how many unauthorized SNMP communities?"
assert added_snmp[0] == __, "Fix this: what is the backdoor SNMP community string?"

# 🔍 TASK 6: Parse interface configurations
def extract_interface_config(config_lines, interface_name):
    """Extract configuration for a specific interface"""
    in_interface = False
    interface_config = []

    for line in config_lines:
        stripped = line.strip()

        # Start of interface section
        if stripped.startswith("interface " + interface_name):
            in_interface = True
            interface_config.append(stripped)
            continue

        # End of interface section (next interface or !)
        if in_interface and (stripped.startswith("interface ") or stripped == "!"):
            break

        if in_interface:
            interface_config.append(stripped)

    return interface_config

# Check the suspicious interface Gi0/24
gi024_config = extract_interface_config(current_lines, "GigabitEthernet0/24")

assert len(gi024_config) > 0, "Fix this: should find config for Gi0/24"
assert "description Backdoor Port" in gi024_config, "Fix this: suspicious description"

# Check if this interface exists in original
gi024_original = extract_interface_config(original_lines, "GigabitEthernet0/24")
assert len(gi024_original) == __, "Fix this: was Gi0/24 in original config? (0 means no)"

# 🔍 TASK 7: Generate a security report
class ConfigSecurityAnalyzer:
    """Analyze configuration for security issues"""

    def __init__(self, original_config, current_config):
        self.original = parse_config(original_config)
        self.current = parse_config(current_config)
        self.findings = []

    def analyze_vlans(self):
        """Check for unauthorized VLANs"""
        orig_vlans = extract_vlans(self.original)
        curr_vlans = extract_vlans(self.current)
        unauthorized = [v for v in curr_vlans if v not in orig_vlans]

        if unauthorized:
            for vlan in unauthorized:
                self.findings.append({
                    "type": "UNAUTHORIZED_VLAN",
                    "severity": "HIGH",
                    "detail": f"VLAN {vlan} was not in original configuration"
                })

        return len(unauthorized)

    def analyze_users(self):
        """Check for unauthorized user accounts"""
        orig_users = extract_usernames(self.original)
        curr_users = extract_usernames(self.current)
        unauthorized = [u for u in curr_users if u not in orig_users]

        if unauthorized:
            for user in unauthorized:
                self.findings.append({
                    "type": "UNAUTHORIZED_USER",
                    "severity": "CRITICAL",
                    "detail": f"User account '{user}' was not in original configuration"
                })

        return len(unauthorized)

    def analyze_snmp(self):
        """Check for unauthorized SNMP communities"""
        orig_snmp = extract_snmp_communities(self.original)
        curr_snmp = extract_snmp_communities(self.current)
        unauthorized = [c for c in curr_snmp if c not in orig_snmp]

        if unauthorized:
            for community in unauthorized:
                self.findings.append({
                    "type": "UNAUTHORIZED_SNMP",
                    "severity": "HIGH",
                    "detail": f"SNMP community '{community}' was not in original configuration"
                })

        return len(unauthorized)

    def get_critical_findings(self):
        """Get all critical severity findings"""
        return [f for f in self.findings if f["severity"] == "CRITICAL"]

    def get_finding_count(self):
        return len(self.findings)


# 🔍 RUN THE ANALYSIS
analyzer = ConfigSecurityAnalyzer(original_config, current_config)

unauthorized_vlans = analyzer.analyze_vlans()
assert unauthorized_vlans == __, "Fix this: how many unauthorized VLANs found?"

unauthorized_users = analyzer.analyze_users()
assert unauthorized_users == __, "Fix this: how many unauthorized users found?"

unauthorized_snmp = analyzer.analyze_snmp()
assert unauthorized_snmp == __, "Fix this: how many unauthorized SNMP communities?"

# Check findings
total_findings = analyzer.get_finding_count()
assert total_findings == __, "Fix this: total security findings? (3 total)"

critical_findings = analyzer.get_critical_findings()
assert len(critical_findings) == __, "Fix this: how many CRITICAL findings?"
assert critical_findings[0]["type"] == __, "Fix this: what type is the critical finding?"

# 🔍 TASK 8: Generate remediation script
def generate_remediation_script(findings):
    """Generate commands to remove unauthorized changes"""
    commands = ["! Remediation Script - Remove Unauthorized Changes"]

    for finding in findings:
        if finding["type"] == "UNAUTHORIZED_VLAN":
            # Extract VLAN number from detail
            vlan = finding["detail"].split()[1]
            commands.append(f"no vlan {vlan}")

        elif finding["type"] == "UNAUTHORIZED_USER":
            # Extract username from detail
            username = finding["detail"].split("'")[1]
            commands.append(f"no username {username}")

        elif finding["type"] == "UNAUTHORIZED_SNMP":
            # Extract community from detail
            community = finding["detail"].split("'")[1]
            commands.append(f"no snmp-server community {community}")

    return commands

remediation = generate_remediation_script(analyzer.findings)

assert len(remediation) > 3, "Fix this: should have header + 3 removal commands"
assert "no vlan 999" in remediation, "Fix this: should remove VLAN 999"
assert "no username admin2" in remediation, "Fix this: should remove admin2"
assert "no snmp-server community secret123" in remediation, "Fix this: should remove secret123"

# 🔍 TASK 9: Configuration template generation
def generate_secure_config_template(hostname, vlans, users):
    """Generate a secure baseline configuration"""
    config_lines = [
        f"hostname {hostname}",
        "!",
        "! VLANs"
    ]

    for vlan_id, vlan_name in vlans.items():
        config_lines.append(f"vlan {vlan_id}")
        config_lines.append(f" name {vlan_name}")
        config_lines.append("!")

    config_lines.append("! User Accounts")
    for username, password in users.items():
        config_lines.append(f"username {username} privilege 15 secret {password}")

    config_lines.append("!")
    config_lines.append("! Security Hardening")
    config_lines.append("no ip http server")
    config_lines.append("no ip http secure-server")
    config_lines.append("service password-encryption")
    config_lines.append("!")
    config_lines.append("end")

    return "\n".join(config_lines)

# Generate secure baseline
secure_vlans = {10: "Engineering", 20: "Marketing", 30: "Finance"}
secure_users = {"admin": "SecureP@ssw0rd!"}

secure_config = generate_secure_config_template("Switch-01", secure_vlans, secure_users)

assert "hostname Switch-01" in secure_config, "Fix this: should have hostname"
assert "vlan 10" in secure_config, "Fix this: should have VLAN 10"
assert "vlan 999" not in secure_config, "Fix this: should NOT have VLAN 999"
assert "service password-encryption" in secure_config, "Fix this: should have security hardening"

# 🔍 TASK 10: Configuration versioning
from datetime import datetime

class ConfigVersion:
    """Track configuration versions"""

    def __init__(self, version_number, config_text, timestamp=None):
        self.version = version_number
        self.config = config_text
        self.timestamp = timestamp or datetime.now().isoformat()
        self.line_count = len(parse_config(config_text))

    def get_summary(self):
        return {
            "version": self.version,
            "timestamp": self.timestamp,
            "line_count": self.line_count
        }


# Create version history
v1 = ConfigVersion(1, original_config, "2025-10-06T23:00:00")
v2 = ConfigVersion(2, current_config, "2025-10-07T03:45:00")

assert v1.version == __, "Fix this: what is v1 version number?"
assert v1.line_count < v2.line_count, "Fix this: v2 should have more lines than v1"

# Calculate changes
config_growth = v2.line_count - v1.line_count
assert config_growth == __, "Fix this: how many lines added in v2?"

print("✓ Network Koan 4 completed!")
print("""

🔍 CONFIGURATION FORENSICS COMPLETE!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─ UNAUTHORIZED CHANGES DETECTED ───────────┐
│ ✗ VLAN 999 (HIDDEN) - Backdoor network   │
│ ✗ User: admin2 / Password: 123456        │
│ ✗ SNMP Community: secret123               │
│ ✗ Interface Gi0/24 - Backdoor port       │
│ ✗ VTY lines 5-15 - Telnet without auth   │
└───────────────────────────────────────────┘

┌─ REMEDIATION PLAN ────────────────────────┐
│ 1. Remove VLAN 999                        │
│ 2. Delete user account admin2             │
│ 3. Remove SNMP community secret123        │
│ 4. Shutdown interface Gi0/24             │
│ 5. Remove VTY lines 5-15                  │
│ 6. Change all passwords                   │
│ 7. Enable logging and monitoring          │
└───────────────────────────────────────────┘

The attacker created multiple backdoors into your network!
But how did they automate these changes across multiple devices?
They must have used APIs...

Continue to Network Koan 5: API and REST Automation!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
