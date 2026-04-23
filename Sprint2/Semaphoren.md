## Semaphoren
Semaphoren sind ein Konzept, um den Zugriff von mehreren Threads auf gemeinsam genutzte Ressoucen zu koordinieren.
Ein Semaphor, besteht aus einem Zähler und einer Schlange, sowie den Methoden Warten() und Freigeben(). Wenn ein Thread auf eine Ressource, die mit einem Semaphor geschützt ist zugreifen möchte, so muss dieser die Methode Warten() aufrufen. Anschließend wird überprüft, ob die Ressource frei ist. Dazu wird der Zähler um 1 reduziert. Sollte dieser negativ sein, weil bereits ein anderer Thread die Ressource nutzt, muss der Thread sich in die Warteschlange einreihen. Der andere Thread der bereits arbeitet, ruft am Ende seines Prozesses die Methode Freigeben auf. Diese erhöht den Zähler um 1 und der nächste Prozess in der Schlange beginnt zu arbeiten.

Man unterscheidet zwischen zwei Arten von Semaphoren:
- Binärsemaphoren
	- Der Zähler wird am Anfang auf den Wert 1 gesetzt. Es kann immer nur 1 Prozess auf die Ressource zugreifen
- Zählsemaphoren
	- Der Zähler wird am Anfang auf einen bestimmten positiven Wert gesetzt. Abhängig des Wertes, können entsprechend viele Threads parallel auf die Ressource zugreifen(Bsp. CPU mit mehreren Kernen)

Das erhöhen und verringern des Zählerwerts muss durch atomare Operationen geschehen, also können die Operationen nur von einem Prozess auf einmal aufgerufen und durchlaufen wrden, ansonsten könnte es zu Inkonsistenzen beim Lesen und Schreiben kommen. Dazu ist eine Unterstützung durch den Prozesser zwingend erforderlich, da nur dieser echte atomare Operationen implementieren kann, welche anschließend über das Betriebssystem bereitgestellt werden.
Es kann sowohl passives als auch aktives Warten eingesetzt werden

Quelle: Schulbuch S. 210-212; S. 213 "roter Kasten"; https://de.wikipedia.org/wiki/Semaphor_(Informatik)

