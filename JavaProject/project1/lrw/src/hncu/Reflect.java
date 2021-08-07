package hncu;

import java.lang.reflect.Constructor;

public class Reflect {
    public static void main(String[] args) throws Exception {
        Student lrw = new Student("lrw", "19", "男");
        Student lqx = new Student("lqx", "20", "男");
        Class class1 = lrw.getClass();
        Class class2 = lqx.getClass();
        Class class3 = Class.forName("hncu.Student"); // 注意路径用点来间隔

//        System.out.println(class1 == class2);
//        System.out.println(lrw == lqx);
//        System.out.println(class1 == class3);

        Class c = Student.class;
        Constructor constructor = c.getDeclaredConstructor(Student.class);
        constructor.setAccessible(true); // 暴力访问

    }
}
