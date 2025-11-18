#Notizen 

def neue_notiz ():
    text = input ("Neue Notiz: ")
    Notiz.append (text)
    print ("Neue Notiz gespeichert.")

def notizen_anzeigen ():
    if len(Notiz) == 0:
       print ("Keine Notiz vorhanden.")
    else:
       print (Notiz)

def notizen_loeschen ():
    nummer = int(input("Welche Notiz soll gelöscht werden? Nummer eingeben: ")) 
    if 1 <= nummer <= len(Notiz):
       Notiz.pop (nummer - 1)
    else:
       print ("Nummer ungültig!")

Notiz = []
enumerate(Notiz)

while True:

 print ("1) Neue Notiz speichern")
 print ("2) Alle Notizen anzeigen")
 print ("3) Notiz löschen")
 print ("4) Beenden")



 Wahl = int(input("Wähle eine Option: ")) 

 if Wahl == 1:
    neue_notiz()
    
 elif Wahl == 2:
    notizen_anzeigen()

 elif Wahl == 3:
    notizen_loeschen()

 elif Wahl == 4:
    print ("Programm beendet")
    break 
 else:
    print ("Ungültige Eingabe")
 


