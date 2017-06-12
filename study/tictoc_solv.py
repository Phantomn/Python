import socket
from ctypes import *
import os

host = "1.222.106.212"
port = 205

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))


data = s.recv(1024)
print data
data = s.recv(1024)
print data
data = data.split("\n")
data = data[0][13:23]

clib = cdll.LoadLibrary("libc.so.6")

clib.srand(int(data))
seed = str(clib.rand() % 10000)
s.send(seed + "\n")
data = s.recv(1024)
print data
data = s.recv(1024)
print data