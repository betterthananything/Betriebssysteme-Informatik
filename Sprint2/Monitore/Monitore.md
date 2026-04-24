# Monitore

## Konzept

Ein Monitor ist ein grundlegendes Konzept zur **Synchronisation von Prozessen oder Threads**. Er dient dazu, den **Zugriff auf gemeinsam genutzte Ressourcen zu steuern**, sodass keine Konflikte auftreten.

Genauso wie Semaphore wird ein Monitor genutzt um die **Race Condition** zu verhindern.

Ein Monitor ist wie eine Art Raum, der nur von einer Person (bzw. Thread) gleichzeitig betreten werden darf.

### Kernkonzepte eines Monitors

Ein Monitor besteht grundlegend aus drei Komponenten:
1. **Daten**: Die privaten Daten, die geschützt werden.
2. **Methoden**: Die Methoden, die exklusiv auf diese Daten zugreifen können.
3. **Implizite Sperre**: Maximal ein Thread darf sich gleichzeitig im Monitor befinden und seine Methoden ausführen.

### Funktionsweise eines Monitors

- **Eintritt**: Ein Thread ruft eine Methode des Monitors auf. Ist kein anderer Thread im Monitor, so kann er "eintreten" und die Methode ausführen.
- **Wechselseitiger Ausschluss**: Ist ein Thread in einem Monitor, so wird er gesperrt. Jede Thread, der jetzt eintreten will, landet auf einer Warteschlange.
- **Bedingungsvariablen**: Manchmal muss ein Thread innerhalb eines Monitors warten bis eine Bedingung erfüllt ist. Er wird in einen Sleep-Zustand versetzt. Der Monitor ist dann vorübergehen frei, bis die Bedingung erfüllt ist und der Thread "geweckt" wird.

### Warteschlangen und Signalisierung

Wichtig ist, dass es einen Unterschied zwischen **Eingangswarteschlange** und **Bedingungswarteschlange** gibt:
* **Eingangswarteschlange (Entry Queue)**: Hier warten Threads, die den Monitor überhaupt erst betreten wollen.
* **Bedingungswarteschlange (Condition Queue)**: Hier warten Threads, die bereits im Monitor waren, aber schlafen gelegt wurden, weil eine Bedingung nicht erfüllt war.

Zudem gibt es einen Unterschied, was passiert, wenn ein Thread einen anderen "aufweckt":
* **Signal-and-Continue**: Der weckende Thread arbeitet erst zu Ende, der geweckte Thread kommt in die Warteschlange und darf erst rein, wenn der Monitor wieder frei ist.
* **Signal-and-Urgent-Wait**: Der weckende Thread gibt sofort den Vortritt an den geweckten Thread.

### Unterschiede zu Semaphoren

|Merkmal|Monitor|Semaphor|
|-------|-------|--------|
|Abstraktion|Höheres Programmierkonzept (Objektorientiert)|Betriebssystemebene|
|Kapselung|Daten und Synchronisation sind eine Einheit|Synchronisation ist manuell zu steuern|
|Fehleranfälligkeit|Geringer, da der Compiler/Laufzeitumgebung viel übernimmt|Höher, da mehr manuelle Steuerung|

## Anwendung

### Monitore im Code

* Kritischer Abschnitt im Code betrifft oft mehrere Methoden innerhalb einer Klasse  
* Alle Bestandteile des kritischen Abschnitts müssen erkannt und gekennzeichnet werden  
* Kennzeichnung erfolgt durch Keywords, um wechselseitigen Ausschluss zu garantieren  
* Vermeidung unübersichtlicher Semaphorenanzahl  
* Synchronisation der Threads erfolgt während der Ausführung im Hintergrund

### Code-Snippets

In [monitor.java](monitor.java) und [monitor.py](monitor.py) sind Code-Snippets, in denen jeweils eine Klasse als Monitor implementiert ist.

In [monitor-multiclass.java](monitor-multiclass.java) und [monitor-multiclass.py](monitor-multiclass.py) sind Code-Snippets, in denen jeweils drei Klassen implementiert sind, je ein Monitor, ein Verbraucher und ein Entnehmer.

In Python wird ein **Lock- bzw. Condition-Objekt** verwendet, um den Monitor zu realisieren. 
In Java kann jedes Klasse nativ als Monitor fungieren. Das Schlüsselwort ```synchronized``` fügt eine Methode zum **kritischen Abschnitt** der Klasse hinzu, um **wechselseitigen Ausschluss** zu ermöglichen.
