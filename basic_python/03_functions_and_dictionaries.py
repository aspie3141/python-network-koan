"""
Koan 3: Functions and Dictionaries (HARD)
==========================================

In this exercise, you'll learn about:
- Functions (reusable code blocks)
- Dictionaries (key-value pairs)
- Return values
- Working with complex data structures

Replace the __ (underscores) with the correct values or code.
"""

# Functions - basic
def get_device_type():
    return "Router"

result = get_device_type()
assert result == __, "Fix this: what does the function return?"

# Functions with parameters
def create_hostname(prefix, number):
    return f"{prefix}{number:02d}"

hostname = create_hostname("SW", 5)
assert hostname == __, "Fix this: what hostname is created? (hint: :02d means 2 digits with leading zero)"

# Functions with default parameters
def configure_port(port_number, status="enabled"):
    return f"Port {port_number} is {status}"

assert configure_port(1) == __, "Fix this: what is returned with default status?"
assert configure_port(2, "disabled") == __, "Fix this: what is returned with disabled status?"

# Dictionaries - key-value pairs (like a network device configuration)
device = {
    "hostname": "CORE-SW-01",
    "ip": "192.168.1.1",
    "model": "Cisco 2960"
}

assert device["hostname"] == __, "Fix this: what is the hostname?"
assert device["ip"] == __, "Fix this: what is the IP?"
assert len(device) == __, "Fix this: how many keys in the dictionary?"

# Adding to dictionaries
device["vlan"] = 100
assert device["vlan"] == __, "Fix this: what is the VLAN value?"

# Dictionary methods
assert "hostname" in device, "hostname should be in device"
assert "port" in device, "Fix this: is 'port' in device? Change to correct assertion"

# Dictionaries with lists
network_config = {
    "vlans": [10, 20, 30],
    "allowed_ports": [1, 2, 3, 4, 5]
}

assert network_config["vlans"][0] == __, "Fix this: what is the first VLAN?"
assert len(network_config["allowed_ports"]) == __, "Fix this: how many allowed ports?"

# Function returning a dictionary
def create_device_config(name, ip, device_type):
    return {
        "name": name,
        "ip": ip,
        "type": device_type,
        "status": "active"
    }

router = create_device_config("RTR-01", "10.0.0.1", "Router")
assert router["name"] == __, "Fix this: what is the router name?"
assert router["status"] == __, "Fix this: what is the default status?"

# List of dictionaries (very common in network automation!)
devices = [
    {"name": "SW-01", "ip": "192.168.1.1", "type": "Switch"},
    {"name": "RTR-01", "ip": "10.0.0.1", "type": "Router"},
    {"name": "FW-01", "ip": "172.16.0.1", "type": "Firewall"}
]

assert len(devices) == __, "Fix this: how many devices?"
assert devices[0]["name"] == __, "Fix this: what is the first device name?"
assert devices[1]["type"] == __, "Fix this: what is the second device type?"

# Function to filter devices
def get_devices_by_type(device_list, device_type):
    result = []
    for device in device_list:
        if device["type"] == device_type:
            result.append(device)
    return result

switches = get_devices_by_type(devices, "Switch")
assert len(switches) == __, "Fix this: how many switches?"
assert switches[0]["ip"] == __, "Fix this: what is the switch IP?"

# Dictionary comprehension (advanced!)
device_names = [d["name"] for d in devices]
assert device_names == __, "Fix this: what is the list of device names?"

# Create a dictionary from lists
names = ["SW-01", "SW-02", "SW-03"]
ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
name_to_ip = dict(zip(names, ips))
assert name_to_ip["SW-02"] == __, "Fix this: what is SW-02's IP?"

print("✓ Koan 3 completed! You understand functions and dictionaries.")
