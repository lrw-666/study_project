package hncu;

public class SumThread extends Thread{
    private static int sum=0;
    int number;
    public SumThread(int number) {
        this.number = number;
    }
    public void run(){
        for(int i=0;i<10;i++){
             add(i);
        }
    }

    private synchronized void add(int i){
        sum += (number+i);
    }

    public static void main (String[] args) throws InterruptedException {
        Thread[] threads = new Thread[10];
        for(int i=0;i<10;i++){
            threads[i] = new SumThread(i*10+1);
            threads[i].start();
        }
        Thread.sleep(5000);
        System.out.println(sum);
    }
}
