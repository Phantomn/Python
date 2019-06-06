from hashlib import *

print '\nExample for SHA256'

m = sha256()

m.update(b'This a')
m.update(b' great python tutorial.')
print('output1 : ',m.digest())

x = sha256(b'This is a great python tutorial.')
print('output 2 : ',x.digest())

print '\nExample for md5'

m = md5()

m.update(b'This a')
m.update(b' great python tutorial.')
print('output1 : ',m.digest())

x = sha256(b'This is a great python tutorial.')
print('output 2 : ',x.digest())