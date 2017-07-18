# -*- coding:utf-8 -*-

from multiprocessing import *
from socket import *

HTML_ROOT_DIR = "./html"


def client_process_handler(new_socket, request_address):
    try:
        print("接收到[%s]客户端连接" % str(request_address))

        request_data = new_socket.recv(1024)
        print("request Data:%s" % request_data)

        """ 将接受到的数据根据换行符进行分割放入列表 """
        request_head_lines = request_data.splitlines()
        """ 响应第一行头 "GET / HTTP/1.1" """
        request_first_line = request_head_lines[0]

        response_head_lines = "HTTP/1.1 200 OK\r\n"
        response_head_lines += "\r\n"
        response_body = "This is static web Test!"

        response = response_head_lines + response_body

        new_socket.send(bytes(response, "utf-8"))
        new_socket.close()
    except Exception as ex:
        print("差异产生:%s" % ex)
    finally:
        new_socket.close()

if __name__ == "__main__":

    """创建服务器套接字"""
    server_socket = socket(AF_INET, SOCK_STREAM)
    """重复使用绑定信息"""
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    """绑定"""
    server_socket.bind(("", 7788))
    """监听"""
    server_socket.listen(10)

    try:
        while True:
            print("等待新的客户端链接")
            # 等待客户端连接
            client_socket, client_address = server_socket.accept();
            # 将接受到的新的客户端放入进程中
            client_process = Process(target=client_process_handler, args=(client_socket, client_address))

            client_process.start()
            # 已经讲新的套接字复制了一份到新的子进程中
            client_socket.close()
    except Exception as ex:
        print("产生异常：%s" % ex)
        # 关闭服务器套接字
        server_socket.close()