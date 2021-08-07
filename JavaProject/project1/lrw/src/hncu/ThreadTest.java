package hncu;

public class ThreadTest {
    public static void main(String[] args) {
        MyThread myThread = new MyThread();
        Thread thread1 = new Thread(myThread, "老师1");
        Thread thread2 = new Thread(myThread,"老师2");
        Thread thread3 = new Thread(myThread, "老师3");
        thread1.start();
        thread2.start();
        thread3.start();

        // 设置和获取线程名称：setName(),getName()
        // 调度模型:分时调度模型、抢占式调度模型(主)

        // 设置优先级:setPriority(int n);  getPriority();
        // 线程休眠:Thread.sleep(1000); 阻塞线程
        // 线程让步:Thread.yield(); 就绪状态
        // 线程插队:join()
        // 只要有一个前台线程，这个程序就不会结束
        // 当前运行线程:Thread.currentThread()
        // 中断线程：stop()、interrupt()

        //同步代码块格式：synchronized(对象){需要同步的代码;}
        //同步方法：synchronized

        // 线程通信：wait()、notify()、notifyAll()
    }
}
