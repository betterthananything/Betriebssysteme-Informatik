# Probleme bei der Nutzung gemeinsamer Ressourcen
In modernen Betriebssystemen ist die Trennung von Privilegienstufen essenziell, um die Stabilität und Sicherheit des Systems zu gewährleisten. Ohne diese Trennung könnte jedes Programm direkt auf die Hardware zugreifen, was zu Datenverlust, Systemabstürzen oder Sicherheitslücken führen würde.

## Kernel Mode vs. User Mode
Das Betriebssystem wechselt je nach Art der ausgeführten Aufgabe zwischen zwei Modi:
### 1. Kernel Mode (Privilegierter Modus)
   Im Kernel-Modus hat der ausführende Code uneingeschränkten Zugriff auf die zugrunde liegende Hardware und alle Speicheradressen.
   - **Zweck:** Ausführung von Betriebssystem-Kernfunktionen, Verwaltung von Hardware (CPU, RAM, Festplatten) und Steuerung von Treibern.
   - **Sicherheit:** Ein Absturz im Kernel-Modus ist kritisch und führt meist zu einem Systemstopp (z. B. dem „Blue Screen of Death“).
   - **Ressourcenzugriff:** Direkter Zugriff auf I/O-Geräte und privilegierte CPU-Befehle.



| Vorteile | Nachteile |
| -------- | --------- |
| **Voller Hardwarezugriff:** Erforderlich für Aufgaben wie Geräteverwaltung und Speicherzuweisung | **Hohes Risiko eines Systemabsturzes:** Fehler oder Bugs können das gesamte Betriebssystem zum Absturz bringen |
| **Effiziente Ressourcenverwaltung:** CPU-Zeit, RAM und I/O-Geräte können direkt verwaltet werden | **Sicherheitslücken:** Ein einziger fehlerhafter Kernel-Treiber kann das System gefährden |
| **Individuelle Optimierung:** Betriebssystementwickler können das System hinsichtlich Leistung oder Hardware feinabstimmen | **Komplexe Entwicklung:** Erfordert fundierte Kenntnisse der Betriebssystem-Interna
| **Geringer Overhead:** Systemaufrufe und Prozessverwaltung werden effizient abgewickelt | |
| **Erweiterte Ablaufsteuerung:** Steuert Multitasking, Thread-Synchronisation und Kontextwechsel | |


### 2. User Mode (Nicht-privilegierter Modus)
  Anwendungsprogramme (wie Browser, Textverarbeitung oder Spiele) laufen standardmäßig im User-Mode.
   - **Zweck:** Ausführung von Benutzeranwendungen in einer isolierten Umgebung.
   - **Sicherheit:** Anwendungen haben keinen direkten Zugriff auf den Speicher anderer Programme oder die Hardware. Ein Absturz betrifft in der Regel nur die einzelne Anwendung, nicht das gesamte System.
   - **Einschränkung:** Um Hardware-Ressourcen zu nutzen, muss die Anwendung eine Anfrage an den Kernel stellen.


     | Vorteile | Nachteile |
     | -------- | --------- |
     | **Leichteres Debugging:** Fehler bleiben auf einzelne Anwendungen beschränkt | **Leistungsaufwand:** Systemaufrufe erfordern einen Wechsel zwischen Benutzer- und Kernel-Modus, was zu Latenz führt und die Leistung beeinträchtigt |
     | **Abgrenzung von Abstürzen:** Nur die abstürzende Anwendung ist betroffen | **Eingeschränkte Fähigkeiten:** Low-Level-Aufgaben können nicht ausgeführt werden |
     | **Prozessisolierung:** Eine Anwendung kann den Speicher einer anderen Anwendung weder lesen noch beschädigen | **Abhängigkeit vom Kernel:** Benutzerprogramme sind zur Ausführung wesentlicher Funktionen auf den Kernel angewiesen |
     | **Kontrollierter Zugriff:** Der Kernel prüft und autorisiert Anfragen | **Geringere Kontrolle für Entwickler:** Der Zugriff auf den Speicher und die Ausführung sind eingeschränkt |
     | **Stabilität und Zuverlässigkeit:** Anwendungen können den Kernel oder andere Prozesse nicht direkt beeinflussen, was das Risiko von Systemabstürzen verringert | |
     | **Sicherheit:** Der direkte Zugriff auf kritische Ressourcen wird blockiert, wodurch unbefugte Nutzung verhindert wird | |


![](https://imgv2-1-f.scribdassets.com/img/document/680035952/original/53e23f9106/1?v=1)



## System Call:
Da Anwendungen im User-Mode nicht direkt auf die Hardware zugreifen dürfen, nutzen sie sogenannte System Calls (Systemaufrufe).
- **Anforderung:** Eine App möchte eine Datei speichern (User-Mode).
- **Umschaltung (Trap/Interrupt):** Ein Systemaufruf wird ausgelöst. Die CPU wechselt vom User-Mode in den Kernel-Mode.
- **Ausführung:** Das Betriebssystem validiert die Anfrage und führt den Schreibvorgang auf der Festplatte aus (Kernel-Mode).
- **Rückkehr:** Nach Abschluss wird die Kontrolle wieder an die Anwendung zurückgegeben und die CPU wechselt zurück in den User-Mode.

![](https://phoenixnap.com/kb/wp-content/uploads/2023/08/system-call-steps-execution.png)


##### Warum ist diese Trennung notwendig?
- **Schutz vor Fehlern:** Verhindert, dass ein fehlerhaftes Programm den Speicher eines anderen Programms überschreibt oder das System einfriert.
- **Sicherheit:** Verhindert, dass Schadsoftware direkt kritische Hardware-Befehle ausführt oder Passwörter aus dem geschützten Kernspeicher ausliest.
- **Abstraktion:** Entwickler müssen nicht wissen, wie man jeden einzelnen Festplattentyp anspricht; sie rufen einfach eine standardisierte Funktion des Kernels auf.
