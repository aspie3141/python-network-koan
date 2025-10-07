"""
Network Koan 6: Network Testing and Validation - Securing the Network (HARD) - SOLVED
=============================================================================

This is the solved version for testing purposes.

🔍 FINAL CHAPTER: PREVENTION & VALIDATION

You've cleaned up the backdoors, but how do you ensure your network stays secure?
The answer: Automated testing and continuous validation!

As a network engineer, you need to:
1. Validate that unauthorized changes are removed
2. Test that security policies are enforced
3. Verify network connectivity
4. Create automated security checks
5. Prevent future breaches

This is your final challenge - build a comprehensive security testing suite
that will protect your network from future attacks!

In this exercise, you'll learn about:
- Writing test functions
- Connectivity testing (ping simulation)
- Configuration validation
- Security compliance checking
- Automated security audits
- Continuous monitoring

This koan relates to course goals:
- K13: Redogöra för metoder för att övervaka nätverkskommunikation
- F3: Övervaka nätverksprestanda och hantera incidenter/problem
- F4: Diagnostisera och lösa nätverksrelaterade problem
- F6: Dokumentera nätverksarkitektur och konfigurationer

Replace the __ (underscores) with the correct values or code.
"""

# 🔍 TEST FRAMEWORK: Build your security validation system

class NetworkSecurityTest:
    """Base class for network security tests"""

    def __init__(self, test_name):
        self.test_name = test_name
        self.passed = False
        self.failure_reason = None

    def run(self):
        """Override this method in subclasses"""
        raise NotImplementedError

    def mark_passed(self):
        self.passed = True

    def mark_failed(self, reason):
        self.passed = False
        self.failure_reason = reason

    def get_result(self):
        status = "PASS" if self.passed else "FAIL"
        if self.failure_reason:
            return f"[{status}] {self.test_name}: {self.failure_reason}"
        return f"[{status}] {self.test_name}"


# 🔍 TEST 1: Validate VLAN configuration
class VLANValidationTest(NetworkSecurityTest):
    """Verify only authorized VLANs exist"""

    def __init__(self, device_vlans, authorized_vlans):
        super().__init__("VLAN Configuration Validation")
        self.device_vlans = device_vlans
        self.authorized_vlans = authorized_vlans

    def run(self):
        unauthorized = []
        for vlan in self.device_vlans:
            if vlan not in self.authorized_vlans:
                unauthorized.append(vlan)

        if unauthorized:
            self.mark_failed(f"Unauthorized VLANs found: {unauthorized}")
        else:
            self.mark_passed()


# Test the VLAN validator
authorized_vlans = [1, 10, 20, 30]

# Test with clean config (should pass)
clean_vlans = [1, 10, 20, 30]
test1 = VLANValidationTest(clean_vlans, authorized_vlans)
test1.run()
assert test1.passed == True, "Fix this: should clean config pass?"

# Test with backdoor VLAN (should fail)
compromised_vlans = [1, 10, 20, 30, 999]
test2 = VLANValidationTest(compromised_vlans, authorized_vlans)
test2.run()
assert test2.passed == False, "Fix this: should compromised config pass?"
assert "999" in test2.failure_reason, "Fix this: failure should mention VLAN 999"

# 🔍 TEST 2: Validate user accounts
class UserAccountTest(NetworkSecurityTest):
    """Verify only authorized users exist"""

    def __init__(self, device_users, authorized_users):
        super().__init__("User Account Validation")
        self.device_users = device_users
        self.authorized_users = authorized_users

    def run(self):
        unauthorized = [u for u in self.device_users if u not in self.authorized_users]

        if unauthorized:
            self.mark_failed(f"Unauthorized users: {', '.join(unauthorized)}")
        else:
            self.mark_passed()


authorized_users = ["admin", "operator"]

# Test with backdoor user
current_users = ["admin", "operator", "admin2"]
test3 = UserAccountTest(current_users, authorized_users)
test3.run()

assert test3.passed == False, "Fix this: should test with admin2 pass?"
assert "admin2" in test3.failure_reason, "Fix this: should detect admin2"

# Test after cleanup
cleaned_users = ["admin", "operator"]
test4 = UserAccountTest(cleaned_users, authorized_users)
test4.run()
assert test4.passed == True, "Fix this: should cleaned users pass?"

# 🔍 TEST 3: Password strength validation
class PasswordStrengthTest(NetworkSecurityTest):
    """Verify passwords meet security requirements"""

    def __init__(self, password_list):
        super().__init__("Password Strength Validation")
        self.password_list = password_list

    def is_password_strong(self, password):
        """Check if password meets requirements:
        - At least 8 characters
        - Contains uppercase and lowercase
        - Contains a number
        - Contains special character
        """
        if len(password) < 8:
            return False

        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in "!@#$%^&*" for c in password)

        return has_upper and has_lower and has_digit and has_special

    def run(self):
        weak_passwords = []

        for username, password in self.password_list.items():
            if not self.is_password_strong(password):
                weak_passwords.append(username)

        if weak_passwords:
            self.mark_failed(f"Weak passwords for users: {', '.join(weak_passwords)}")
        else:
            self.mark_passed()


# Test password strength
passwords_weak = {
    "admin": "123456",  # Too short, no special chars
    "operator": "SecureP@ss1"  # Strong
}

test5 = PasswordStrengthTest(passwords_weak)
test5.run()
assert test5.passed == False, "Fix this: should weak passwords pass?"

# Test with all strong passwords
passwords_strong = {
    "admin": "SecureP@ss1",
    "operator": "C0mpl3x!Pwd"
}

test6 = PasswordStrengthTest(passwords_strong)
test6.run()
assert test6.passed == True, "Fix this: should strong passwords pass?"

# 🔍 TEST 4: Connectivity testing (simulated ping)
class ConnectivityTest(NetworkSecurityTest):
    """Test network connectivity"""

    def __init__(self, target_devices):
        super().__init__("Network Connectivity Check")
        self.target_devices = target_devices
        # Simulated reachability
        self.reachable_devices = {
            "Switch-01": True,
            "Switch-02": True,
            "Router-01": True,
            "Switch-03": False  # This one is down
        }

    def run(self):
        unreachable = []

        for device in self.target_devices:
            if not self.reachable_devices.get(device, False):
                unreachable.append(device)

        if unreachable:
            self.mark_failed(f"Unreachable devices: {', '.join(unreachable)}")
        else:
            self.mark_passed()


# Test connectivity
devices_to_check = ["Switch-01", "Switch-02", "Router-01"]
test7 = ConnectivityTest(devices_to_check)
test7.run()
assert test7.passed == True, "Fix this: should all devices be reachable?"

# Test with offline device
devices_with_offline = ["Switch-01", "Switch-02", "Switch-03"]
test8 = ConnectivityTest(devices_with_offline)
test8.run()
assert test8.passed == False, "Fix this: should test pass with offline device?"
assert "Switch-03" in test8.failure_reason, "Fix this: should mention Switch-03"

# 🔍 TEST 5: Security policy compliance
class SecurityPolicyTest(NetworkSecurityTest):
    """Verify security policies are enforced"""

    def __init__(self, device_config):
        super().__init__("Security Policy Compliance")
        self.config = device_config

    def run(self):
        violations = []

        # Check if password encryption is enabled
        if "service password-encryption" not in self.config:
            violations.append("Password encryption not enabled")

        # Check if HTTP server is disabled
        if "no ip http server" not in self.config:
            violations.append("HTTP server not disabled")

        # Check if telnet is disabled on VTY lines
        if "transport input telnet" in self.config:
            violations.append("Telnet is enabled (insecure)")

        # Check for default SNMP communities
        if "snmp-server community public" in self.config:
            violations.append("Default SNMP community 'public' detected")

        if violations:
            self.mark_failed(f"Policy violations: {'; '.join(violations)}")
        else:
            self.mark_passed()


# Test with secure configuration
secure_config = """
service password-encryption
no ip http server
no ip http secure-server
line vty 0 4
 transport input ssh
snmp-server community SecureComm123 RO
"""

test9 = SecurityPolicyTest(secure_config)
test9.run()
assert test9.passed == True, "Fix this: should secure config pass?"

# Test with insecure configuration
insecure_config = """
line vty 0 4
 transport input telnet
snmp-server community public RO
"""

test10 = SecurityPolicyTest(insecure_config)
test10.run()
assert test10.passed == False, "Fix this: should insecure config pass?"
assert "Telnet" in test10.failure_reason, "Fix this: should detect telnet"

# 🔍 TEST 6: Interface security validation
class InterfaceSecurityTest(NetworkSecurityTest):
    """Validate interface security settings"""

    def __init__(self, interfaces):
        super().__init__("Interface Security Validation")
        self.interfaces = interfaces

    def run(self):
        violations = []

        for interface_name, config in self.interfaces.items():
            # Check for suspicious descriptions
            description = config.get("description", "")
            if "backdoor" in description.lower() or "hidden" in description.lower():
                violations.append(f"{interface_name}: Suspicious description")

            # Check for high VLAN numbers (often used for backdoors)
            vlan = config.get("vlan", 0)
            if vlan >= 900:
                violations.append(f"{interface_name}: Suspicious VLAN {vlan}")

            # Check if unused interfaces are shutdown
            if "unused" in description.lower() and config.get("status") != "shutdown":
                violations.append(f"{interface_name}: Unused but not shutdown")

        if violations:
            self.mark_failed(f"Interface violations: {'; '.join(violations)}")
        else:
            self.mark_passed()


# Test with backdoor interface
interfaces_compromised = {
    "GigabitEthernet0/1": {"description": "Uplink", "vlan": 1},
    "GigabitEthernet0/24": {"description": "Backdoor Port", "vlan": 999}
}

test11 = InterfaceSecurityTest(interfaces_compromised)
test11.run()
assert test11.passed == False, "Fix this: should backdoor interface pass?"

# Test with clean interfaces
interfaces_clean = {
    "GigabitEthernet0/1": {"description": "Uplink", "vlan": 1},
    "GigabitEthernet0/2": {"description": "Access Port", "vlan": 10}
}

test12 = InterfaceSecurityTest(interfaces_clean)
test12.run()
assert test12.passed == True, "Fix this: should clean interfaces pass?"

# 🔍 TEST SUITE: Run all tests together
class NetworkSecurityTestSuite:
    """Run multiple security tests"""

    def __init__(self):
        self.tests = []
        self.results = []

    def add_test(self, test):
        """Add a test to the suite"""
        self.tests.append(test)

    def run_all(self):
        """Run all tests and collect results"""
        self.results = []

        for test in self.tests:
            test.run()
            self.results.append({
                "test_name": test.test_name,
                "passed": test.passed,
                "result": test.get_result()
            })

        return self.results

    def get_summary(self):
        """Get test summary"""
        total = len(self.results)
        passed = sum(1 for r in self.results if r["passed"])
        failed = total - passed

        return {
            "total": total,
            "passed": passed,
            "failed": failed,
            "pass_rate": (passed / total * 100) if total > 0 else 0
        }

    def all_passed(self):
        """Check if all tests passed"""
        return all(r["passed"] for r in self.results)


# 🔍 BUILD THE COMPREHENSIVE SECURITY SUITE
suite = NetworkSecurityTestSuite()

# Add all security tests
suite.add_test(VLANValidationTest([1, 10, 20, 30], [1, 10, 20, 30]))
suite.add_test(UserAccountTest(["admin", "operator"], ["admin", "operator"]))
suite.add_test(PasswordStrengthTest({"admin": "SecureP@ss1"}))
suite.add_test(ConnectivityTest(["Switch-01", "Switch-02"]))
suite.add_test(SecurityPolicyTest(secure_config))
suite.add_test(InterfaceSecurityTest(interfaces_clean))

# Run the full suite
results = suite.run_all()

assert len(results) == 6, "Fix this: how many tests in the suite?"

# Get summary
summary = suite.get_summary()
assert summary["total"] == 6, "Fix this: total number of tests?"
assert summary["passed"] == 6, "Fix this: how many tests passed? (all 6)"
assert summary["failed"] == 0, "Fix this: how many tests failed?"
assert summary["pass_rate"] == 100.0, "Fix this: what is the pass rate percentage?"

# All tests should pass
assert suite.all_passed() == True, "Fix this: did all tests pass?"

# 🔍 FINAL CHALLENGE: Detect compromised network
# Run the same suite on a compromised configuration

compromised_suite = NetworkSecurityTestSuite()
compromised_suite.add_test(VLANValidationTest([1, 10, 20, 30, 999], [1, 10, 20, 30]))
compromised_suite.add_test(UserAccountTest(["admin", "admin2"], ["admin"]))
compromised_suite.add_test(SecurityPolicyTest(insecure_config))

compromised_results = compromised_suite.run_all()
compromised_summary = compromised_suite.get_summary()

assert compromised_summary["passed"] == 0, "Fix this: how many passed on compromised? (0)"
assert compromised_summary["failed"] == 3, "Fix this: how many failed on compromised? (3)"
assert compromised_suite.all_passed() == False, "Fix this: did compromised network pass all tests?"

# 🔍 MONITORING: Continuous security validation
class ContinuousSecurityMonitor:
    """Monitor network security continuously"""

    def __init__(self):
        self.scan_history = []
        self.alert_threshold = 1  # Alert if any test fails

    def perform_scan(self, test_suite):
        """Run security scan and record results"""
        results = test_suite.run_all()
        summary = test_suite.get_summary()

        scan_result = {
            "timestamp": "2025-10-07T10:00:00",
            "summary": summary,
            "details": results
        }

        self.scan_history.append(scan_result)
        return scan_result

    def should_alert(self, scan_result):
        """Determine if we should send an alert"""
        failed_count = scan_result["summary"]["failed"]
        return failed_count >= self.alert_threshold

    def get_scan_count(self):
        return len(self.scan_history)


# Set up continuous monitoring
monitor = ContinuousSecurityMonitor()

# Scan 1: Network is secure
scan1 = monitor.perform_scan(suite)
assert monitor.should_alert(scan1) == False, "Fix this: should we alert for secure network?"

# Scan 2: Network is compromised
scan2 = monitor.perform_scan(compromised_suite)
assert monitor.should_alert(scan2) == True, "Fix this: should we alert for compromised network?"

assert monitor.get_scan_count() == 2, "Fix this: how many scans performed?"

# 🔍 GENERATE FINAL SECURITY REPORT
def generate_security_report(test_suite):
    """Generate comprehensive security report"""
    summary = test_suite.get_summary()
    results = test_suite.results

    report = f"""
╔══════════════════════════════════════════════════════════════╗
║           NETWORK SECURITY VALIDATION REPORT                  ║
╚══════════════════════════════════════════════════════════════╝

Test Summary:
  Total Tests: {summary['total']}
  Passed: {summary['passed']}
  Failed: {summary['failed']}
  Pass Rate: {summary['pass_rate']:.1f}%

Overall Status: {'✓ SECURE' if summary['failed'] == 0 else '✗ VULNERABLE'}

Detailed Results:
"""

    for result in results:
        status_icon = "✓" if result["passed"] else "✗"
        report += f"  {status_icon} {result['test_name']}\n"
        if not result["passed"]:
            report += f"    Failure: {result['result']}\n"

    return report.strip()


# Generate report for secure network
secure_report = generate_security_report(suite)
assert "SECURE" in secure_report, "Fix this: report should show SECURE"
assert "Pass Rate: 100.0%" in secure_report, "Fix this: should show 100% pass rate"

# Generate report for compromised network
compromised_report = generate_security_report(compromised_suite)
assert "VULNERABLE" in compromised_report, "Fix this: report should show VULNERABLE"

print("""
✓✓✓ Network Koan 6 completed! ✓✓✓

🎉 CONGRATULATIONS! CASE CLOSED! 🎉
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

You've successfully completed the investigation and secured your network!

┌─ INVESTIGATION SUMMARY ─────────────────────────────────────┐
│                                                              │
│ Case ID: CASE-2025-001                                       │
│ Title: Unauthorized Network Access                           │
│ Status: ✓ CLOSED                                             │
│                                                              │
│ Timeline:                                                    │
│   2025-10-06 23:00 - Normal operations                      │
│   2025-10-07 03:42 - Attack begins                          │
│   2025-10-07 03:47 - Devices go offline                     │
│   2025-10-07 09:00 - Investigation starts (YOU!)            │
│   2025-10-07 11:00 - Backdoors removed                      │
│   2025-10-07 12:00 - Security validated                     │
│                                                              │
└──────────────────────────────────────────────────────────────┘

┌─ WHAT YOU LEARNED ──────────────────────────────────────────┐
│                                                              │
│ ✓ File I/O and log analysis                                 │
│ ✓ Object-oriented programming for evidence tracking         │
│ ✓ Using Python modules for forensic analysis                │
│ ✓ Network configuration management and comparison           │
│ ✓ REST API security and attack vectors                      │
│ ✓ Automated security testing and validation                 │
│                                                              │
└──────────────────────────────────────────────────────────────┘

┌─ SECURITY IMPROVEMENTS IMPLEMENTED ─────────────────────────┐
│                                                              │
│ ✓ Removed VLAN 999 (backdoor network)                       │
│ ✓ Deleted user account: admin2                              │
│ ✓ Removed SNMP community: secret123                         │
│ ✓ Disabled interface Gi0/24                                 │
│ ✓ Enforced strong password policy                           │
│ ✓ Enabled API rate limiting                                 │
│ ✓ Implemented continuous security monitoring                │
│ ✓ Created automated security test suite                     │
│                                                              │
└──────────────────────────────────────────────────────────────┘

┌─ ATTACKER PROFILE ──────────────────────────────────────────┐
│                                                              │
│ IP Address: 192.168.1.50                                     │
│ Attack Duration: 2.7 minutes                                 │
│ Method: Stolen API token + automated script                 │
│ Sophistication: HIGH                                         │
│ Intent: Create persistent backdoor access                   │
│                                                              │
│ Lessons:                                                     │
│ • Rotate API tokens regularly                                │
│ • Enable API rate limiting                                   │
│ • Monitor for unusual API activity                           │
│ • Use multi-factor authentication                            │
│ • Implement least-privilege access                           │
│                                                              │
└──────────────────────────────────────────────────────────────┘

You are now a Network Detective! 🔍

You've mastered:
• Python programming fundamentals
• Network automation with Python
• Security incident response
• Forensic analysis techniques
• Automated testing and validation

Your network is now:
• Monitored continuously
• Validated automatically
• Protected from future attacks
• Documented thoroughly

Well done! You've completed all 9 koans and solved the mystery! 🎊

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
