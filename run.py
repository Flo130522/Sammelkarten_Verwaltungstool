import csv
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

sammelkarten_liste = []

def karte_eingeben(entry, text_widget):
    nummern = entry.get()
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

    entry.delete(0, tk.END)  
    liste_anzeigen(text_widget)

def karte_versenden(entry, text_widget):
    nummern = entry.get()
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
            messagebox.showerror("Fehler", f"Die Sammelkarte mit der Nummer {nummer} wurde nicht gefunden und kann nicht versendet werden.")

    entry.delete(0, tk.END)  

def liste_anzeigen(text_widget, separate_window=False):
    if separate_window:
        list_window = tk.Tk()
        list_window.title("Liste aller Sammelkarten")

        text_widget_separate = scrolledtext.ScrolledText(list_window, width=40, height=20)
        text_widget_separate.pack(padx=10, pady=10)

        text_widget_separate.insert(tk.END, "Liste aller Sammelkarten:\n")
        for karte in sammelkarten_liste:
            text_widget_separate.insert(tk.END, f"Nummer: {karte['Nummer']}, Anzahl: {karte['Anzahl']}\n")

        text_widget_separate.configure(state='disabled')  

        list_window.mainloop()
    else:
        text_widget.config(state='normal')  
        text_widget.delete('1.0', tk.END)  

        text_widget.insert(tk.END, "Liste der zuletzt hinzugefügten Sammelkarten:\n")
        for karte in sammelkarten_liste[-5:]:  
            text_widget.insert(tk.END, f"Nummer: {karte['Nummer']}, Anzahl: {karte['Anzahl']}\n")

        text_widget.config(state='disabled')  
        
def exportiere_csv():
    with open('sammelkarten_liste.csv', 'w', newline='') as csvfile:
        fieldnames = ['Nummer', 'Anzahl']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for karte in sammelkarten_liste:
            writer.writerow(karte)

def importiere_csv(dateipfad):
    if sammelkarten_liste:
        antwort = messagebox.askyesno("Daten überschreiben", "Möchten Sie die vorhandenen Daten überschreiben?")
        if not antwort:
            return 

    sammelkarten_liste.clear()
    
    with open(dateipfad, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            sammelkarten_liste.append({'Nummer': int(row['Nummer']), 'Anzahl': int(row['Anzahl'])})

def importiere_csv_durch_dialog():
    root = tk.Tk()
    root.withdraw()  
    file_path = filedialog.askopenfilename(title="CSV-Datei auswählen", filetypes=[("CSV-Dateien", "*.csv")])
    if file_path:
        importiere_csv(file_path)

def zeige_gui():
    root = tk.Tk()
    root.title("Sammelkarten Verwaltung")

    entry_label = tk.Label(root, text="Nummern eingeben:")
    entry_label.pack(pady=10)

    entry = tk.Entry(root, width=30)
    entry.pack(pady=10)

    eingeben_button = tk.Button(root, text="Karte eingeben", command=lambda: karte_eingeben(entry, text_widget))
    eingeben_button.pack(pady=5)

    versenden_button = tk.Button(root, text="Karte versenden", command=lambda: karte_versenden(entry, text_widget))
    versenden_button.pack(pady=5)

    anzeigen_button = tk.Button(root, text="Liste anzeigen", command=lambda: liste_anzeigen(text_widget, separate_window=True))
    anzeigen_button.pack(pady=10)

    export_button = tk.Button(root, text="CSV exportieren", command=exportiere_csv)
    export_button.pack(pady=10)

    import_button = tk.Button(root, text="CSV importieren", command=importiere_csv_durch_dialog)
    import_button.pack(pady=10)

    text_widget = scrolledtext.ScrolledText(root, height=10, width=40)
    text_widget.pack(pady=10)
    text_widget.config(state='disabled') 
    exit_button = tk.Button(root, text="Beenden", command=root.destroy)
    exit_button.pack(pady=10)

    root.mainloop()

zeige_gui()
