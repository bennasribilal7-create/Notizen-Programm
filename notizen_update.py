#Notizen 

from datetime import datetime
import json
Notiz = []

def laden():
   global Notiz
   try: 
      with open("notizen.json", "r", encoding="utf-8") as datei:
         Notiz = json.load(datei)
   except FileNotFoundError:
      Notiz = []

def speichern():
   with open ("notizen.json", "w", encoding="utf-8") as datei:
       json.dump(Notiz,datei, ensure_ascii=False, indent=4)

def neue_notiz ():
    Datum = datetime.now().strftime("%d.%b.%Y %H:%M")
    Titel = input ("Gib den Titel ein: ")
    Text = input ("Notiz: ")
    Notiz.append ({"Datum": Datum,"Titel": Titel,"Text": Text})
    print ("Neue Notiz gespeichert.")

def notizen_anzeigen ():
    if len(Notiz) == 0:
       print ("Keine Notiz vorhanden.")
    else:
       for i, n in enumerate(sorted(Notiz, key=lambda x:x ["Datum"], reverse = True), start=1):
          print(f"{i}: {n['Datum']} | {n['Titel']}\n -- {n['Text']} --")
def notizen_loeschen ():
    for i, n in enumerate(Notiz, start=1):
       print (f"{i}: {n['Datum']}\n {n['Titel']} | {n['Text']}")
    nummer = int(input("Welche Notiz soll gelöscht werden? Nummer eingeben: ")) 
    if 1 <= nummer <= len(Notiz):
       Notiz.pop (nummer - 1)
    else:
       print ("Nummer ungültig!")

def alle_notizen_loeschen():
    Notiz.clear()

laden()

while True:

 print ("1) Neue Notiz speichern")
 print ("2) Alle Notizen anzeigen")
 print ("3) Notiz löschen")
 print ("4) Alle Notizen löschen")
 print ("5) Beenden")



 Wahl = int(input("Wähle eine Option: ")) 

 if Wahl == 1:
    neue_notiz()
    speichern()
 elif Wahl == 2:
    notizen_anzeigen()

 elif Wahl == 3:
    notizen_loeschen()
    speichern()
 elif Wahl == 4:
    alle_notizen_loeschen()
    speichern()
 elif Wahl == 5:
    print ("Programm beendet")
    break 
 else:
    print ("Ungültige Eingabe")
 


