# Probleme bei der Nutzung gemeinsamer Ressourcen
In modernen Betriebssystemen ist die Trennung von Privilegienstufen essenziell, um die Stabilität und Sicherheit des Systems zu gewährleisten. Ohne diese Trennung könnte jedes Programm direkt auf die Hardware zugreifen, was zu Datenverlust, Systemabstürzen oder Sicherheitslücken führen würde.

### Kernel Mode vs. User Mode
Das Betriebssystem wechselt je nach Art der ausgeführten Aufgabe zwischen zwei Modi:
##### 1. Kernel Mode (Privilegierter Modus)
   Im Kernel-Modus hat der ausführende Code uneingeschränkten Zugriff auf die zugrunde liegende Hardware und alle Speicheradressen.
   - **Zweck:** Ausführung von Betriebssystem-Kernfunktionen, Verwaltung von Hardware (CPU, RAM, Festplatten) und Steuerung von Treibern.
   - **Sicherheit:** Ein Absturz im Kernel-Modus ist kritisch und führt meist zu einem Systemstopp (z. B. dem „Blue Screen of Death“).
   - **Ressourcenzugriff:** Direkter Zugriff auf I/O-Geräte und privilegierte CPU-Befehle.
##### 2. User Mode (Nicht-privilegierter Modus)
  Anwendungsprogramme (wie Browser, Textverarbeitung oder Spiele) laufen standardmäßig im User-Mode.
   - **Zweck:** Ausführung von Benutzeranwendungen in einer isolierten Umgebung.
   - **Sicherheit:** Anwendungen haben keinen direkten Zugriff auf den Speicher anderer Programme oder die Hardware. Ein Absturz betrifft in der Regel nur die einzelne Anwendung, nicht das gesamte System.
   - **Einschränkung:** Um Hardware-Ressourcen zu nutzen, muss die Anwendung eine Anfrage an den Kernel stellen.


### System Call:
Da Anwendungen im User-Mode nicht direkt auf die Hardware zugreifen dürfen, nutzen sie sogenannte System Calls (Systemaufrufe).
- **Anforderung:** Eine App möchte eine Datei speichern (User-Mode).
- **Umschaltung (Trap/Interrupt):** Ein Systemaufruf wird ausgelöst. Die CPU wechselt vom User-Mode in den Kernel-Mode.
- **Ausführung:** Das Betriebssystem validiert die Anfrage und führt den Schreibvorgang auf der Festplatte aus (Kernel-Mode).
- **Rückkehr:** Nach Abschluss wird die Kontrolle wieder an die Anwendung zurückgegeben und die CPU wechselt zurück in den User-Mode.


##### Vergleichstabelle

| Merkmal | User Mode | Kernel Mode |
| -------- | -------- | ------------ |
| **Zugriffsebene** | Eingeschränkt (Sandboxed) | Voller Zugriff auf Hardware & Speicher |
| **Adressraum** | Eigener virtueller Adressraum | Gemeinsamer System-Adressraum | 
| **Folge eines Fehlers** | Nur die Anwendung stürzt ab | Das gesamte System kann abstürzen |
| **Privilegien** | Niedrig | Hoch |
| **Beispiele** | Word, Chrome  | Dateisystem-Manager, Gerätetreiber |

##### Warum ist diese Trennung notwendig?
- **Schutz vor Fehlern:** Verhindert, dass ein fehlerhaftes Programm den Speicher eines anderen Programms überschreibt oder das System einfriert.
- **Sicherheit:** Verhindert, dass Schadsoftware direkt kritische Hardware-Befehle ausführt oder Passwörter aus dem geschützten Kernspeicher ausliest.
- **Abstraktion:** Entwickler müssen nicht wissen, wie man jeden einzelnen Festplattentyp anspricht; sie rufen einfach eine standardisierte Funktion des Kernels auf.
