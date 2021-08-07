package exam;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class test4 {
    public static void main(String[] args) throws IOException {
        FileWriter writer = new FileWriter("reader.txt");
        writer.write("itcast");
        FileReader reader = new FileReader("reader.txt");
        int len;
        char[] str = new char[1024];
        while((len=reader.read(str))!=-1){
            System.out.println(str);
        }
        writer.close();
        reader.close();
    }
}
