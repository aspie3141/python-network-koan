# Python Koans - Projektöversikt

**Skapad för:** Nätverksteknik-kursen (NT25G_NT)
**Kursansvarig:** Johan Saldes
**Datum:** Oktober 2025

---

## Projektstruktur

```
koan/
├── README.md                          # Studentinstruktioner (svenska)
├── ANSWER_KEY.md                      # Facit för lärare (KONFIDENTIELL)
├── OVERVIEW.md                        # Detta dokument
├── run_koans.py                       # Huvudskript för att köra koans
│
├── basic_python/                      # Del 1: Grundläggande Python
│   ├── 01_variables_and_strings.py   # Lätt - Variabler & strängar
│   ├── 02_lists_and_loops.py         # Medium - Listor & loopar
│   └── 03_functions_and_dictionaries.py  # Svår - Funktioner & dicts
│
└── network_automation/                # Del 2: Nätverksautomation
    ├── 01_ip_address_validation.py   # Lätt - IP-validering
    ├── 02_device_inventory.py        # Medium - Device management
    └── 03_network_monitoring.py      # Svår - Monitoring & logging
```

---

## Snabböversikt

### 📚 Koans (6 st totalt)

#### **Del 1: Grundläggande Python**

| # | Namn | Nivå | Tid | Koncept |
|---|------|------|-----|---------|
| 01 | Variables & Strings | Lätt | 15-20 min | Variabler, strängar, string-metoder |
| 02 | Lists & Loops | Medium | 30-40 min | Listor, for-loopar, list comprehensions |
| 03 | Functions & Dictionaries | Svår | 45-60 min | Funktioner, dicts, komplex data |

#### **Del 2: Nätverksautomation**

| # | Namn | Nivå | Tid | Koncept | Kursmål |
|---|------|------|-----|---------|---------|
| 04 | IP Address Validation | Lätt | 30-40 min | IP-validering, CIDR, subnät | K5, K11 |
| 05 | Device Inventory | Medium | 45-60 min | Inventory, CSV, data mgmt | K1, F6, K11 |
| 06 | Network Monitoring | Svår | 60-90 min | Logging, monitoring, alerts | K12, K13, F3, F4 |

**Total tid:** ~3.5-4.5 timmar

---

## Hur Koans Fungerar

### Koncept
Koans är programmeringsövningar baserade på Zen Buddhism:
- Studenten möter kod som inte fungerar
- Uppgiften är att "fylla i luckor" (ersätta `__`)
- När alla tester är gröna, har studenten lärt sig konceptet

### Pedagogisk Metod
1. **Läsa** - Förstå vad koden gör
2. **Reflektera** - Fundera på vad som saknas
3. **Prova** - Testa sin lösning
4. **Upprepa** - Till alla tester är gröna

### Exempel
```python
# Studenten ser detta:
ip_address = "192.168.1.1"
octets = ip_address.split(".")
assert len(octets) == __, "Fix this: how many octets?"

# De fyller i:
assert len(octets) == 4, "Fix this: how many octets?"
```

---

## Användning

### För Studenter
```bash
# Navigera till mappen
cd koan

# Kör alla koans
python3 run_koans.py

# Eller direkt:
./run_koans.py
```

Programmet stannar vid första felet och visar filnamn.

### För Lärare
Se `ANSWER_KEY.md` för kompletta lösningar och pedagogiska tips.

---

## Koppling till Kursmål

### Kunskapsmål (K)
- **K1:** Nätverksutrustning → Koan 05
- **K5:** IP-adresser → Koan 04
- **K11:** Python-script för automation → Alla koans
- **K12:** Nätverksdrift → Koan 06
- **K13:** Övervaka kommunikation → Koan 06

### Färdighetsmål (F)
- **F3:** Övervaka prestanda → Koan 06
- **F4:** Diagnostisera problem → Koan 06
- **F6:** Dokumentera arkitektur → Koan 05

---

## Lämplig Användning i Kursen

### Lektion 2025-10-07 (Python-automation dag)

**09:00-13:00: Python-introduktion**
- Genomgång av koans-konceptet (15 min)
- Demo av första koanen (15 min)
- Studenter börjar med Koan 01-03 (2-3 timmar)

**13:00-15:00: Gästföreläsning**
- Magnus Peterson från Validit

**15:00-16:00: Nätverksautomation**
- Introduktion till Koan 04-06
- Studenter börjar med nätverksautomation

### Lektion 2025-11-10 (Fördjupning Python)

**09:00-16:00: Fortsättning och fördjupning**
- Slutför alla koans
- Diskussion av lösningar
- Skriva egna automationsskript
- Applicera på labbmiljön

---

## Bedömning

### Godkänt (G)
✅ Slutför Koan 01-05 med handledning
✅ Förklara grundläggande Python-koncept
✅ Applicera på enkla automationsuppgifter

### Väl Godkänt (VG)
✅ Slutför alla koans (01-06) självständigt
✅ Förklara och motivera lösningar
✅ Skriva egna funktioner utöver koanerna
✅ Optimera kod för prestanda
✅ Applicera på komplexa nätverksscenarier

---

## Tekniska Detaljer

### Krav
- Python 3.7+
- Ingen externa dependencies
- Fungerar på Mac, Linux, Windows

### Filformat
- Alla koans: `.py` filer med assertions
- Runner: `run_koans.py` - kör alla koans i ordning
- Stannar vid första felet för fokuserat lärande

### Testing
Använder Pythons inbyggda `assert` statement:
```python
assert värde == förväntat, "Felmeddelande"
```

---

## Vidareutveckling

### För Nästa År
Möjliga utökningar:
1. **IPv6-koans** - Hantera IPv6-adresser
2. **VLAN-automation** - Konfigurera VLANs
3. **Config templates** - Jinja2-templates för configs
4. **REST API** - Anropa nätverks-APIs
5. **Netmiko-koans** - SSH till verklig utrustning

### Extra Utmaningar för Avancerade
- Implementera subnetting-kalkylator
- SNMP-simulering
- Syslog-server i Python
- Cisco config-generator

---

## Resurser och Referenser

### Kurslitteratur
- **Huvudbok:** "Mastering Python Networking" av Eric Chou
- Kapitel 2-3 är mest relevanta för koanerna

### Online Resurser
- Python docs: https://docs.python.org/3/
- Real Python: https://realpython.com/
- Network Automation: https://github.com/networktocode

### Verktyg för Fortsättning
Efter koanerna kan studenter utforska:
- `netmiko` - SSH till nätverksutrustning
- `napalm` - Multi-vendor network automation
- `paramiko` - SSH-bibliotek
- `ansible` - Automation platform

---

## Vanliga Frågor (FAQ)

### Q: Hur lång tid tar det?
**A:** 3.5-4.5 timmar för de flesta studenter. Snabba studenter kan klara det på 2-3 timmar.

### Q: Kan studenter hoppa över koans?
**A:** Nej, de bygger på varandra. Men avancerade studenter kan gå snabbare genom de tidiga.

### Q: Vad om någon kör fast?
**A:**
1. Läs felmeddelandet noga
2. Använd `print()` för debugging
3. Diskutera med klasskamrat
4. Fråga läraren
5. Se ledtrådar i kommentarerna

### Q: Kan de använda Google/ChatGPT?
**A:** Ja, men uppmuntra först eget tänkande. Målet är förståelse, inte bara rätt svar.

### Q: Fungerar det på Windows?
**A:** Ja! Använd `python` istället för `python3` i terminalen.

---

## Slutsats

Detta koan-system ger studenterna:
- ✅ Strukturerat lärande i Python
- ✅ Direkt koppling till nätverksautomation
- ✅ Praktiska färdigheter för yrkesrollen
- ✅ Självkörande med omedelbar feedback
- ✅ Progressiv svårighetsgrad

**Lycka till med kursen!** 🐍🌐

---

*För frågor, kontakta Johan Saldes - johan.saldes@lararvikarie.nu*
