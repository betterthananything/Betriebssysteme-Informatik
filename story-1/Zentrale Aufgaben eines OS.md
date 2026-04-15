
# Zentrale Aufgaben eines OS

### Definition:
* Das Betriebssystem bildet die Schnittstelle zwischen den Hardware-Komponenten und der Anwendungssoftware des Benutzers.

## Zentrale Aufgaben

### Prozessmanagement (Process Management)
Das Betriebssystem steuert die Ausführung aller aktiven Programme (Prozesse).

* **Zuweisung von Rechenzeit**
    * Der Scheduler entscheidet, welcher Prozess wie lange die CPU nutzen darf.
* **Multitasking**
    * Es ermöglicht den parallelen oder scheinbar gleichzeitigen Ablauf mehrerer Aufgaben.
* **Synchronisation**
    * Es regelt die Kommunikation und Koordination zwischen den verschiedenen Prozessen.

### Speicherverwaltung (Memory Management)
Das System verwaltet den physikalischen Arbeitsspeicher (RAM).

* **Adressraumzuweisung**
    * Jedem Prozess wird ein isolierter Speicherbereich zugewiesen, um Konflikte zu vermeiden.
* **Virtueller Speicher**
    * Bei Bedarf wird Festplattenspeicher als Erweiterung des RAM genutzt.

### Dateimanagement (File Management)
* **Dateisysteme**
    * Das Betriebssystem legt fest, wie Dateien strukturiert, benannt und gespeichert werden.