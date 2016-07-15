'''
Title     : Capitalize!
Subdomain : Strings
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
s = input()
s_ar = s.split(' ')
final_ar = []
space = ' '
for w in s_ar:
    final_ar.append(w.capitalize())
print(space.join(final_ar))
