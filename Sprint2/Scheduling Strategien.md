## Scheduling Strategien 

### **Round Robin**
In der Round Robin Scheduling Strategie rotiert das System (OS) durch jeden anstehenden Prozess und gibt ihnen allen die gleiche Anzahl an Zeit, genannt *Quantum Time*, zur Verfügung. Dabei wird nicht auf Priorität geachtet. 

#### Beispiel 1: Prozesse mit gleichzeitigem Ankommen
| Process | Burst Time | Arrival Time |
|---------|------------|--------------|
| P1 | 4 ms | 0 ms |
| P2 | 5 ms | 0 ms |
| P3 | 3 ms | 0 ms |

**Step-by-Step**:
1. Zeit 0-2 (P1): P1 läuft für 2 ms (Gesamte Zeit Übrig: 2 ms).
2. Zeit 2-4 (P2): P2 läuft für 2 ms (Gesamte Zeit Übrig: 3 ms).
3. Zeit 4-6 (P3): P3 läuft für 2 ms (Gesamte Zeit Übrig: 1 ms).
4. Zeit 6-8 (P1): P1 beendet seine letzten 2 ms.
5. Zeit 8-10 (P2): P2 läuft für nochmal 2 ms (Gesamte Zeit Übrig: 1 ms).
6. Zeit 10-11 (P3): P3 beendet seine letze 1 ms.
7. Zeit 11-12 (P2): P2 beendet seine letzte 1 ms.
