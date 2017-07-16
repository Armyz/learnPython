# -*- coding:utf-8 -*-

from socket import *

if __name__ == "__main__":

    #创建服务器套接字
    serverSocket = socket(AF_INET, SOCK_STREAM)
    #重复使用绑定信息
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    #绑定
    serverSocket.bind(("", 7788))
    #监听
    serverSocket.listen(10)
    #设置服务器套接字为非阻塞，在使用accept时不会阻塞
    serverSocket.setblocking(False)
    #保存接受到的客户端套接字
    clientSocketList = []

    #主动使用ctrl+c时产生的异常
    try:
        while True:
            try:
                #接受客户端连接，若没有连接则产生异常
                clientSocket, destAddr = serverSocket.accept();
            except:
                pass
            else:
                #设置客户端为非阻塞，recv时不会阻塞
                clientSocket.setblocking(False)
                #将接受到的新的客户端放入客户端套接字列表中
                clientSocketList.append((clientSocket, destAddr))

                print("%s已连接"%str(destAddr))

            #FOR循环遍历是否接受到新的内容
            for clientSocket, destAddr in clientSocketList:
                try:
                    recvData = clientSocket.recv(1024)
                except:
                    pass
                else:
                    if len(recvData) > 0:
                        print("[%s]:%s"%(destAddr, recvData.decode("utf-8")))
                    else:
                        print("%s已下线"%str(destAddr))
                        clientSocket.close()
                        clientSocketList.remove((clientSocket, destAddr))
    except:
        #关闭服务器套接字
        serverSocket.close()
