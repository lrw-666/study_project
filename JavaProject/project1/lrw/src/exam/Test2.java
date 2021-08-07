package exam;

public class Test2 {
    public static void main(String[] args) {
        MyThread myThread = new MyThread();
        Thread thread = new Thread(myThread);
        thread.start();
    }
}

class MyThread implements Runnable{
    @Override
    public void run() {
        System.out.println("hello thread");
    }
}
