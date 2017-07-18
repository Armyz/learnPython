# -*- coding:utf-8 -*-

from multiprocessing import *
from threading import Thread
from socket import *
import sys

def serverWorker(newSocket ,destAddr):
    try:
        print("接收到[%s]客户端连接"%str(destAddr))

        while True:
            recvData = newSocket.recv(1024)
            if len(recvData) > 0:
                print("recv[%s]:%s"%(destAddr, recvData.decode("utf-8")))
            else:
                print("客户端[%s]已关闭"%str(destAddr))
                break
    finally:
        newSocket.close()

if __name__ == "__main__":

    #创建服务器套接字
    serverSocket = socket(AF_INET, SOCK_STREAM)
    #重复使用绑定信息
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    #绑定
    serverSocket.bind(("", 7788))
    #监听
    serverSocket.listen(10)

    try:
        while True:
            print("等待新的客户端链接")
            #等待客户端连接
            newSocket, destAddr = serverSocket.accept();
            #将接受到的新的客户端放入进程中
            client = Process(target = serverWorker, args = (newSocket, destAddr))
            #多线程
            #client = Thread(target = serverWorker, args = (newSocket, destAddr))

            client.start()
            #已经讲新的套接字复制了一份到新的子进程中
            newSocket.close()
            #若是多线程，则不能关闭，子线程需要用到父进程的资源
            #newSocket.close()

    finally:
        #关闭服务器套接字
        serverSocket.close()
