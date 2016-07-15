'''
Title     : Class 2 - Find the Torsional Angle
Subdomain : Classes
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
def custom_diff(a,b):
    res0 = a[0] - b[0]
    res1 = a[1] - b[1]
    res2 = a[2] - b[2]
    return [res0,res1,res2]

def dot_product(a,b):
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]

def abs_val(a):
    tmp_val=a[0]*a[0]+a[1]*a[1]+a[2]*a[2]
    return math.sqrt(tmp_val)



def cross(a, b):
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]

    return c

a_str_ar=raw_input().strip().split()
b_str_ar=raw_input().strip().split()
c_str_ar=raw_input().strip().split()
d_str_ar=raw_input().strip().split()

a=list(map(float,a_str_ar))
b=list(map(float,b_str_ar))
c=list(map(float,c_str_ar))
d=list(map(float,d_str_ar))

ab=custom_diff(b,a)
bc=custom_diff(c,b)
cd=custom_diff(d,c)

x=cross(ab,bc)
y=cross(bc,cd)
       
cosphi_top=dot_product(x,y)
cosphi_bottom=abs_val(x)*abs_val(y)
cosphi=cosphi_top/cosphi_bottom

res=math.degrees(math.acos(cosphi))

print "%.2f" %res
