package hncu;

import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.util.Scanner;

public class UDPClient {
    public static void main(String[] args) throws Exception {
        // 指定发送端端口
        DatagramSocket socket = new DatagramSocket(9999);
        // 定义发送数据
        String line = "hello world";
        // 定义数据报封装信息:二进制信息、长度、网络号、端口
        DatagramPacket packet = new DatagramPacket(line.getBytes(), line.getBytes().length, InetAddress.getByName("127.0.0.1"), 8001);
        socket.send(packet);
        socket.close();
    }
}
