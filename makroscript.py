#Version 1.0 By Nox7-Media @ Julian Schiefer

from time import sleep
import sys
from pathlib import Path
from pynput.keyboard import Key, Listener
from datetime import datetime
import config

#im Pynput-Master Ordner die "setup.py" datei ausführen
#"py -m pip install pynput" in der console ausführen
#keys verteilen

#Checken ob eine Datei exestiert und im zweifelsfall erstellen
now = datetime.now()
item = now.strftime(config.date)
item = item + ".txt"

file = Path(config.dpfad + item)
#Abfrage der Config 
if config.true == 0:
    print ("Bitte config anpassen")
    sleep (10)
    exit(0)
elif config.true == 1:

    #Checken ob datei exestiert
    if file.is_file():
        print("Datei exestiert")
        f= open(config.dpfad + item,"w+")
    else:
        #datei erstellen
        f= open(config.dpfad + item,"w+")
        print("Datei erstellt:" +item)
        print ("Warter auf start")

    #Globale variablen für den Timer
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
        if x == config.s:
            sc = 1
            if ee == 1:
                te = datetime.now()
                total = te - ts
                total = str(total).split(".")[0]
                f.write("Total Time -> " + str(total) + "\r")
                f.close()   
                print("beenden")
                exit(0)
            else:
                print("start")
                ts = datetime.now()
                ee = 1
                f.write("Start" + "\r")
        #Die Timestamps setzen
        elif x == config.t and sc == 1:
            print("timestamp")
            tt = datetime.now()
            current = tt - ts
            current = str(current).split(".")[0]
            f.write("Timestamp -> " + str(current) + "\r")
        #Die Funny setzen
        elif x == config.f and sc == 1:
            print("Funny")
            tt = datetime.now()
            current = tt - ts
            current = str(current).split(".")[0]
            f.write("Timestamp -> " + str(current) + "\r")
        #Beenden des Loggings  
    
#Tastatur Logging
with Listener(on_press=test) as listener:
            listener.join()