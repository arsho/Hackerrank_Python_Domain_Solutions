'''
Title     : String Formatting
Subdomain : Strings
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
n = int(input().strip())
w = len(str(bin(n))[2:])
for i in range(1,n+1,1):
    o = str(oct(i))[2:]
    h = str(hex(i))[2:]
    h = h.upper()
    b = str(bin(i))[2:]
    d = str(i)
    print('{:>{width}} {:>{width}} {:>{width}} {:>{width}}'.format(d,o,h,b,width=w))
