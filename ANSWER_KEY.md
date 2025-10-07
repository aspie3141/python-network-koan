# Facit - Python Koans för Nätverkstekniker

**OBS! Detta dokument är endast för läraren.**

## Basic Python Koans

### 01_variables_and_strings.py (EASY)

```python
assert network_device == "Switch"
assert full_name == "Cisco 2960"
assert len(ip_address) == 11
assert connection_string == "SWITCH01:22"
assert device_name.upper() == "ROUTER"
assert device_name.lower() == "router"
assert first_octet == "00"
```

**Svårighetsgrad:** Lätt
**Tidsuppskattning:** 15-20 minuter
**Lärandemål:** Grundläggande variabler, strängar, string-metoder

---

### 02_lists_and_loops.py (MEDIUM)

```python
assert len(devices) == 3
assert devices[0] == "Router"
assert devices[-1] == "Firewall"
assert vlans == [10, 20, 30, 40]
assert ports == [1, 2, 4, 5]
assert count == 3
assert doubled == [2, 4, 6, 8]
assert even_numbers == [2, 4]
assert low_vlans == [10, 20, 30, 40]
assert hostname_string == "SW01, SW02, SW03"
assert parts == ["192.168.1.1", "Switch", "Active"]
assert parts[1] == "Switch"
```

**Svårighetsgrad:** Medium
**Tidsuppskattning:** 30-40 minuter
**Lärandemål:** Listor, for-loopar, list comprehensions, string split/join

---

### 03_functions_and_dictionaries.py (HARD)

```python
assert result == "Router"
assert hostname == "SW05"
assert configure_port(1) == "Port 1 is enabled"
assert configure_port(2, "disabled") == "Port 2 is disabled"
assert device["hostname"] == "CORE-SW-01"
assert device["ip"] == "192.168.1.1"
assert len(device) == 3
assert device["vlan"] == 100
# Change to: assert "port" not in device (or comment out the failing line)
assert network_config["vlans"][0] == 10
assert len(network_config["allowed_ports"]) == 5
assert router["name"] == "RTR-01"
assert router["status"] == "active"
assert len(devices) == 3
assert devices[0]["name"] == "SW-01"
assert devices[1]["type"] == "Router"
assert len(switches) == 1
assert switches[0]["ip"] == "192.168.1.1"
assert device_names == ["SW-01", "RTR-01", "FW-01"]
assert name_to_ip["SW-02"] == "192.168.1.2"
```

**Svårighetsgrad:** Svår
**Tidsuppskattning:** 45-60 minuter
**Lärandemål:** Funktioner, dictionaries, komplex datastrukturer, list/dict comprehensions

---

## Network Automation Koans

### 01_ip_address_validation.py (EASY)

```python
assert len(octets) == 4
assert octets[0] == "192"
assert octets[3] == "100"
assert is_valid_octet("192") == True
assert is_valid_octet("300") == False
assert is_valid_octet("0") == True
assert is_valid_ip("192.168.1.1") == True
assert is_valid_ip("256.1.1.1") == False
assert is_valid_ip("10.0.0") == False
assert ip_part == "192.168.1.0"
assert prefix == "24"
assert int(prefix) == 24
assert prefix_to_subnet_mask(24) == "255.255.255.0"
assert prefix_to_subnet_mask(16) == "255.255.0.0"
assert is_private_ip("192.168.1.1") == True
assert is_private_ip("8.8.8.8") == False
assert is_private_ip("10.0.0.1") == True
assert is_private_ip("172.16.0.1") == True
assert len(ip_range) == 5
assert ip_range[0] == "192.168.1.10"
assert ip_range[4] == "192.168.1.14"
assert is_valid_mac("00:1A:2B:3C:4D:5E") == True
assert is_valid_mac("00:1A:2B:3C:4D") == False
```

**Svårighetsgrad:** Lätt-Medium
**Tidsuppskattning:** 30-40 minuter
**Lärandemål:** IP-validering, CIDR, subnät, MAC-adresser
**Kursmål:** K5 (IP-adresser), K11 (Python-script)

---

### 02_device_inventory.py (MEDIUM)

```python
assert len(devices) == 5
assert core_switch["ip"] == "10.0.0.1"
assert core_switch["location"] == "Server Room"
assert len(switches) == 3
assert len(routers) == 1
assert len(server_room_devices) == 3
assert device_counts["Switch"] == 3
assert device_counts["Router"] == 1
assert device_counts["Firewall"] == 1
# config assertions already in place
assert len(devices) == 6  # After adding one
assert new_device["location"] == "Floor 3"
assert success == True
assert updated_device["ip"] == "10.0.2.10"
assert len(lines) == 4  # header + separator + 2 devices
# report assertions already in place
assert len(csv_rows) == 3  # header + 2 devices
assert csv_rows[0] == "hostname,ip,type,vlan,location"
assert len(parsed) == 1
assert parsed[0]["hostname"] == "TEST-SW-01"
assert parsed[0]["vlan"] == 100
```

**Svårighetsgrad:** Medium-Svår
**Tidsuppskattning:** 45-60 minuter
**Lärandemål:** Inventory management, CSV, data manipulation
**Kursmål:** K1 (Nätverksutrustning), F6 (Dokumentation), K11 (Python)

---

### 03_network_monitoring.py (HARD)

```python
assert first_log["device"] == "CORE-SW-01"
assert first_log["level"] == "INFO"
assert first_log["message"] == "Port Gi0/1 is UP"
assert len(parsed_logs) == 7
assert len(errors) == 3
assert len(warnings) == 2
assert len(core_switch_logs) == 3
assert device_log_counts["DIST-SW-01"] == 2
assert len(critical_issues) == 3
# config assertions already in place
assert avg_cpu_core == 57.333333333333336  # (45+85+42)/3
# Or accept: assert round(avg_cpu_core, 2) == 57.33
assert len(high_cpu) == 1
assert high_cpu[0]["device"] == "CORE-SW-01"
assert alert["severity"] == "CRITICAL"
# alert message assertion already in place
assert total_bw == 1740  # 250+780+320+180+210
assert peak["bandwidth"] == 780
assert peak["device"] == "CORE-SW-01"
assert report["errors"] == 3
assert report["critical_issues"] == 3
assert report["devices_monitored"] == 2  # CORE-SW-01 and DIST-SW-01
assert uptime == 30  # 9:30 - 9:00 = 30 minutes
# health score around 36-37 (depends on rounding)
assert len(summary) == 1
# summary assertion already in place
```

**Svårighetsgrad:** Svår
**Tidsuppskattning:** 60-90 minuter
**Lärandemål:** Logganalys, performance monitoring, alerting
**Kursmål:** K12 (Nätverksdrift), K13 (Övervaka kommunikation), F3 (Övervaka prestanda), F4 (Diagnostisera problem)

---

## Bedömning och Betygssättning

### Godkänt (G)
Studenten ska kunna:
- Slutföra koans 01-03 (Basic Python) med viss hjälp
- Slutföra koans 04-05 (Network Automation Easy-Medium) med handledning
- Förklara grundläggande Python-koncept
- Applicera kunskaper på enkla automationsuppgifter

### Väl Godkänt (VG)
Studenten ska kunna:
- Slutföra alla koans (01-06) självständigt
- Förklara och motivera lösningarna
- Skriva egna funktioner utöver koanerna
- Optimera kod för bättre prestanda
- Applicera kunskaper på komplexa nätverksscenarier

---

## Pedagogiska Tips

### För lektionen 2025-10-07:

**Del 1: Introduktion (09:00-10:30)**
- Förklara koans-konceptet
- Demonstrera hur man kör `run_koans.py`
- Gå igenom första koanen tillsammans
- Låt studenterna börja själva

**Del 2: Självständigt arbete (10:45-12:00)**
- Studenter arbetar i sin egen takt
- Cirkulera och hjälp vid behov
- Uppmuntra par-programmering

**Del 3: Efter gästföreläsning (15:00-16:00)**
- Fortsätt med koans
- Fokusera på nätverksautomation
- Diskutera praktiska tillämpningar

### Vanliga Fallgropar

1. **String vs Integer**: Studenter glömmer att konvertera strängar till tal
   - Lösning: Påminn om `int()` och `str()`

2. **List indexing**: Förväxlar 0-baserad indexering
   - Lösning: Rita upp listor på tavlan med index

3. **Dictionary keys**: Använder fel datatyp för nycklar
   - Lösning: Visa exempel med olika nycklar

4. **Indentation**: Python är känsligt för indentering
   - Lösning: Använd konsekvent tabs eller spaces (rekommendera 4 spaces)

### Utökning för Avancerade Studenter

**Extra uppgifter:**
1. Skapa en koan som hanterar IPv6-adresser
2. Bygg en funktion som beräknar nätverksadress från IP och mask
3. Implementera SNMP-simulering med Python
4. Skapa ett skript som genererar Cisco-konfigurationer

---

## Sammanfattning

**Tidsplan:**
- Koans 01-03: ~90 minuter totalt
- Koans 04-06: ~120 minuter totalt
- **Total tid:** ~3.5 timmar aktivt arbete

**Rekommenderad hemuppgift:**
Låt studenter slutföra koanerna hemma om de inte hinner på lektionen.

**Uppföljning:**
Använd koncepten från koanerna i kommande laborationer med riktig nätverksutrustning.

---

**Lycka till med undervisningen!**

Johan Saldes
Kursansvarig - Nätverksteknik
