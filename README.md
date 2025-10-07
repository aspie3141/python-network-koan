# Python Koans för Nätverkstekniker

**Kurs:** Nätverksteknik (50 YH-poäng)
**Lärare:** Johan Saldes
**Kursmål:** K11 - Redogöra för Python-script för att kunna automatisera och optimera nätverksdrift

## Vad är Koans?

Koans är programmeringsövningar där du lär dig genom att "fylla i luckor" i kod. Varje koan innehåller tester som misslyckas, och din uppgift är att få testerna att bli gröna genom att ersätta `__` (understreck) med rätt värden eller kod.

Konceptet kommer från Zen Buddhism och har anpassats för programmering - du lär dig Python genom att lösa små problem steg för steg.

## Struktur

Koanerna är organiserade i två delar:

### Del 1: Grundläggande Python (3 koans)
1. **Variables and Strings** (Lätt) - Variabler, strängar, grundläggande operationer
2. **Lists and Loops** (Medium) - Listor, for-loopar, list comprehensions
3. **Functions and Dictionaries** (Svår) - Funktioner, dictionaries, komplex datahantering

### Del 2: Nätverksautomation (3 koans)
4. **IP Address Validation** (Lätt) - IP-adressvalidering, CIDR, subnät
5. **Device Inventory** (Medium) - Hantera nätverksutrustning, inventarier, CSV
6. **Network Monitoring** (Svår) - Logganalys, prestandaövervakning, alerter

## Installation och Körning

### Förutsättningar
- Python 3.7 eller senare installerat
- En textredigerare (VS Code, Sublime Text, eller valfri IDE)

### Steg för steg

1. **Navigera till koan-mappen:**
   ```bash
   cd /Users/johan/Documents/arbete/Nätverkskommunikation/python_programming/koan
   ```

2. **Kör alla koans:**
   ```bash
   python3 run_koans.py
   ```

3. **Programmet kommer att stanna vid första felet:**
   ```
   ✗ Failed: Fix this: what is the value of network_device?
   File: basic_python/01_variables_and_strings.py
   ```

4. **Öppna filen och fixa felet:**
   - Hitta raden med `__` (understreck)
   - Ersätt `__` med rätt värde
   - Spara filen

5. **Kör igen:**
   ```bash
   python3 run_koans.py
   ```

6. **Upprepa tills alla koans är gröna!**

## Exempel

Här är ett exempel på hur en koan ser ut:

```python
# I filen finns detta:
network_device = "Switch"
assert network_device == __, "Fix this: what is the value of network_device?"

# Du ändrar till:
network_device = "Switch"
assert network_device == "Switch", "Fix this: what is the value of network_device?"
```

## Tips för Studenter

### För Nybörjare (G-nivå)
1. Börja med de grundläggande Python-koanerna (01-03)
2. Läs kommentarerna noggrant - de förklarar vad som händer
3. Testa att köra kodens delar i Python-konsolen för att förstå bättre
4. Använd `print()` för att se värden när du är osäker
5. Gå vidare till nätverksautomation (04-06) när du känner dig bekväm

### För Avancerade (VG-nivå)
1. Försök lösa alla koans utan att titta på facit
2. Efter att ha löst en koan, försök skriva liknande funktioner själv
3. Utöka koanerna med dina egna tester
4. Försök optimera lösningarna för bättre prestanda
5. Kombinera flera koncept från olika koans

## Vanliga Problem och Lösningar

### Problem: "SyntaxError"
- **Orsak:** Du har skrivit ogiltig Python-kod
- **Lösning:** Kolla att du har rätt antal citattecken, parenteser, etc.

### Problem: "AssertionError"
- **Orsak:** Ditt svar är inte korrekt
- **Lösning:** Läs felmeddelandet, det ger ofta ledtrådar

### Problem: "NameError: name '__' is not defined"
- **Orsak:** Du har glömt att ersätta `__` med rätt värde
- **Lösning:** Hitta alla `__` i filen och ersätt dem

## Koppling till Kursmål

Dessa koans hjälper dig att uppnå följande kursmål:

- **K11:** Redogöra för Python-script för att kunna automatisera och optimera nätverksdrift
- **F3:** Övervaka nätverksprestanda och hantera incidenter/problem
- **F6:** Dokumentera nätverksarkitektur och konfigurationer
- **K5:** Redogöra för IP-adresser i nätverk
- **K1:** Redogöra för nätverksutrustning och olika produkter

## Praktiska Tillämpningar

Kunskaperna du lär dig här används för att:

✅ **Automatisera konfiguration** av switchar och routrar
✅ **Övervaka nätverksprestanda** och upptäcka problem
✅ **Hantera inventarier** av nätverksutrustning
✅ **Analysera loggar** för felsökning
✅ **Generera rapporter** om nätverksstatus
✅ **Validera konfigurationer** innan deployment

## Nästa Steg

När du är klar med koanerna:

1. ✅ Applicera kunskaperna på riktiga nätverksscenarier
2. ✅ Utforska nätverksbibliotek som `netmiko`, `napalm`, `paramiko`
3. ✅ Bygg egna automationsskript för laborationsmiljön
4. ✅ Delta i kursprojektet med Python-automation

## Resurser

- **Kurslitteratur:** "Mastering Python Networking" av Eric Chou
- **Python Dokumentation:** https://docs.python.org/3/
- **Nätverksautomation:** https://github.com/networktocode
- **Övningslabb:** Använd era Cisco/Arista-labbar för att testa skript

## Support

Om du fastnar:

1. Läs felmeddelandet noga - det ger ofta svaret
2. Använd `print()` för att debugga
3. Diskutera med klasskamrater
4. Fråga läraren (Johan Saldes)
5. Använd Python-dokumentationen

## Lycka till! 🐍🌐

> "En nätverkstekniker som kan Python är som en ninja med extra verktyg!"
> — Johan Saldes

---

**Senast uppdaterad:** Oktober 2025
**Version:** 1.0
