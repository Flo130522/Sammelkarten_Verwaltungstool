# Sammelkarten-Verwaltungstool
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/flo130522/Sammelkarten_Verwaltungstool.svg?style=for-the-badge
[contributors-url]: https://github.com/flo130522/Sammelkarten_Verwaltungstool/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/flo130522/Sammelkarten_Verwaltungstool.svg?style=for-the-badge
[forks-url]: https://github.com/flo130522/Sammelkarten_Verwaltungstool/network/members
[stars-shield]: https://img.shields.io/github/stars/flo130522/Sammelkarten_Verwaltungstool.svg?style=for-the-badge
[stars-url]: https://github.com/flo130522/Sammelkarten_Verwaltungstool/stargazers
[issues-shield]: https://img.shields.io/github/issues/flo130522/Sammelkarten_Verwaltungstool.svg?style=for-the-badge
[issues-url]: https://github.com/flo130522/Sammelkarten_Verwaltungstool/issues
[license-shield]: https://img.shields.io/github/license/flo130522/Sammelkarten_Verwaltungstool.svg?style=for-the-badge
[license-url]: https://github.com/flo130522/Sammelkarten_Verwaltungstool/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/flokurek
Das Sammelkarten Verwaltungs-Tool ist eine Anwendung, die es ermöglicht, eine Liste von Sammelkarten zu erstellen, zu verwalten, zu versenden und in einer CSV-Datei zu speichern. Die Anwendung wurde in Python unter Verwendung von Tkinter für die Benutzeroberfläche entwickelt.

## Funktionen
### Karte eingeben
Fügt eine oder mehrere Sammelkarten mit ihren Nummern hinzu.

### Karte versenden
Verringert die Anzahl einer bestimmten Sammelkarte, wenn sie versendet wird.

### Liste anzeigen
Zeigt die zuletzt hinzugefügten Sammelkarten unter den Buttons an. Bei Klick öffnet sich ein separates Fenster mit einer Liste aller Sammelkarten.

### CSV exportieren
Exportiert die Sammelkartendaten in eine CSV-Datei.

### CSV importieren
Importiert Sammelkartendaten aus einer CSV-Datei.

## Anleitung zur Verwendung
### Karte eingeben
Geben Sie die Nummern der Sammelkarten durch Leerzeichen getrennt ein und klicken Sie auf "Karte eingeben".

### Karte versenden
Geben Sie die Nummern der zu versendenden Sammelkarten ein und klicken Sie auf "Karte versenden".

### Liste anzeigen
Zeigt die zuletzt hinzugefügten Sammelkarten unter den Buttons an. Klicken Sie darauf, um eine Liste aller Sammelkarten in einem separaten Fenster anzuzeigen.

### CSV exportieren
Exportiert die Sammelkartendaten in eine CSV-Datei mit dem Namen "sammelkarten_liste.csv".

### CSV importieren
Importiert Sammelkartendaten aus einer CSV-Datei. Der Benutzer wird gefragt, ob die vorhandenen Daten überschrieben werden sollen.

## Voraussetzungen
Python (getestet mit Version 3.6 und höher)
## Ausführung
Führen Sie das Skript sammelkarten_verwaltung.py aus, um das Tool zu starten. \
```
python sammelkarten_verwaltung.py
```

