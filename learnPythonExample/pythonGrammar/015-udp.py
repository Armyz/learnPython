# -*- coding:utf-8 -*-

from socket import *

#inet_addr = input("请输入IP地址：")
inet_addr = "192.168.1.101"
#inet_port = input("请输入Port：")
inet_port = 8080

bind_addr = ('',2345)

#1建立UDP形式套接字
upd_socket = socket(AF_INET,SOCK_DGRAM)

#2绑定本机信息，IP地址为‘’表示接受所有IP地址的信息，2345为端口号
#其他IP像2345发送信息本机都能够收到
upd_socket.bind(bind_addr)

while True:
    inet_info = input("请输入发送内容：")
    #输入退出标识则退出
    if(inet_info == "quit"
            or inet_info == "exit"
            or inet_info == "退出"):
        break ;

    #3发送数据
    upd_socket.sendto(inet_info.encode("gb2312"),(inet_addr,inet_port))
    #接受数据,阻塞
    recv_data = upd_socket.recvfrom(1024)
    #将接受的元组信息分别赋值给两个变量
    content, destinfo = recv_data

    print("目标机信息：%s内容为：%s"%(destinfo,content.decode("gb2312")))

#5.关闭套接字
upd_socket.close()
