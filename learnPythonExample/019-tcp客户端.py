 # -*- coding:utf-8 -*-

from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect(("127.0.0.1", 7788))

while True:
    sendMsg = raw_input("请输入发送内容:")
    if sendMsg == "q":
        break;
    clientSocket.send(sendMsg);

clientSocket.close()
