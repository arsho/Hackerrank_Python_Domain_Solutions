'''
Title     : Finding the percentage
Subdomain : Data Types
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
ar={}
for i in range(0,n):
    s=input()
    ss=s.split(" ")
    n=ss[0]
    m1=float(ss[1])
    m2=float(ss[2])
    m3=float(ss[3])
    m_avg=(m1+m2+m3)/3.0
    ar[n]="%.2f" % m_avg
s_name=input()
print(ar[s_name])
