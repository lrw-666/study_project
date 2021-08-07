"""网络编程"""
from socket import *
from time import *

"""
tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 创建TCP/IP套接字
udpSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # 创建UDP/IP套接字
"""

HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)


def tcp_server():
    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    tcpSerSock.bind(ADDR)  # 将地址绑定到套接字上
    tcpSerSock.listen(5)  # 设置并启动TCP监听器
    try:
        while True:
            print('waiting for connection...')
            tcpCliSock, addr = tcpSerSock.accept()  # 接收客户端连接
            print('...connected from:', addr)

            while True:
                data = tcpCliSock.recv(BUFSIZ)  # 接收
                if not data:
                    break
                tcpCliSock.send(bytes('[%s] %s' % (ctime(), data), 'utf-8'))  # 发送

            tcpCliSock.close()
    except():
        tcpSerSock.close()


def tcpClient():
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)  # 尝试连接服务器
    while True:
        data = input('> ')
        if not data:
            break
        tcpCliSock.send(bytes(data, 'utf-8'))
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        print(data.decode('utf-8'))
    tcpCliSock.close()

def udp_server():
    udpSerSock = socket(AF_INET, SOCK_DGRAM)
    udpSerSock.bind(ADDR)
    while True:
        print('waiting for message...')
        data, addr = udpSerSock.recvfrom(BUFSIZ)
        udpSerSock.sendto(bytes('[%s] %s' % (ctime(), data)), addr)
        print('...received from and returned to:', addr)
    udpSerSock.close()

def udp_client():
    udpCliSock = socket(AF_INET, SOCK_DGRAM)
    while True:
        data = input('> ')
        if not data:
            break
        udpCliSock.sendto(data, ADDR)
        data, ADDR = udpCliSock.recvfrom(BUFSIZ)
        if not data:
            break
        print(data)
    udpCliSock.close()

# SocketServer模块：事件驱动，只有在系统中的时间发生时，他们才会工作
# Twisted框架:一个完整的事件驱动的网络框架

if __name__ == '__main__':
    tcp_server()
    # tcpClient()
