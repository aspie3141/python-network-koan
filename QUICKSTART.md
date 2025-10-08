# Snabbstart - Python Koans

**5 minuter till igång!** ⚡

---

## Steg 1: Kolla att Python finns

Öppna Terminal (Mac/Linux) eller Command Prompt (Windows):

```bash
python3 --version
```

Du bör se något som: `Python 3.11.x` eller liknande.

**Windows-användare:** Använd `python` istället för `python3`

## Steg 2: Navigera till koan-mappen

```bash
cd /Users/johan/Documents/arbete/Nätverkskommunikation/python_programming/koan
```

**Eller:** Öppna mappen i VS Code och använd den inbyggda terminalen.

---

## Steg 3: Kör dina första koan

```bash
python3 run_koans.py
```

Du kommer se något som:

```
====================================================================
PYTHON KOANS - Network Technician Edition
====================================================================

📁 Basic Python
--------------------------------------------------------------------
  ✗ Failed: Fix this: what is the value of network_device?
  File: basic_python/01_variables_and_strings.py

====================================================================
Fix the failing koan above, then run again!
====================================================================
```

---

## Steg 4: Fixa ditt första fel

1. **Öppna filen:** `basic_python/01_variables_and_strin
gs.py`

2. **Hitta raden med `__`** (understreck):
   ```python
   assert network_device == __, "Fix this..."
   ```

3. **Ersätt `__` med rätt värde:**
   ```python
   assert network_device == "Switch", "Fix this..."
   ```

4. **Spara filen** (Ctrl+S / Cmd+S)

---

## Steg 5: Kör igen

```bash
python3 run_koans.py
```

Om det var rätt, går du vidare till nästa fel. Om fel, försök igen!

---

## Tips & Tricks

### 💡 Använd Python-konsolen för att testa

```bash
python3

>>> network_device = "Switch"
>>> network_device
'Switch'
>>> len("192.168.1.1")
11
>>> exit()
```

### 💡 Använd print() för debugging

```python
ip_address = "192.168.1.1"
print(ip_address)        # Se värdet
print(len(ip_address))   # Se längden
```

### 💡 Läs felmeddelanden noga

```
✗ Failed: Fix this: how many octets in an IPv4 address?
```

Felmeddelandet ger ofta ledtrådar!

### 💡 Kör bara en koan

```bash
python3 basic_python/01_variables_and_strings.py
```

---

## Vanliga Problem

### Problem: "python3: command not found"
**Lösning:** Använd `python` istället

### Problem: "No such file or directory"
**Lösning:** Kolla att du är i rätt mapp med `pwd` (Mac/Linux) eller `cd` (Windows)

### Problem: "SyntaxError"
**Lösning:** Du har gjort ett stavfel. Kolla citattecken, parenteser, etc.

### Problem: "AssertionError"
**Lösning:** Ditt svar är inte rätt. Läs ledtråden i felmeddelandet.

---

## Progressionsplan

1. ✅ **Koan 01** - Variables & Strings (15-20 min)
2. ✅ **Koan 02** - Lists & Loops (30-40 min)
3. ✅ **Koan 03** - Functions & Dictionaries (45-60 min)
4. ✅ **Koan 04** - IP Validation (30-40 min)
5. ✅ **Koan 05** - Device Inventory (45-60 min)
6. ✅ **Koan 06** - Network Monitoring (60-90 min)

**Total tid:** ~3.5-4.5 timmar

---

## När du är klar

När alla koans är gröna:

```
====================================================================
🎉 CONGRATULATIONS! All koans completed!
====================================================================
```

**Nästa steg:**
- Visa för läraren
- Applicera på riktiga nätverkslabb
- Bygg egna automationsskript
- Utforska bibliotek som `netmiko` och `napalm`

---

## Hjälp Behövs?

1. 📖 Läs `README.md` för mer detaljer
2. 💬 Fråga en klasskamrat
3. 👨‍🏫 Fråga Johan
4. 🔍 Google error message (men försök själv först!)

---

**Lycka till!** 🚀

*Det här är början på din resa mot att bli en Python-kunnig nätverkstekniker!*
