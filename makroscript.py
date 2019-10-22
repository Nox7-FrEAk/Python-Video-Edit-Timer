import datetime
import sys
from pathlib import Path
from pynput.keyboard import Key, Listener

#im Pynput-Master Ordner die "setup.py" datei ausführen
#"py -m pip install pynput" in der console ausführen
#keys verteilen
#bei normalen keys: "'e'" bei operatoren 'Key.f3'
s = 'Key.f12'
t = 'Key.f10'
e = "'-'"


#Checken ob eine Datei exestiert und im zweifelsfall erstellen
file = Path("Aufnahme.txt")

if file.is_file():
    print("Datei exestiert")
    f= open("Aufnahme.txt","w+")
else:
    print("Datei nicht gefunden")
    print("Soll datei erstellt werden?")
    l = 1
    while (l == 1):
        x = input("Eingabe(y/n)")

        if x == "y":
            #datei erstellen
            f= open("Aufnahme.txt","w+")
            l=0
            print("datei erstellt")
        elif x =="n":
            print("ok...")

global ee,sc
sc = 0
ee = 0

#Keylogger + Magic
def test(Key):
    #globale Variablen damit die Werte weiter benutzt werden können
    global ts,tt,te,ee,sc

    #log in eine Variable schreiben
    x = str(Key)
    #starten des Loggings
    if x == s:
        sc = 1
        if ee == 1:
            te = datetime.datetime.now()
            total = te - ts
            f.write("Total Time -> " + str(total) + "\r")
            f.close()   
            ee = 2
            print("stoppen")
        elif ee == 2:
            f.close()
            print("beenden")
            exit(0)
        else:
            print("start")
            ts = datetime.datetime.now()
            ee = 1
            f.write("Start" + "\r")
    #Die Timestamps setzen
    elif x == t and sc == 1:
        print("timestamp")
        tt = datetime.datetime.now()
        current = tt - ts
        f.write("Timestamp -> " + str(current) + "\r")
    #Beenden des Loggings  
    
#Tastatur Logging
with Listener(on_press=test) as listener:
            listener.join()