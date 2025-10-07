"""
Network Koan 5: API and REST Automation - Tracing the Attack Vector (HARD) - SOLVED
===========================================================================

This is the solved version for testing purposes.

🔍 THE SMOKING GUN: API TRACES

You've discovered what was changed, but HOW did the attacker make these changes
across multiple devices so quickly? The answer: REST APIs!

Modern network devices expose REST APIs for automation. The attacker exploited
this to rapidly compromise your network. By analyzing API logs and simulating
API requests, you can reconstruct exactly how the attack was executed.

In this exercise, you'll learn about:
- REST API concepts (GET, POST, PUT, DELETE)
- JSON data in API requests/responses
- HTTP status codes
- API authentication
- Working with API responses
- Simulating API calls (we'll use mock data, not actual network devices)

This koan relates to course goals:
- K11: Redogöra för Python-script för att kunna automatisera nätverksdrift
- K12: Redogöra för nätverksdrift
- F4: Diagnostisera och lösa nätverksrelaterade problem

Replace the __ (underscores) with the correct values or code.
"""

import json

# 🔍 EVIDENCE: API access logs from your network controller
api_logs = [
    {
        "timestamp": "2025-10-07T03:42:30",
        "method": "POST",
        "endpoint": "/api/vlans",
        "source_ip": "192.168.1.50",
        "status_code": 201,
        "request_body": {"vlan_id": 999, "name": "HIDDEN"}
    },
    {
        "timestamp": "2025-10-07T03:43:15",
        "method": "POST",
        "endpoint": "/api/users",
        "source_ip": "192.168.1.50",
        "status_code": 201,
        "request_body": {"username": "admin2", "privilege": 15, "password": "123456"}
    },
    {
        "timestamp": "2025-10-07T03:44:20",
        "method": "PUT",
        "endpoint": "/api/interfaces/GigabitEthernet0/24",
        "source_ip": "192.168.1.50",
        "status_code": 200,
        "request_body": {"description": "Backdoor Port", "vlan": 999}
    },
    {
        "timestamp": "2025-10-07T03:45:00",
        "method": "POST",
        "endpoint": "/api/snmp",
        "source_ip": "192.168.1.50",
        "status_code": 201,
        "request_body": {"community": "secret123", "access": "RW"}
    }
]

# 🔍 TASK 1: Analyze API log entries
assert len(api_logs) == 4, "Fix this: how many API calls were made?"

# All requests came from the same IP
attacker_ips = [log["source_ip"] for log in api_logs]
unique_ips = set(attacker_ips)
assert len(unique_ips) == 1, "Fix this: how many unique source IPs?"
assert list(unique_ips)[0] == "192.168.1.50", "Fix this: what is the attacker's IP?"

# 🔍 TASK 2: HTTP Status Codes
# 200 = OK (successful)
# 201 = Created (resource created successfully)
# 401 = Unauthorized
# 404 = Not Found
# 500 = Server Error

successful_requests = [log for log in api_logs if log["status_code"] in [200, 201]]
assert len(successful_requests) == 4, "Fix this: how many successful API calls?"

# 🔍 TASK 3: HTTP Methods
# GET = Retrieve data
# POST = Create new resource
# PUT = Update existing resource
# DELETE = Delete resource

post_requests = [log for log in api_logs if log["method"] == "POST"]
assert len(post_requests) == 3, "Fix this: how many POST requests?"

put_requests = [log for log in api_logs if log["method"] == "PUT"]
assert len(put_requests) == 1, "Fix this: how many PUT requests?"

# 🔍 TASK 4: Extract created resources
def extract_created_resources(logs):
    """Get all resources that were created (POST with 201)"""
    created = []
    for log in logs:
        if log["method"] == "POST" and log["status_code"] == 201:
            resource = {
                "endpoint": log["endpoint"],
                "data": log["request_body"]
            }
            created.append(resource)
    return created

created_resources = extract_created_resources(api_logs)
assert len(created_resources) == 3, "Fix this: how many resources were created?"

# Check what was created
vlan_creation = created_resources[0]
assert vlan_creation["data"]["vlan_id"] == 999, "Fix this: what VLAN was created?"

user_creation = created_resources[1]
assert user_creation["data"]["username"] == "admin2", "Fix this: what username was created?"

# 🔍 TASK 5: Simulate API Response
class NetworkDeviceAPI:
    """Simulated network device REST API"""

    def __init__(self, device_name):
        self.device_name = device_name
        self.vlans = {10: "Engineering", 20: "Marketing", 30: "Finance"}
        self.users = {"admin": {"privilege": 15, "password": "Cisco123!"}}
        self.interfaces = {
            "GigabitEthernet0/1": {"description": "Uplink", "vlan": 1},
            "GigabitEthernet0/2": {"description": "Access Port", "vlan": 10}
        }

    def get_vlans(self):
        """GET /api/vlans - Retrieve all VLANs"""
        return {
            "status": 200,
            "data": self.vlans
        }

    def create_vlan(self, vlan_id, name):
        """POST /api/vlans - Create a new VLAN"""
        if vlan_id in self.vlans:
            return {"status": 409, "error": "VLAN already exists"}

        self.vlans[vlan_id] = name
        return {"status": 201, "message": "VLAN created", "data": {"vlan_id": vlan_id, "name": name}}

    def create_user(self, username, privilege, password):
        """POST /api/users - Create a new user"""
        if username in self.users:
            return {"status": 409, "error": "User already exists"}

        self.users[username] = {"privilege": privilege, "password": password}
        return {"status": 201, "message": "User created"}

    def update_interface(self, interface_name, config):
        """PUT /api/interfaces/{name} - Update interface configuration"""
        if interface_name not in self.interfaces:
            # Create the interface if it doesn't exist
            self.interfaces[interface_name] = {}

        self.interfaces[interface_name].update(config)
        return {"status": 200, "message": "Interface updated"}

    def get_interface(self, interface_name):
        """GET /api/interfaces/{name} - Get interface configuration"""
        if interface_name not in self.interfaces:
            return {"status": 404, "error": "Interface not found"}

        return {"status": 200, "data": self.interfaces[interface_name]}


# 🔍 SIMULATE THE ATTACK
device = NetworkDeviceAPI("Switch-01")

# Before attack - check VLANs
vlans_before = device.get_vlans()
assert vlans_before["status"] == 200, "Fix this: what is the status code?"
assert len(vlans_before["data"]) == 3, "Fix this: how many VLANs before attack?"

# Attack Step 1: Create malicious VLAN
response1 = device.create_vlan(999, "HIDDEN")
assert response1["status"] == 201, "Fix this: what status code for creating VLAN?"
assert response1["message"] == "VLAN created", "Fix this: what is the success message?"

# After attack - verify VLAN was added
vlans_after = device.get_vlans()
assert len(vlans_after["data"]) == 4, "Fix this: how many VLANs after creating 999?"
assert 999 in vlans_after["data"], "Fix this: VLAN 999 should now exist"

# Attack Step 2: Create backdoor user
response2 = device.create_user("admin2", 15, "123456")
assert response2["status"] == 201, "Fix this: status code for user creation?"
assert len(device.users) == 2, "Fix this: how many users after creating admin2?"

# Attack Step 3: Configure backdoor interface
response3 = device.update_interface("GigabitEthernet0/24", {
    "description": "Backdoor Port",
    "vlan": 999
})
assert response3["status"] == 200, "Fix this: status code for interface update?"

# Verify the interface configuration
gi024 = device.get_interface("GigabitEthernet0/24")
assert gi024["status"] == 200, "Fix this: status for getting interface?"
assert gi024["data"]["vlan"] == 999, "Fix this: what VLAN is Gi0/24 configured for?"
assert "Backdoor" in gi024["data"]["description"], "Fix this: description should mention backdoor"

# 🔍 TASK 6: API Authentication simulation
class SecureNetworkAPI:
    """Network API with authentication"""

    def __init__(self):
        self.valid_tokens = {
            "token_admin_abc123": {"user": "admin", "role": "admin"},
            "token_operator_xyz789": {"user": "operator", "role": "read-only"}
        }

    def authenticate(self, token):
        """Verify API token"""
        if token in self.valid_tokens:
            return {"authenticated": True, "user_info": self.valid_tokens[token]}
        return {"authenticated": False, "error": "Invalid token"}

    def create_vlan_authenticated(self, token, vlan_id, name):
        """Create VLAN with authentication required"""
        auth = self.authenticate(token)

        if not auth["authenticated"]:
            return {"status": 401, "error": "Unauthorized"}

        if auth["user_info"]["role"] != "admin":
            return {"status": 403, "error": "Forbidden - admin role required"}

        return {"status": 201, "message": f"VLAN {vlan_id} created by {auth['user_info']['user']}"}


secure_api = SecureNetworkAPI()

# Test with valid admin token
response = secure_api.create_vlan_authenticated("token_admin_abc123", 100, "NewVLAN")
assert response["status"] == 201, "Fix this: status code with valid admin token?"

# Test with read-only token (should be forbidden)
response = secure_api.create_vlan_authenticated("token_operator_xyz789", 100, "NewVLAN")
assert response["status"] == 403, "Fix this: status code with read-only token? (403=Forbidden)"

# Test with invalid token
response = secure_api.create_vlan_authenticated("invalid_token", 100, "NewVLAN")
assert response["status"] == 401, "Fix this: status code with invalid token? (401=Unauthorized)"

# 🔍 CLUE: How did the attacker get a valid token?
# You find an API token in the logs!

stolen_token = "token_admin_abc123"  # The attacker stole an admin token!
auth_check = secure_api.authenticate(stolen_token)
assert auth_check["authenticated"] == True, "Fix this: is the stolen token valid?"
assert auth_check["user_info"]["role"] == "admin", "Fix this: what role does the stolen token have?"

# 🔍 TASK 7: Reconstruct the attack sequence
def reconstruct_attack(api_logs):
    """Create a timeline of the attack"""
    timeline = []

    for log in api_logs:
        event = {
            "time": log["timestamp"].split("T")[1],  # Extract time only
            "action": f"{log['method']} {log['endpoint']}",
            "status": "SUCCESS" if log["status_code"] in [200, 201] else "FAILED"
        }
        timeline.append(event)

    return timeline

attack_timeline = reconstruct_attack(api_logs)
assert len(attack_timeline) == 4, "Fix this: how many events in timeline?"
assert attack_timeline[0]["time"] == "03:42:30", "Fix this: what time was the first API call?"
assert "POST /api/vlans" in attack_timeline[0]["action"], "Fix this: first action was creating VLAN"

# All requests succeeded
failed_requests = [t for t in attack_timeline if t["status"] == "FAILED"]
assert len(failed_requests) == 0, "Fix this: how many failed requests? (all succeeded)"

# 🔍 TASK 8: Generate API cleanup script
def generate_api_cleanup_script(api_logs):
    """Generate API calls to undo the attack"""
    cleanup_calls = []

    for log in api_logs:
        if log["method"] == "POST" and "/api/vlans" in log["endpoint"]:
            vlan_id = log["request_body"]["vlan_id"]
            cleanup_calls.append(f"DELETE /api/vlans/{vlan_id}")

        elif log["method"] == "POST" and "/api/users" in log["endpoint"]:
            username = log["request_body"]["username"]
            cleanup_calls.append(f"DELETE /api/users/{username}")

        elif log["method"] == "PUT" and "/api/interfaces" in log["endpoint"]:
            interface = log["endpoint"].split("/")[-1]
            cleanup_calls.append(f"PUT /api/interfaces/{interface} (restore original config)")

        elif log["method"] == "POST" and "/api/snmp" in log["endpoint"]:
            community = log["request_body"]["community"]
            cleanup_calls.append(f"DELETE /api/snmp/{community}")

    return cleanup_calls

cleanup_script = generate_api_cleanup_script(api_logs)
assert len(cleanup_script) == 4, "Fix this: how many cleanup API calls needed?"
assert "DELETE /api/vlans/999" in cleanup_script, "Fix this: should delete VLAN 999"
assert "DELETE /api/users/admin2" in cleanup_script, "Fix this: should delete admin2"

# 🔍 TASK 9: API rate limiting detection
class RateLimitedAPI:
    """API with rate limiting (security feature)"""

    def __init__(self, max_requests_per_minute=10):
        self.max_requests = max_requests_per_minute
        self.request_count = {}

    def make_request(self, client_ip, endpoint):
        """Simulate API request with rate limiting"""
        # Initialize counter for new IPs
        if client_ip not in self.request_count:
            self.request_count[client_ip] = 0

        self.request_count[client_ip] += 1

        # Check rate limit
        if self.request_count[client_ip] > self.max_requests:
            return {"status": 429, "error": "Too Many Requests - Rate limit exceeded"}

        return {"status": 200, "message": "Request successful"}


rate_limited_api = RateLimitedAPI(max_requests_per_minute=3)

# Simulate attacker making rapid requests
results = []
for i in range(5):
    response = rate_limited_api.make_request("192.168.1.50", "/api/vlans")
    results.append(response["status"])

# First 3 requests should succeed
assert results[0] == 200, "Fix this: first request status?"
assert results[1] == 200, "Fix this: second request status?"
assert results[2] == 200, "Fix this: third request status?"

# 4th and 5th should be rate limited
assert results[3] == 429, "Fix this: fourth request status? (429=Too Many Requests)"
assert results[4] == 429, "Fix this: fifth request status?"

# Count how many were blocked
blocked = [r for r in results if r == 429]
assert len(blocked) == 2, "Fix this: how many requests were rate limited?"

# 🔍 TASK 10: The final piece - how was the attack automated?
# The attacker used a Python script!

def automated_attack_script(api_client, auth_token):
    """Reconstructed attack script (DO NOT RUN ON REAL DEVICES!)"""
    results = []

    # Step 1: Create hidden VLAN
    results.append({
        "step": "Create VLAN 999",
        "call": "POST /api/vlans",
        "payload": {"vlan_id": 999, "name": "HIDDEN"}
    })

    # Step 2: Create backdoor user
    results.append({
        "step": "Create backdoor user",
        "call": "POST /api/users",
        "payload": {"username": "admin2", "privilege": 15}
    })

    # Step 3: Configure backdoor interface
    results.append({
        "step": "Configure backdoor interface",
        "call": "PUT /api/interfaces/GigabitEthernet0/24",
        "payload": {"vlan": 999, "description": "Backdoor Port"}
    })

    # Step 4: Add SNMP backdoor
    results.append({
        "step": "Add SNMP backdoor",
        "call": "POST /api/snmp",
        "payload": {"community": "secret123", "access": "RW"}
    })

    return results

# Analyze the attack script
attack_steps = automated_attack_script(None, None)
assert len(attack_steps) == 4, "Fix this: how many steps in the attack script?"

# This matches our API logs!
assert attack_steps[0]["call"] == "POST /api/vlans", "Fix this: what was the first API call?"
assert attack_steps[1]["payload"]["username"] == "admin2", "Fix this: username created in step 2?"

print("""
✓ Network Koan 5 completed!

🔍 ATTACK VECTOR IDENTIFIED!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─ HOW THE ATTACK HAPPENED ─────────────────┐
│ 1. Attacker stole admin API token         │
│ 2. Used automated Python script           │
│ 3. Made 4 API calls in under 3 minutes    │
│ 4. Created multiple backdoors              │
│ 5. No rate limiting was enabled           │
│ 6. All requests succeeded (201/200)       │
└───────────────────────────────────────────┘

┌─ ATTACK TIMELINE ─────────────────────────┐
│ 03:42:30 - POST /api/vlans (VLAN 999)    │
│ 03:43:15 - POST /api/users (admin2)      │
│ 03:44:20 - PUT /api/interfaces/Gi0/24    │
│ 03:45:00 - POST /api/snmp (secret123)    │
└───────────────────────────────────────────┘

┌─ SECURITY LESSONS ────────────────────────┐
│ ✓ Always use API authentication           │
│ ✓ Implement rate limiting                 │
│ ✓ Monitor API access logs                 │
│ ✓ Rotate API tokens regularly             │
│ ✓ Use role-based access control (RBAC)    │
│ ✓ Enable audit logging                    │
└───────────────────────────────────────────┘

You now know EXACTLY how the attack happened!
Time for the final koan - validating that your
network is secure and preventing future attacks!

Continue to Network Koan 6: Network Testing & Validation!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
