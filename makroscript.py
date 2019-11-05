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

#Abfrage der Config 
if config.true == 0:
    print ("Bitte config anpassen")
    sleep (10)
    exit(0)
elif config.true == 1:

    #Globale variablen für den Timer
    global ee,sc
    sc = 0
    ee = 0

    #Keylogger + Magic
    def test(Key):
        #globale Variablen damit die Werte weiter benutzt werden können
        global ts,tt,te,ee,sc,f

        #log in eine Variable schreiben
        x = str(Key)
        #starten des Loggings
        if x == config.s:
            sc = 1
            if ee == 1:
                #Timer beenden
                te = datetime.now()
                total = te - ts
                total = str(total).split(".")[0]
                f.write("Total Time -> " + str(total) + "\r")
                #Schließen der Datei
                f.close()   
                #Beenden des Scripts
                print("beenden")
                exit(0)
            else:
                #Dateinamen erstellen
                now = datetime.now()
                item = now.strftime(config.date)
                item = item + ".txt"
                #Datei anlegen
                f= open(config.dpfad + item,"w+")
                print("Datei erstellt:" +item)
                #Timer starten
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
    
#Tastatur Logging
with Listener(on_press=test) as listener:
            listener.join()