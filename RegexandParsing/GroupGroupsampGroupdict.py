'''
Title     : Group(), Groups() &amp; Groupdict()
Subdomain : Regex and Parsing
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
import re
s = input()
res = re.search(r'([A-Za-z0-9])\1',s)
if res == None:
    print(-1)
else:
    print(res.group(1))
