## Deadlocks
### Was ist ein Deadlock?
Ein Deadlock ist wenn 2+ Prozesse unendlich stuck sind weil sie auf gegenseitige Ressourcen warten. Dafür müssen 4 Bedingungen gleichzeitig erfüllt sein, die sogenannten Coffman Bedingungen.

### Coffman Bedingungen
**Gegenseitiger Ausschluss (mutual exclusion):**  
Eine Ressource kann nur von einem Prozess gleichzeitig verwendet werden, d.h. non-sharable resources.  

**Halten und Warten (hold and wait):**  
Ein Prozess "hält" mindestens eine Ressource und wartet um andere Ressourcen zu bekommen. In dieser Zeit gibt er nicht seine Ressourcen frei.

**Keine Verdrängung (No Preemption):**  
Ressourcen können nicht von einem Prozess nicht entzogen werden ohne Erlaubnis des Prozesses. Das Betriebssytem und andere Prozesse dürfen sie nicht wegnehmen um es einem anderen Prozess zuzuordnen.  

**Zyklisches Warten (circular wait):**  
Es entsteht eine Kette an Prozessen, die alle auf die Ressource von dem nächsten Prozess warten, der letzte dann auf die Ressource vom ersten, wodurch ein Zyklus entsteht.
