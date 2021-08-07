package hncu;

import java.io.File;

public class FileTest {
    public static void main(String[] args) {
        // 文件与目录
        File file1 = new File("D:\\test\\a.java");
        File file2 = new File("D:\\test","a.java");
        File file3 = new File("D:\\test");
        File file4 = new File(file3,"a.java");

        // 创建功能
        /*
        public boolean createNewFile():创建文件，如果创建成功返回True,否则，返回False
        public boolean mkdir()：创建单级目录，如果创建成功返回True,否则，返回False.
        public boolean mkdirs()：创建多级目录，如果创建成功返回True,否则，返回False

        说明：创建单级目录时mkdir()和mkdirs()完全等价
              如果要直接创建多级目录，只能使用mkdirs()
         */
        //需求：我要在D:\test目录下创建一个a.txt
//        File file = new File("D:/test/a.txt");
//        System.out.println(file.createNewFile());

//        //需求：我要在D:\\test目录下创建一个文件夹a
//        File file1 = new File("D:/test/a");
//        //System.out.println(file1.mkdir());
//        System.out.println(file1.mkdirs());

        //需求：我要在D:\\test目录下创建一个文件夹a，文件夹a中又有一个文件夹b
        File file5 = new File("D:/test/a/b");
        //System.out.println(file1.mkdir());
        System.out.println(file1.mkdirs());

        // 删除功能
        /*
        public boolean delete():
            删除一个文件，如果删除成功，返回True,否则返回false
            删除一个目录，如果删除成功，返回True,否则返回false。
            注意：如果用这个方法删除一个目录，那么目录中不能有任何内容。
         */
        //需求：我要删除D:/test/a.txt
//        File file = new File("D:/test/a.txt");
//        System.out.println( file.delete());

        //需求：我要删除D:/test/aa目录
//        File file1 = new File("D:/test/aa");
//        System.out.println(file1.delete());

        //需求：我要删除D:/test/a目录
        File file6 = new File("D:/test/aa");
        System.out.println(file1.delete());//删除失败，要先删除b目录，再删除a目录

        // 重命名功能
        /*
        public boolean renameTo(File dest):
            如果路径名相同，这个方法就是重命名
            如果路径名不同，这个方法就是剪切并重命名
         */
        //创建文件时，如果没有写路径名，默认的路径名是在当前工程的目录下。
        File file = new File("a.txt");
//        file.createNewFile();
        //File newFile = new File("b.txt");
        File newFile = new File("D:/test/bbb.txt");
        file.renameTo(newFile);

        // 判断功能
        /*
        public boolean isDirectory():判断是否是目录
        public boolean isFile()：判断是否是文件
        public boolean exists()：判断是否存在
        public boolean canRead()：判断是否可读
        public boolean canWrite()：判断是否可写
        public boolean isHidden()：判断是否隐藏
         */

        // 基本获取功能
        /*
        public String getAbsolutePath():获取绝对路径(路径是从盘符开始，一级级表示出来的)
        public String getPath()：获取相对路径（相对于我的项目工程的路径）
        public String getName()：获取名称
        public long length()：获取长度，单位：字节
        public long lastModified()：获取最后修改时间
         */

        // 高级获取功能
        /*
        public String[] list():获取指定目录下所有文件或文件夹的名称数组
        public File[] listFiles()：获取指定目录下所有文件或文件夹的File数组
         */

        // 文件名称过滤器
        /*
        需求：判断D:/test目录下是否有后缀名为.java的文件，如果有，输出文件的名称
        public String[] list(FilenameFilter filter)
        public File[] listFiles(FilenameFilter filter)
         */


    }
}
