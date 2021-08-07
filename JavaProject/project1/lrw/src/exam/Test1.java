package exam;

import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class Test1 {
    public static void main(String[] args) throws IOException {
        writeFile();
    }

    public static void writeFile() throws IOException {
        FileOutputStream stream = new FileOutputStream("D:\\example.txt", true);
        stream.write("务实创新".getBytes());
        stream.close();
    }
}
