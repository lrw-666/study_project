package hncu;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;

public class TCPClient {
    public static void main(String[] args) throws IOException {
        // 创建Socket连接到指定的服务器端
        Socket socket = new Socket("127.0.0.1", 8888);

        // 发送消息
        OutputStream outputStream = socket.getOutputStream();
        String message = "你好，成功了，哈哈哈！";
        outputStream.write(message.getBytes());
        socket.shutdownOutput(); // 关闭输出流

        // 获取返回值
        InputStream inputStream = socket.getInputStream();
        byte[] bytes = new byte[1024];
        int len=inputStream.read(bytes); // read也是一个阻塞方法
        String str = new String(bytes, 0, len);
        System.out.println(str);
        len=inputStream.read(bytes);
        while(len!=-1){
            str = new String(bytes, 0, len);
            System.out.println(str);
            len=inputStream.read(bytes);
        }
        // 关闭输入流
        socket.shutdownInput();

        inputStream.close();
        outputStream.close();
        socket.close();
    }
}
