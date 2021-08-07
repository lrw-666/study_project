package hncu;

import java.io.*;
import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class IOTest {
    public static void main(String[] args) throws Exception {
        File file = new File("F:\\projects\\JavaProject\\project1\\lrw\\src\\hncu\\test.txt");
        File file2 = new File("F:\\projects\\JavaProject\\project1\\lrw\\src\\hncu\\test1.txt");
        // FileInputStream与FileInputStream实现文件拷贝
//        FileInputStream inputStream = new FileInputStream(file);
//        FileOutputStream outputStream = new FileOutputStream(file2);
//        int len;
//        byte[] str = new byte[1024];
//        while((len = inputStream.read(str))!=-1){
//            outputStream.write(str, 0, len);
//        }
//        inputStream.close();
//        outputStream.close();

        // FileReader与FileWriter拷贝文件
//        FileReader reader = new FileReader(file);
//        FileWriter writer = new FileWriter(file2);
//        BufferedReader reader1 = new BufferedReader(reader);
//        BufferedWriter writer1 = new BufferedWriter(writer);
//        String str;
//        while((str=reader1.readLine())!=null){
//            writer1.write(str);
//            writer1.newLine();
//        }
//        reader1.close();
//        writer1.close();

        // 键盘输入
//        Scanner scanner = new Scanner(System.in);
//        String s;
//        for(int i=0;i<5;i++){
//            s = scanner.next();
//            if(s.equals("123456")){
//                System.out.println("恭喜你已经成功进入游戏！");
//                scanner.close();
//                System.exit(0);
//            }else{
//                System.out.println("密码错误");
//            }
//        }
//        scanner.close();
//        System.out.println("密码错误，结束游戏");
//        System.exit(0);

        // BufferReader对字符流包装
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        for(int i=0;i<5;i++){
            String line = reader.readLine();
            if(line.equals("123456")){
                System.out.println("恭喜你进入游戏");
                reader.close();
                System.exit(0);
            }
        }
        System.out.println("密码错误，结束游戏！");
        System.exit(0);

        /*
        如何实现数据的换行?
            写数据的时候，写入换行符。
            如何写入换行符？
                不同的操作系统有不同的换行符。
                    windows:\r\n
                    Linux:\n

        如何实现数据的追加写入?
            FileOutputStream(File file, boolean append)
            FileOutputStream(String name, boolean append)
                实现方式只要把append设置为true就可以了
         */

        /*
            字节缓冲输出流
                BufferedOutputStream(OutputStream out)
                BufferedOutputStream(OutputStream out, int size)：一般不用这个构造方法。默认缓冲区已经足够我们使用了
             public void flush():刷新此缓冲的输出流。这迫使所有缓冲的输出字节被写出到底层输出流中。（写文件需要）
         */


        /*
         从文本文件中读取数据(每一行为一个字符串数据)到集合中，并遍历集合.
         */
        //封装数据源
        BufferedReader br = new BufferedReader(new FileReader("a.txt"));
        //封装目的地
        ArrayList<String> list = new ArrayList<>();
        String line = null;
        while ((line = br.readLine())!=null){
            list.add(line);
        }
        br.close();
        for (String s : list) {
            System.out.println(s);
        }

        /*
            随机点名器
         */
        //封装数据源
//        BufferedReader br = new BufferedReader(new FileReader("1906806.txt"));
//        //封装目的地
//        ArrayList<String> list = new ArrayList<String>();
//        String line = null;
//        while ((line = br.readLine()) != null){
//            list.add(line);
//        }
//        br.close();
//        //产生一个随机数
//        Random random = new Random();
//        int index = random.nextInt(list.size());
//        //根据随机数获取学生名字
//        String name = list.get(index);
//        System.out.println("请" + name + "回答问题");
    }
}
