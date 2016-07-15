'''
Title     : Find a string
Subdomain : Strings
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
s=raw_input()
ss=raw_input()
cnt=0
len_s=len(s)
len_ss=len(ss)
for i in range(0,len_s):
    tmp=s[i:i+len_ss]
    if(tmp==ss):
        cnt=cnt+1
print cnt
