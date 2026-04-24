## Deadlocks
### Was ist ein Deadlock?
Ein Deadlock ist wenn 2+ Prozesse unendlich stuck sind, weil sie auf gegenseitige Ressourcen warten. Dafür müssen 4 Bedingungen gleichzeitig erfüllt sein; die sogenannten Coffman-Bedingungen.

### Coffman-Bedingungen
**Gegenseitiger Ausschluss (mutual exclusion):**  
Eine Ressource kann nur von einem Prozess gleichzeitig verwendet werden (non-sharable resources) 

**Halten und Warten (hold and wait):**  
Ein Prozess "hält" mindestens eine Ressource und wartet um andere Ressourcen zu bekommen. In dieser Zeit gibt er nicht seine Ressourcen frei.

**Keine Verdrängung (No Preemption):**  
Ressourcen können nicht ohne Erlaubnis des Prozesses von einem Prozess entzogen werden. Das Betriebssytem und andere Prozesse dürfen sie nicht wegnehmen, um es einem anderen Prozess zuzuordnen.
