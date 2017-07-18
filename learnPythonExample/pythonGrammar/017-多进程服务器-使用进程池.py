# -*- coding:utf-8 -*-

from multiprocessing import Pool
from socket import *
import sys

def serverWorker(msg):
    try:
        newSocket, destAddr = msg

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

    #创建进程池,同时可执行10个任务
    pool_apply_async = Pool(10)
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
            recvCient = serverSocket.accept();
            #将接受到的客户端放入进程池中运行
            pool_apply_async.apply_async(serverWorker, (recvCient, ))
    finally:
        #关闭套接字
        serverSocket.close()
        pool_apply_async.close()
        pool_apply_async.join()
