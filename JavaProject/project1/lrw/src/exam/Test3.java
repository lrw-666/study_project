package exam;

import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.SocketException;

public class Test3 {
    public static void main(String[] args) throws SocketException {
        DatagramSocket socket = new DatagramSocket(8001);
        byte[] bytes = new byte[1024];
        int len;
        DatagramPacket packet = new DatagramPacket(bytes, bytes.length);
    }
}
