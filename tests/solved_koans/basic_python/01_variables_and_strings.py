"""
Koan 1: Variables and Strings (EASY) - SOLVED VERSION
====================================

This is the solved version for testing purposes.
"""

# Variables store data
network_device = "Switch"
assert network_device == "Switch", "Fix this: what is the value of network_device?"

# Strings can be combined (concatenation)
device_type = "Cisco"
model = "2960"
full_name = device_type + " " + model
assert full_name == "Cisco 2960", "Fix this: what is device_type + ' ' + model?"

# String methods
ip_address = "192.168.1.1"
assert len(ip_address) == 11, "Fix this: how many characters are in '192.168.1.1'?"

# String formatting
hostname = "SWITCH01"
port = 22
connection_string = f"{hostname}:{port}"
assert connection_string == "SWITCH01:22", "Fix this: what is the value of connection_string?"

# String methods - upper and lower
device_name = "Router"
assert device_name.upper() == "ROUTER", "Fix this: what is 'Router' in uppercase?"
assert device_name.lower() == "router", "Fix this: what is 'Router' in lowercase?"

# String slicing
mac_address = "00:1A:2B:3C:4D:5E"
first_octet = mac_address[0:2]
assert first_octet == "00", "Fix this: what are the first 2 characters?"

print("✓ Koan 1 completed! You understand variables and strings.")
