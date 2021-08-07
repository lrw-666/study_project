package hncu;

public class DieLock extends Thread{
    private boolean flag;

    public DieLock(Boolean flag){
        this.flag = flag;
    }

    @Override
    public void run() {
        if(flag){
            synchronized (MyLock.objA){
                System.out.println("if objA");
                synchronized (MyLock.objB){
                    System.out.println("if objB");
                }
            }
        }else {
            synchronized (MyLock.objB){
                System.out.println("else objB");
                synchronized (MyLock.objA){
                    System.out.println("else objA");
                }
            }
        }

    }
}

class MyLock {
    //创建两把锁
    public static final Object objA = new Object();
    public static final Object objB = new Object();
}

class DieLockDemo {
    public static void main(String[] args) {
        DieLock dl1 = new DieLock(true);
        DieLock dl2 = new DieLock(false);

        dl1.start();
//        try {
//            Thread.sleep(1000);
//        } catch (InterruptedException e) {
//            e.printStackTrace();
//        }
        dl2.start();
    }
}