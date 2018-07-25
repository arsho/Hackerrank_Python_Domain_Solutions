'''
Title     : Lists
Subdomain : Data Types
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
ar=[]
n=int(input())
for i in range(0,n):
    tmp_str=input()
    tmp_str_ar=tmp_str.strip().split(" ")
    cmd=tmp_str_ar[0]
    if(cmd=="print"):
        print(ar)
    elif(cmd=="sort"):
        ar.sort()
    elif(cmd=="reverse"):
        ar.reverse()
    elif(cmd=="pop"):
        ar.pop()
    elif(cmd=="count"):
        val=int(tmp_str_ar[1])
        ar.count(val)
    elif(cmd=="index"):
        val=int(tmp_str_ar[1])
        ar.index(val)
    elif(cmd=="remove"):
        val=int(tmp_str_ar[1])
        ar.remove(val)  
    elif(cmd=="append"):
        val=int(tmp_str_ar[1])
        ar.append(val)          
    elif(cmd=="insert"):
        pos=int(tmp_str_ar[1])
        val=int(tmp_str_ar[2])
        ar.insert(pos,val)
