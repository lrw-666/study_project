package hncu;

public class MyThread implements Runnable{
    private static int number = 80;
    Object lock = new Object();
    public void run (){
        while(number>0){
            synchronized (lock){
                if(number>0){
                    try {
                        Thread.sleep(10);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                    System.out.println(Thread.currentThread().getName() + "正在分发第" + number-- + "份笔记");
                }
            }
            // dispatchNotes();
            Thread.yield();
        }
    }

    private synchronized void dispatchNotes(){
        if(number>0){
            try {
                Thread.sleep(10);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println(Thread.currentThread().getName() + "正在分发第" + number-- + "份笔记");
        }
    }
}
