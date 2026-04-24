class Konto {

    private int kontostand = 100;

    // Die Methode ist durch 'synchronized' geschützt (Monitor-Sperre)
    public synchronized void einzahlen(int betrag) {
        kontostand += betrag;
        // Weckt alle Threads, die bei abheben() gewartet haben
        notifyAll();
    }

    public synchronized void abheben(int betrag) {
        while (kontostand < betrag) {
            try {
                // Thread gibt Monitor frei und wartet in der Condition Queue
                wait();
            } catch (InterruptedException e) {
                Thread.currentThread.interrupt();
            }
        }
        kontostand -= betrag;
    }

    public synchronized int getStand() {
        return kontostand;
    }
}
