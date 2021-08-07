package hncu;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class TCPServer {
    public static void main(String[] args) throws Exception {
        // 指定接收端端口
        ServerSocket socket = new ServerSocket(8888);
        while(true){
            // 接收信息
            Socket accept = socket.accept();
            byte[] bytes = new byte[1024];
            int len;
            InputStream inputStream = accept.getInputStream();
            while((len=inputStream.read(bytes))!=-1){ // 要等待客户端关闭流才行
                String str = new String(bytes, 0, bytes.length);
                System.out.println(str);
            }
            // 返回消息
            OutputStream outputStream = accept.getOutputStream();
            outputStream.write("你已经成功连接到服务器！".getBytes());

            inputStream.close();
            outputStream.close();
        }
    }
}
