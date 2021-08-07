package hncu;

public class Accumulator extends Thread {
    private final int stratNum;
    public static int sum;
    public Accumulator(int startNum) {
        this.stratNum = startNum;
    }
    public static synchronized void add(int num) {
        sum += num;
    }
    public void run() {
        int sum = 0;
        for (int i = 0; i < 10; i++) {
            sum += stratNum + i;
        }
        add(sum);
    }
    public static void main(String[] args) throws Exception {
        Thread[] threadList = new Thread[10];
        for (int i = 0; i < 10; i++) {
            threadList[i] = new Accumulator(10 * i + 1);
            threadList[i].start();
        }
        Thread.sleep(5000);
        System.out.println("Sum is : " + sum);
    }
}