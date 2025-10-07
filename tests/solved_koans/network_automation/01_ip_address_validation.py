"""
Network Koan 1: IP Address Validation and Manipulation (EASY) - SOLVED VERSION
==============================================================
"""

# IP address components
ip_address = "192.168.1.100"
octets = ip_address.split(".")
assert len(octets) == 4, "Fix this: how many octets in an IPv4 address?"
assert octets[0] == "192", "Fix this: what is the first octet?"
assert octets[3] == "100", "Fix this: what is the last octet?"

# Validate IP address - all octets should be 0-255
def is_valid_octet(octet):
    num = int(octet)
    return 0 <= num <= 255

assert is_valid_octet("192") == True, "Fix this: is 192 a valid octet?"
assert is_valid_octet("300") == False, "Fix this: is 300 a valid octet?"
assert is_valid_octet("0") == True, "Fix this: is 0 a valid octet?"

# Complete IP validation function
def is_valid_ip(ip_string):
    parts = ip_string.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not is_valid_octet(part):
            return False
    return True

assert is_valid_ip("192.168.1.1") == True, "Fix this: is this a valid IP?"
assert is_valid_ip("256.1.1.1") == False, "Fix this: is this a valid IP?"
assert is_valid_ip("10.0.0") == False, "Fix this: is this a valid IP?"

# CIDR notation
cidr = "192.168.1.0/24"
ip_part, prefix = cidr.split("/")
assert ip_part == "192.168.1.0", "Fix this: what is the IP part?"
assert prefix == "24", "Fix this: what is the prefix length?"
assert int(prefix) == 24, "Fix this: what is the prefix as a number?"

# Subnet mask calculation (simplified)
def prefix_to_subnet_mask(prefix_length):
    if prefix_length == 24:
        return "255.255.255.0"
    elif prefix_length == 16:
        return "255.255.0.0"
    elif prefix_length == 8:
        return "255.0.0.0"
    return "Unknown"

assert prefix_to_subnet_mask(24) == "255.255.255.0", "Fix this: what is /24 subnet mask?"
assert prefix_to_subnet_mask(16) == "255.255.0.0", "Fix this: what is /16 subnet mask?"

# Private IP ranges
def is_private_ip(ip):
    first_octet = int(ip.split(".")[0])
    second_octet = int(ip.split(".")[1])

    # 10.0.0.0/8
    if first_octet == 10:
        return True
    # 172.16.0.0/12
    if first_octet == 172 and 16 <= second_octet <= 31:
        return True
    # 192.168.0.0/16
    if first_octet == 192 and second_octet == 168:
        return True
    return False

assert is_private_ip("192.168.1.1") == True, "Fix this: is this a private IP?"
assert is_private_ip("8.8.8.8") == False, "Fix this: is this a private IP?"
assert is_private_ip("10.0.0.1") == True, "Fix this: is this a private IP?"
assert is_private_ip("172.16.0.1") == True, "Fix this: is this a private IP?"

# Generate IP range
def generate_ip_range(base_ip, count):
    """Generate a list of IPs starting from base_ip"""
    parts = base_ip.split(".")
    ips = []
    start = int(parts[3])

    for i in range(count):
        new_ip = f"{parts[0]}.{parts[1]}.{parts[2]}.{start + i}"
        ips.append(new_ip)
    return ips

ip_range = generate_ip_range("192.168.1.10", 5)
assert len(ip_range) == 5, "Fix this: how many IPs generated?"
assert ip_range[0] == "192.168.1.10", "Fix this: what is the first IP?"
assert ip_range[4] == "192.168.1.14", "Fix this: what is the last IP?"

# MAC address validation
def is_valid_mac(mac):
    """Check if MAC address format is valid (XX:XX:XX:XX:XX:XX)"""
    parts = mac.split(":")
    if len(parts) != 6:
        return False
    for part in parts:
        if len(part) != 2:
            return False
    return True

assert is_valid_mac("00:1A:2B:3C:4D:5E") == True, "Fix this: is this a valid MAC?"
assert is_valid_mac("00:1A:2B:3C:4D") == False, "Fix this: is this a valid MAC?"

print("✓ Network Koan 1 completed! You can validate and manipulate IP addresses.")
