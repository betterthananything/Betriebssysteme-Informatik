## Scheduling Strategien 

### **Round Robin**
In der Round Robin Scheduling Strategie rotiert das System (OS) durch jeden anstehenden Prozess und gibt ihnen allen die gleiche Anzahl an Zeit, genannt *Quantum Time*, zur Verfügung. Dabei wird nicht auf Priorität geachtet. 

#### Beispiel 1: Prozesse mit gleichzeitigem Ankommen
| Process | Burst Time | Arrival Time |
|---------|------------|--------------|
| P1 | 4 ms | 0 ms |
| P2 | 5 ms | 0 ms |
| P3 | 3 ms | 0 ms |

**Step-by-Step:**
1. Time 0-2 (P1): P1 läuft für 2 ms (Gesamte Zeit Übrig: 2 ms)
2. Time 2-4 (P2): P2 läuft für 2 ms (Gesamte Zeit Übrig: 3 ms)
3. Time 4-6 (P3): P3 läuft für 2 ms (Gesamte Zeit Übrig: 1 ms)
4. Time 6-8 (P1): P1 beendet seine letzten 2 ms
5. Time 8-10 (P2): P2 läuft für nochmal 2 ms (Gesamte Zeit Übrig: 1 ms)
6. Time 10-11 (P3): P3 beendet seine letze 1 ms
7. Time 11-12 (P2): P2 beendet seine letzte 1 ms

#### Beispiel 2: Prozesse mit unterschiedlichem Ankommen
| Process | Burst Time (BT) | Arrival Time (AT) |
|---------|------------|--------------|
| P1 | 5 ms | 0 ms |
| P2 | 2 ms | 4 ms |
| P3 | 4 ms | 5 ms |

**Step-by-Step:**
1. Time 0-2 (P1 führt aus):
    - P1 fängt Ausführung an als es bei 0 ms ankommt
    -  Läuft für 2 ms; restliche BT = 5 - 2 = 3 ms
    - Ready Queue: P1

2. Time 2-4 (P1 führt nochmal aus):
    - P1 führt weiter aus, da noch kein anderer Prozess angekommen ist
    - Läuft für 2 ms; restliche BT = 3 - 2 = 1 ms
    - P2 kommt bei 4 ms an
    - Ready Queue: P2, P1

3. Time 4-6 (P2 führt aus):
    - P2 fängt Ausführung an, als es bei 4 ms ankommt
    - Läuft für 2 ms; restliche BT = 2 - 2 = 0 ms
    - P2 ist fertig
    - P3 kommt bei 5 ms an
    - Ready Queue: P1, P3

4. Time 6-7 (P1 führt aus):
    - P1 fängt Ausführung an
    - Läuft für 1 ms; restliche BT = 1 - 1 = 0 ms
    - Ready Queue: P3

5. Time 7-9 (P3 führt aus):
    - P3 fängt Ausführung an
    - Restliche BT = 4 - 2 = 2 ms
    - Ready Queue: P3
  
6. Time 9-11 (P3 führt nochmal aus):
    - P3 fährt fort und läuft für 2 ms und beedet seine Ausführung
    - Restliche BT = 2 - 2 = 0 ms
    - Ready Queue: 

#### Vorteile: 
- Jeder Prozess kriegt die gleiche Menge an CPU
- Der Algorithmus ist einfach zu implementieren und verstehen
- Kann mehrere Prozesse gleichzeitig ohne große Verzögerungen bewältigen 

#### Nachteile:
- Großer Overhead, wenn der Quantum (Quantum Time) zu klein ist
- Fühlt sich langsam an, wenn der Quantum zu groß ist
  
---------------

### **Shortest-Job-First (SJF)**
Wie der Name schon sagt, wird der kürzester Prozess, also der Prozess mit der wenigsten BT, ausgeführt.  

Dabei ist das erste Problem schon, dass das System nicht die BT's der einzelnen Prozesse weiß, weswegen es nur in spezifischen Situationen verwendet werden kann, wo die BT bekannt ist.  

Um zu vermeiden, dass immer mehr kürzere Prozess kommen und die längeren ignoriert werden, muss man aging implementieren. 

#### Vorteile:
- Besser als FCFS, weil es die durchschnittliche Wartezeit verkürzt
- Gut in Situationen, wo die BT's bekannt sind

#### Nachteile:
- Kann zu starvation führen (siehe ageing)
- BT zu berechnen ist schwer
