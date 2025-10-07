"""
Koan 2: Lists and Loops (MEDIUM) - SOLVED VERSION
=================================
"""

# Lists store multiple values
devices = ["Router", "Switch", "Firewall"]
assert len(devices) == 3, "Fix this: how many devices are in the list?"
assert devices[0] == "Router", "Fix this: what is the first device?"
assert devices[-1] == "Firewall", "Fix this: what is the last device? (use negative index)"

# Adding to lists
vlans = [10, 20, 30]
vlans.append(40)
assert vlans == [10, 20, 30, 40], "Fix this: what is the list after appending 40?"

# Removing from lists
ports = [1, 2, 3, 4, 5]
ports.remove(3)
assert ports == [1, 2, 4, 5], "Fix this: what is the list after removing 3?"

# For loops - iterate through a list
ip_addresses = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
count = 0
for ip in ip_addresses:
    count += 1
assert count == 3, "Fix this: how many IPs did we count?"

# For loops - build a new list
original = [1, 2, 3, 4]
doubled = []
for num in original:
    doubled.append(num * 2)
assert doubled == [2, 4, 6, 8], "Fix this: what is the doubled list?"

# List comprehension (advanced but useful!)
numbers = [1, 2, 3, 4, 5]
even_numbers = [n for n in numbers if n % 2 == 0]
assert even_numbers == [2, 4], "Fix this: which numbers are even?"

# Practical example: filtering VLANs
all_vlans = [10, 20, 30, 40, 50, 100, 200]
# Get VLANs less than 50
low_vlans = [v for v in all_vlans if v < 50]
assert low_vlans == [10, 20, 30, 40], "Fix this: which VLANs are less than 50?"

# String operations with lists
hostname_list = ["SW01", "SW02", "SW03"]
hostname_string = ", ".join(hostname_list)
assert hostname_string == "SW01, SW02, SW03", "Fix this: what is the joined string?"

# Splitting strings into lists
csv_line = "192.168.1.1,Switch,Active"
parts = csv_line.split(",")
assert parts == ["192.168.1.1", "Switch", "Active"], "Fix this: what is the result of splitting?"
assert parts[1] == "Switch", "Fix this: what is the device type?"

print("✓ Koan 2 completed! You understand lists and loops.")
