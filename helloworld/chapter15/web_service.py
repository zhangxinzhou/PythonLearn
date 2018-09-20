# coding:utf-8
import socket
import re
from multiprocessing import Process

HTML_ROOT_DIR = "./Views"


class HTTPService(object):
    def __init__(self):
        """"初始化方法"""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def start(self):
        """开始方法"""
        self.server_socket.listen(128)
