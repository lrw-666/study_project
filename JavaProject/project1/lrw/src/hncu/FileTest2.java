package hncu;

import java.io.File;
import java.io.FilenameFilter;

public class FileTest2 {
    public static void main(String[] args) {
        // 判断目录下是否有后缀名为.java的文件，如果有，输出文件的名称
        File file7 = new File("F:\\projects\\JavaProject\\project1\\lrw\\src\\hncu");
//        File[] files = file7.listFiles();
//        if(files==null){
//            return;
//        }
//        for(File f: files){
//            if(f.isFile()){
//                if(f.getName().endsWith(".java")){{
//                    System.out.println(f.getName());
//                }}
//            }
//        }

        // 文件名称过滤器
        String[] list = file7.list(new FilenameFilter() {
            @Override
            public boolean accept(File dir, String name) {
                // 如果返回true,指定文件就会包含在list列表中，如果返回false，指定文件就不会包含在列表中
                File file = new File(dir, name);
                return file.isFile() && file.getName().endsWith(".java");
            }
        });
        for(String str: list){
            System.out.println(str);
        }
    }
}
