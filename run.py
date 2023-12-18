import csv

sammelkarten_liste = []

def karte_eingeben():
    nummern = input("Gib die Nummern der Sammelkarten (durch Leerzeichen getrennt) ein: ")
    nummern = list(map(int, nummern.split()))

    for nummer in nummern:
        found = False
        for karte in sammelkarten_liste:
            if karte['Nummer'] == nummer:
                karte['Anzahl'] += 1
                found = True
                break

        if not found:
            sammelkarten_liste.append({'Nummer': nummer, 'Anzahl': 1})

def karte_versenden():
    nummern = input("Gib die Nummern der Sammelkarten zum Versenden (durch Leerzeichen getrennt) ein: ")
    nummern = list(map(int, nummern.split()))

    for nummer in nummern:
        found = False
        for karte in sammelkarten_liste:
            if karte['Nummer'] == nummer:
                if karte['Anzahl'] > 1:
                    karte['Anzahl'] -= 1
                else:
                    sammelkarten_liste.remove(karte)
                found = True
                break

        if not found:
            print(f"Fehler: Die Sammelkarte mit der Nummer {nummer} wurde nicht gefunden und kann nicht versendet werden.")

def liste_anzeigen():
    print("Liste der Sammelkarten:")
    for karte in sammelkarten_liste:
        print(f"Nummer: {karte['Nummer']}, Anzahl: {karte['Anzahl']}")

def exportiere_csv():
    with open('sammelkarten_liste.csv', 'w', newline='') as csvfile:
        fieldnames = ['Nummer', 'Anzahl']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for karte in sammelkarten_liste:
            writer.writerow(karte)

while True:
    print("\n1. Karte eingeben\n2. Karte versenden\n3. Liste anzeigen\n4. CSV exportieren\n5. Beenden")
    auswahl = int(input("Wähle eine Option (1-5): "))

    if auswahl == 1:
        karte_eingeben()
    elif auswahl == 2:
        karte_versenden()
    elif auswahl == 3:
        liste_anzeigen()
    elif auswahl == 4:
        exportiere_csv()
    elif auswahl == 5:
        break
    else:
        print("Ungültige Auswahl. Bitte wähle eine Option von 1 bis 5.")
