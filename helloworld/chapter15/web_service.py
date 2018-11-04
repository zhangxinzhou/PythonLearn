# coding:utf-8
import socket
import re
import os
from multiprocessing import Process

# HTML_ROOT_DIR = os.getcwd().replace('\\','/')+"/bat"


HTML_ROOT_DIR = "./Views"


class HTTPService(object):
    def __init__(self):
        """"初始化方法"""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建socket对象

    def start(self):
        """开始方法"""
        self.server_socket.listen(128)
        print('服务器等待客户端连接...')
        # 执行死循环
        while True:
            client_socket, client_address = self.server_socket.accept()  # 建立客户端链接
            print("[%s,%s]用户连接上了" % client_address)
            # 实例化线程类
            handle_client_process = Process(target=self.handle_client, args=(client_socket,))
            handle_client_process.start()  # 开启线程
            client_socket.close()  # 关闭客户端socket

    def handle_client(self, client_socket):
        """处理客户端请求"""
        # 获取客户端请求数量
        request_data = client_socket.recv(1024)  # 获取客户端请求数量
        print("request data:", request_data)
        request_lines = request_data.splitlines()  # 按照行('\r','\r\n','\n')分割
        # 输出每行的信息
        for line in request_lines:
            print(line)
        request_start_line = request_lines[0]  # 解析请求报文
        print("*" * 10)
        print(request_start_line.decode("utf-8"))
        # 使用正则表达式,提取用户请求的文件名
        file_name = re.match(r"\w+ +(/[^ ]*)", request_start_line.decode("utf-8")).group(1)
        # 如果文件名是目录,设置文件名为file_name
        if "/" == file_name:
            file_name = "/index.html"
        # 打开文件,读取内容
        try:
            print("========================================")
            print(HTML_ROOT_DIR + file_name)
            print("========================================")
            file = open(HTML_ROOT_DIR + file_name, "rb")
        except IOError:
            # 如果存在异常,返回404
            response_start_line = "HTTP/1.1 404 Not Fount\r\n"
            response_headers = "Server: My server\r\n"
            response_body = "The file is not found!"
        else:
            # 读取文件内容
            file_data = file.read()
            file.close()
            # 构造响应数据
            response_start_line = "HTTP/1.1 200 OK\r\n"
            response_headers = "Server: My server\r\n"
            response_body = file_data.decode("utf-8")
        # 拼接返回数据
        response = response_start_line + response_headers + "\r\n" + response_body
        print("response data:", response)
        client_socket.send(bytes(response, "utf-8"))  # 向客户端返回响应数据
        client_socket.close()  # 关闭客户端连接

    def bind(self, port):
        """绑定端口"""
        self.server_socket.bind(("", port))


def main():
    """主函数"""
    http_server = HTTPService()
    http_server.bind(8000)
    http_server.start()


if __name__ == "__main__":
    print("=====================路径信息=======================")
    print(os.path.realpath(__file__))
    print(os.path.split(os.path.realpath(__file__)))
    print(os.getcwd())
    print(os.getcwd().replace('\\', '/'))
    print("=====================路径信息=======================")

    main()
