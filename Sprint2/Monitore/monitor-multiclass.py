import threading
import time


# 1. Der Monitor
class Konto:
    def __init__(self):
        self.kontostand = 0
        self.cond = threading.Condition()

    def einzahlen(self, betrag):
        with self.cond:
            self.kontostand += betrag
            print(f"Eingezahlt: {betrag} | Stand: {self.kontostand}")
            self.cond.notify_all()

    def abheben(self, betrag):
        with self.cond:
            while self.kontostand < betrag:
                self.cond.wait()
            self.kontostand -= betrag
            print(f"Abgehoben: {betrag} | Stand: {self.kontostand}")


# 2. Der Erzeuger
class Arbeitgeber(threading.Thread):
    def __init__(self, konto):
        super().__init__()
        self.konto = konto

    def run(self):
        while True:
            # zahlt alle 2s 50 € ein
            self.konto.einzahlen(50)
            time.sleep(2)


# 3. Der Verbraucher
class Arbeitnehmer(threading.Thread):
    def __init__(self, konto):
        super().__init__()
        self.konto = konto

    def run(self):
        while True:
            # versucht Geld abzuheben -> erst möglich wenn mindestens 100 € eingezahlt
            # -> Thread wird schlafen gelegt bis er von einzahlen() geweckt wird
            # und anschließend die Bedingung in abheben() erfüllt ist
            self.konto.abheben(100)
