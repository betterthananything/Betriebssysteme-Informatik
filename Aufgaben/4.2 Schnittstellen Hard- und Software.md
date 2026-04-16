## Schnittstellen Hard Software
Eine Schnittstelle(Interface) ist eine Möglichkeit, für zwei Systeme bzw. Komponenten zu kommunizieren. Daher gibt es mehrere Arten von Schnittstellen. Wir betrachten die Software- und Hardwareschnittstelle.

### *Hintergund*
Die CPU hat 2 Arbeitsmodi. Den **Kernelmode** und den **Usermode**. Im Kernelmode stehen alle CPU Befehle zur Verfügung, wobei i.d.r. ausschließlich der Kernel im Kernelmode arbeitet. Im Usermode hingegen, stehen Funktionen wie direkter Speicherzugriff und direkter Zugriff auf die Hardware nicht zur Verfügung.


### Driver und Schnittstellen
Möchte nun ein Programm das im Usermode arbeitet, auf eine Hardware Komponente zugreifen. So muss es einen sog. **Systemcall** (Syscall) machen. Wenn ein Programm einen Syscall aufruft, wird das Programm gehalten und der Kernel führt die Funktion aus. Wenn der Kernel den Call durchgeführt hat, wird das Programm wieder durchgeführt.

Quelle: Schulbuch Q12 S. 242/243
