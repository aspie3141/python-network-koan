"""
Network Koan 2: Device Inventory Management (MEDIUM)
====================================================

In this exercise, you'll learn about:
- Managing network device inventories
- Working with structured data
- Device configuration management
- Filtering and searching devices

This koan relates to course goals:
- K1: Redogöra för nätverksutrustning och olika produkter inom nätverksteknik
- F6: Dokumentera nätverksarkitektur och konfigurationer
- K11: Redogöra för Python-script för att kunna automatisera nätverksdrift
"""

# Network device inventory
devices = [
    {"hostname": "CORE-SW-01", "ip": "10.0.0.1", "type": "Switch", "vlan": 1, "location": "Server Room"},
    {"hostname": "DIST-SW-01", "ip": "10.0.1.1", "type": "Switch", "vlan": 10, "location": "Floor 1"},
    {"hostname": "DIST-SW-02", "ip": "10.0.1.2", "type": "Switch", "vlan": 20, "location": "Floor 2"},
    {"hostname": "EDGE-RTR-01", "ip": "203.0.113.1", "type": "Router", "vlan": 1, "location": "Server Room"},
    {"hostname": "FW-01", "ip": "198.51.100.1", "type": "Firewall", "vlan": 1, "location": "DMZ"},
]

# Basic inventory queries
assert len(devices) == 5 , "Fix this: how many devices in inventory?"

# Find device by hostname
def find_device_by_hostname(inventory, hostname):
    for device in inventory:
        if device["hostname"] == hostname:
            return device
    return None

core_switch = find_device_by_hostname(devices, "CORE-SW-01")
assert core_switch["ip"] == "10.0.0.1", "Fix this: what is the core switch IP?"
assert core_switch["location"] == "Server Room", "Fix this: where is the core switch?"

# Get all devices of a specific type
def get_devices_by_type(inventory, device_type):
    return [d for d in inventory if d["type"] == device_type]

switches = get_devices_by_type(devices, "Switch")
assert len(switches) == 3 , "Fix this: how many switches?"

routers = get_devices_by_type(devices, "Router")
assert len(routers) == 1 , "Fix this: how many routers?"

# Get devices in a location
def get_devices_by_location(inventory, location):
    result = []
    for device in inventory:
        if device["location"] == location:
            result.append(device)
    return result

server_room_devices = get_devices_by_location(devices, "Server Room")
assert len(server_room_devices) == 2 , "Fix this: how many devices in Server Room?"

# Count devices by type
def count_devices_by_type(inventory):
    counts = {}
    for device in inventory:
        device_type = device["type"]
        if device_type in counts:
            counts[device_type] += 1
        else:
            counts[device_type] = 1
    return counts

device_counts = count_devices_by_type(devices)
assert device_counts["Switch"] == 3 , "Fix this: how many switches?"
assert device_counts["Router"] == 1 , "Fix this: how many routers?"
assert device_counts["Firewall"] == 1 , "Fix this: how many firewalls?"

# Generate device configuration templa_te
def generate_device_config(device):
    config = f"""
hostname {device['hostname']}
interface Vlan{device['vlan']}
 ip address {device['ip']} 255.255.255.0
!
""".strip()
    return config

config = generate_device_config(devices[0])
assert "hostname CORE-SW-01" in config, "Fix this: config should contain hostname"
assert "10.0.0.1" in config, "Fix this: config should contain IP address"

# Add new device to inventory
def add_device(inventory, hostname, ip, device_type, vlan, location):
    new_device = {
        "hostname": hostname,
        "ip": ip,
        "type": device_type,
        "vlan": vlan,
        "location": location
    }
    inventory.append(new_device)
    return inventory

# Add a new access switch
devices = add_device(devices, "ACC-SW-01", "10.0.2.1", "Switch", 30, "Floor 3")
assert len(devices) == 6 , "Fix this: how many devices after adding one?"

new_device = find_device_by_hostname(devices, "ACC-SW-01")
assert new_device["location"] == "Floor 3", "Fix this: what is the new device location?"

# Update device information
def update_device_ip(inventory, hostname, new_ip):
    device = find_device_by_hostname(inventory, hostname)
    if device:
        device["ip"] = new_ip
        return True
    return False

success = update_device_ip(devices, "ACC-SW-01", "10.0.2.10")
assert success == True, "Fix this: was the update successful?"

updated_device = find_device_by_hostname(devices, "ACC-SW-01")
assert updated_device["ip"] == "10.0.2.10", "Fix this: what is the updated IP?"

# Generate inventory report
def generate_inventory_report(inventory):
    report_lines = ["Network Device Inventory Report", "=" * 40]

    for device in inventory:
        line = f"{device['hostname']:15} | {device['ip']:15} | {device['type']:10} | {device['location']}"
        report_lines.append(line)

    return "\n".join(report_lines)

report = generate_inventory_report(devices[:2])  # First 2 devices only
lines = report.split("\n")
assert len(lines) == 4 , "Fix this: how many lines in report? (header + separator + 2 devices)"
assert "CORE-SW-01" in report, "Fix this: report should contain CORE-SW-01"

# Export to CSV format
def export_to_csv(inventory):
    csv_lines = ["hostname,ip,type,vlan,location"]
    for device in inventory:
        line = f"{device['hostname']},{device['ip']},{device['type']},{device['vlan']},{device['location']}"
        csv_lines.append(line)
    return "\n".join(csv_lines)

csv_output = export_to_csv(devices[:2])
csv_rows = csv_output.split("\n")
assert len(csv_rows) == 3 , "Fix this: how many CSV rows? (header + 2 devices)"
assert csv_rows[0] == "hostname,ip,type,vlan,location", "Fix this: what is the CSV header?"

# Parse CSV back to device list
def parse_csv_to_devices(csv_string):
    lines = csv_string.strip().split("\n")
    headers = lines[0].split(",")
    device_list = []

    for line in lines[1:]:
        values = line.split(",")
        device = {
            "hostname": values[0],
            "ip": values[1],
            "type": values[2],
            "vlan": int(values[3]),
            "location": values[4]
        }
        device_list.append(device)

    return device_list

csv_data = "hostname,ip,type,vlan,location\nTEST-SW-01,10.1.1.1,Switch,100,Test Lab"
parsed = parse_csv_to_devices(csv_data)
assert len(parsed) == 1 , "Fix this: how many devices parsed?"
assert parsed[0]["hostname"] == "TEST-SW-01", "Fix this: what is the hostname?"
assert parsed[0]["vlan"] == 100 , "Fix this: what is the VLAN (as number)?"

print("✓ Network Koan 2 completed! You can manage device inventories.")
