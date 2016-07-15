'''
Title     : Most Common
Subdomain : Collections
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
import collections
s = sorted(input().strip())
s_counter = collections.Counter(s).most_common()
'''
s_counter_length = len(s_counter)
for i in range(0,s_counter_length,1):
    for j in range(i+1,s_counter_length,1):
        if (s_counter[i][1] == s_counter[j][1]) and (ord(s_counter[j][0]) < ord(s_counter[i][0])):
            s_counter[i],s_counter[j] = s_counter[j],s_counter[i]
'''
s_counter = sorted(s_counter,key = lambda x: (x[1] * -1,x[0]))
for i in range(0,3):
    print(s_counter[i][0],s_counter[i][1])
