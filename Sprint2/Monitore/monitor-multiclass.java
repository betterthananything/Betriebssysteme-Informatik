// 1. Der Monitor
class Konto {

    private int kontostand = 0;

    public synchronized void einzahlen(int betrag) {
        kontostand += betrag;
        System.out.println("Eingezahlt: " + b + " | Stand: " + kontostand);
        notifyAll();
    }

    public synchronized void abheben(int betrag) {
        while (kontostand < betrag) {
            try {
                wait();
            } catch (InterruptedException e) {}
        }
        kontostand -= betrag;
        System.out.println("Abgehoben: " + betrag + " | Stand: " + kontostand);
    }
}

// 2. Klasse: Der Erzeuger
class Arbeitgeber implements Runnable {

    private Konto k;

    public Arbeitgeber(Konto k) {
        this.k = k;
    }

    public void run() {
        while (true) {
            k.einzahlen(50); // zahlt alle 2s, 50 € ein
            try {
                Thread.sleep(2000); // pausiert 2s
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                break;
            }
        }
    }
}

// 3. Klasse: Der Verbraucher
class Arbeitnehmer implements Runnable {

    private Konto k;

    public Arbeitnehmer(Konto k) {
        this.k = k;
    }

    public void run() {
        while (true) {
            /*
            versucht Geld abzuheben -> erst möglich wenn mindestens 100 € eingezahlt
            -> Thread wird schlafen gelegt bis er von einzahlen() geweckt wird
            und anschließend die Bedingung in abheben() erfüllt ist
            */
            k.abheben(100);
        }
    }
}
