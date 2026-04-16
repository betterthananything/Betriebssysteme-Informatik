# Das Schalenmodell

* Das Schalenmodell beschreibt die hierarchische Struktur eines Betriebssystems
* Es verdeutlicht, wie die verschiedenen Bestandteile die Hardware abstrahieren, um dem Nutzer eine bedienbare Oberfläche zu bieten.

![Schalenmodell](image.png)

---

## Schichten

* **Hardware (Kern)**
    * Die unterste Ebene, bestehend aus physischen Komponenten wie CPU, RAM und Peripheriegeräten

* **Kernel (Betriebssystemkern)**
    * Der **Kernel** ist die innerste Software-Schicht
    * Er hat direkten Zugriff auf die Hardware und verwaltet die zentralen Aufgaben wie das **Prozessmanagement** und die **Speicherverwaltung**
    * Er verteilt die Ressourcen der Hardware an die darüberliegenden Schichten

* **Driver (Gerätetreiber)**
    * **Driver** bilden die Verbindungsschicht zwischen dem Kernel und spezifischer Hardware

* Sie übersetzen allgemeine Befehle des Betriebssystems in die spezifische „Sprache“ des jeweiligen Geräts

* **Dateisystem (File System)**
    * Das **Dateisystem** liegt über dem Kernel und organisiert die logische Struktur der Daten
    * Es ermöglicht das **Dateimanagement**, also das Erstellen, Speichern und Verwalten von Verzeichnissen

* **Shell (Benutzerschnittstelle)**
    * Die **Shell** ist die äußerste Schicht des Betriebssystems
    * Sie dient als Schnittstelle zum Anwender, entweder grafisch (**GUI**) oder textbasiert (**CLI**)
    * Hier werden Nutzerbefehle entgegengenommen und an den Kernel weitergeleitet

* **Anwendungssoftware (Applications)**
    * Programme wie Browser oder Textverarbeitung laufen „außerhalb“ des eigentlichen Betriebssystems und nutzen dessen Dienste
