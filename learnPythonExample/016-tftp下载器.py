# -*- coding:utf-8 -*-

from socket import *
import sys
import struct
import time

def main():
    if len(sys.argv) < 3:
        print("*"*30)
        print("Tips:python3 xxx.py ipaddress filename")
        print("*"*30)
        exit()
    else:
        serverIp = sys.argv[1]
        downFileName = sys.argv[2]

    #创建套接字
    udpSocket = socket(AF_INET, SOCK_DGRAM)
    #tftp服务器的IP地址，以及端口号
    sendAddr = (serverIp, 69)
    #计算pack时的format
    packFormat = "!H" + str(len(downFileName)) + "sb5sb"
    #根据tftp协议进行数据封装,请求数据包
    requsetData = struct.pack(packFormat, 1, downFileName, 0, "octet", 0)
    #发送数据
    udpSocket.sendto(requsetData,sendAddr)

    newfile = 0
    blockNum = 0

    while True:
        #接受数据包，元组方式存储
        recvData = udpSocket.recvfrom(1024)
        #将接受到的数据包分别放入接受数据缓冲区和地址缓冲区
        recvContent,recvAddr = recvData
        #解析返回的操作码
        operateNum = struct.unpack("!HH",recvContent[:4])
        print(operateNum)
        #print(recvContent[4:])

        #文件不存在
        if(recvContent[4:] == "File not found"):
            print("%s文件不在"%downFileName)
            break

        #收到数据包
        if(operateNum[0] == 3):
            if(operateNum[1] == 1 and newfile == 0):
                newfile = open(downFileName,"wb")

            if(blockNum+1 == operateNum[1]):
                #写文件
                newfile.write(recvContent[4:])
                blockNum += 1
                print(blockNum)
                if(blockNum == 65535):
                    blockNum = 0

            if(len(recvContent) < 516):
                newfile.close()
                print("下载完毕")
                break

            #发送应答至服务器
            requsetData = struct.pack("!HH",4,operateNum[1])
            #此处的地址必须为服务器返回的IP和端口号
            udpSocket.sendto(requsetData,recvAddr)

        #出现错误
        if operateNum[0] == 5:
            print("download error!")
            break

    udpSocket.close()

if __name__ == "__main__":
    main()
