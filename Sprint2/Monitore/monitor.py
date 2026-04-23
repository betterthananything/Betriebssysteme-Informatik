import threading


# Beispiel mit Lock-Objekt
class Konto1:
    def __init__(self):
        self.kontostand = 100
        self.monitor_lock = threading.Lock()

    def einzahlen(self, betrag):
        # Der Bereich innerhalb von 'with' ist Teil
        # des kritischen Abschnitts (vom Monitor geschützt)
        with self.monitor_lock:
            self.kontostand += betrag

    def abheben(self, betrag):
        with self.monitor_lock:
            self.kontostand -= betrag

    def get_kontostand(self):
        with self.monitor_lock:
            return self.kontostand


# Beispiel mit Condition-Objekt (beinhaltet Lock-Objekt bereits)
class Konto2:
    def __init__(self):
        self.kontostand = 100
        self.condition = threading.Condition()

    def einzahlen(self, betrag):
        with self.condition:
            self.kontostand += betrag
            # Benachrichtigt wartende Threads
            self.condition.notify_all()

    def abheben(self, betrag):
        with self.condition:
            # Warten, bis Kontostand ausreicht
            while self.kontostand < betrag:
                self.condition.wait()
            self.kontostand -= betrag

    def get_kontostand(self):
        with self.condition:
            return self.kontostand
