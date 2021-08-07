package hncu;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.SocketException;

public class UDPServer {
    public static void main(String[] args) throws IOException {
        // 定义接收端
        DatagramSocket socket = new DatagramSocket(8001);
        // 定义字节数组用于接收数据，最大为65507字节(8K)
        byte[] bytes = new byte[1024];
        // 定义一个用于封装接收信息的数据报对象
        DatagramPacket packet = new DatagramPacket(bytes, 0, bytes.length);
        socket.receive(packet);
        String line = new String(packet.getData(), 0, packet.getLength());
        System.out.println(line);
        socket.close();
    }
}
