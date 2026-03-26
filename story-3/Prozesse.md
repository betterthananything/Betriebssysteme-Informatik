## Prozesse
Ein Prozess ist einfach gesagt ein aktives Programm. Jedoch kommen zu dem Programm noch die aktuellen States, Memory und die System Ressourcen die verwendet werden dazu.

### ***Attribute***
Die Attribute werden in dem sogenannten Process Control Block (PCB) gespeichert.
- Process ID (PID): individuell für jeden Prozess damit das System überblick hat
- Process State: Aktueller Status
- Priority & Scheduling Info: Wichtigkeit, gibt dem OS an, welcher Prozess als nächstes gemacht werden muss
- I/O Info: Input/Output Information des Prozesses
- Dateideskriptor: Zahl um auf eine Datei (auch directory, netzwerk socket und terminal) zuzugreifen)
- Resourcenverbrauchsdaten (Accounting Information): Gibt an wie lang der Prozess schon läuft, wie viel CPU Zeit es verbraucht hat und andere Resourcenverbrauchdaten
- Memory Management Info: Info zur allocated memory, wo im memory es geladen ist und die Struktur (Stack, heap, etc.)

### ***States***
Die States werden mithilfe des 5-State-Modells dargestellt
1. New: Neuer Prozess der noch nicht gelaufen ist, dessen PCB aber schon vorbereitet ist
2. Ready: Der Prozess ist bereit und wartet nur darauf, dass die CPU frei wird
3. Running: Die CPU führt den Prozess aus	
4. Blocked/Waiting: Prozess kann nicht ausgeführt werden, wartet auf ein Event (z.B. I/O oder data input)
5. Exit/Terminate: Der Prozess wurde beendet bzw. abgebrochen? und das System entfernt ihn aus dem Memory
