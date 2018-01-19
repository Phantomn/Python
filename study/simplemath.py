from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('45.32.63.188', 2939))

print s.recv(4096)
s.send("\n")
print s.recv(1024)
data = s.recv(1024)