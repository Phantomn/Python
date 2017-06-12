regex = r'0\d{1,2}[ -]?\d{3,4}[ -]?\d{3,4}'

search_target = '''Luke Skywarker 02-123-4567 luke@daum.net
darthvader 070-9999-9999 darth_vader@gmail.com
princess leia 010 2454 3457 leia@gmail.com'''

import re

result = re.findall(regex, search_target)
print "\n".join(result)