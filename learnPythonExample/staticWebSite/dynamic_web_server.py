# -*- coding:utf-8 -*-

from multiprocessing import *
from socket import *
import re
import sys

# html 根目录
HTML_ROOT_DIR = "./html"
PY_ROOT_DIR = "./pyShellDir"


class HTTPServer(object):
    def __init__(self):
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.response_heads = ""

    # 开启服务
    def start(self):
        self.server_socket.listen(128)
        print("等待客户端连接")
        try:
            while True:
                client_socket, client_address = self.server_socket.accept()

                # 开启新的进程处理客户端连接
                client_process = Process(target=self.client_process_handler,
                                         args=(client_socket, client_address))

                client_process.start()
                client_socket.close()
           
        except Exception as ex:
            print("主进程产生异常:%s" % ex)
            
        finally:
            self.server_socket.close()
    
    # 处理客户端请求
    def client_process_handler(self, new_socket, request_address):

        print("[%s]已连接" % str(request_address))

        request_data = new_socket.recv(2048)
        try:
            # 将接受到的数据根据换行符进行分割放入列表
            request_head_lines = request_data.splitlines()
            for line in request_head_lines:
                print(line)

            # 请求第一行头 "GET / HTTP/1.1" bytes类型
            request_first_line = request_head_lines[0]

            # 获取请求文件名
            get_file_name = re.match(r"\w+\s+(/[^ ]*)",
                                     request_first_line.decode("utf-8")).group(1)

            if "/" == get_file_name:
                get_file_name += "index.html"

            if get_file_name.endswith(".py"):
                try:
                    m = __import__(get_file_name[1:-3])
                    env = {

                    }
                    response_body = m.application(env, self.start_response)
                    response_head_lines = self.response_heads
                except Exception as e:
                    response_head_lines = "HTTP/1.1 404 Not Found!\r\n"
                    response_head_lines += "Server:My Server\r\n"
                    response_body = "File Not Found!"
                    print(e)
            else:
                try:
                    file_fd = open(HTML_ROOT_DIR + get_file_name, "rb")
                except IOError:
                    response_head_lines = "HTTP/1.1 404 Not Found!\r\n"
                    response_head_lines += "Server:My Server\r\n"
                    response_body = "File Not Found!"
                else:
                    file_data = file_fd.read()
                    file_fd.close()

                    # 构造响应数据
                    response_head_lines = "HTTP/1.1 200 OK!\r\n"
                    response_head_lines += "Server:My Static Server\r\n"
                    response_body = file_data.decode("utf-8")
        
            response = response_head_lines + "\r\n" + response_body
            print(response)
            # 发送数据 Python3需要将发送内容进行bytes转换
            new_socket.send(bytes(response, "utf-8"))
        # 是否有异常产生   
        except Exception as ex:
            print("客户端处理产生异常:%s" % ex)
        finally:
            new_socket.close()

    # bind 地址,传输一个元组
    def bind(self, bind_info):
        self.server_socket.bind(bind_info)

    # bind 地址,传输一个元组
    def start_response(self, status, headers):
        response_head_lines = "HTTP/1.1 " + status + "\r\n"
        server_heads = [
            ('Date', 'Mon, 31 June 2017 16:01:12 GMT'),
            ('Server', 'WSGIServer 0.1'),
        ]
        headers += server_heads
        for line in headers:
            response_head_lines += "%s:%s\r\n" % line

        self.response_heads = response_head_lines


def main():
    # 定义主函数入口

    # 添加搜索对象
    sys.path.insert(1, PY_ROOT_DIR)

    # httpServer实例对象
    http_server = HTTPServer()
    http_server.bind(("", 8000))
    http_server.start()

if __name__ == "__main__":
    main()
