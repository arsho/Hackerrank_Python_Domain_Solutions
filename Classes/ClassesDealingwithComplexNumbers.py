'''
Title     : Classes: Dealing with Complex Numbers
Subdomain : Classes
Domain    : Python
Author    : Ahmedur Rahman Shovon
Updater   : Imtiaz Ahmed
Created   : 15 July 2016
Updated   : 30 August 2022
Problem   : https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem
'''
# Enter your code here. Read input from STDIN. Print output to 


# c_str_ar= input().strip().split()
# d_str_ar= input().strip().split()

# def custom_print(n):
#     r=n.real
#     i=n.imag
#     ret_str=""
#     if(i==0 and r==0):
#         ret_str="0.00"
#     elif(r==0):        
#         tmp_str="%.2f" %i
#         ret_str=tmp_str+"i"
#     elif(i==0):        
#         tmp_str="%.2f" %r
#         ret_str=tmp_str
#     else:
#         tmp_str1="%.2f" %r
#         tmp_str2="%.2f" %i     
#         if(i>0):
#             ret_str=tmp_str1+" + "+tmp_str2+"i"
#         else:
#             i=i*-1
#             tmp_str2="%.2f" %i                 
#             ret_str=tmp_str1+" - "+tmp_str2+"i"
#     print(ret_str)

# cr=float(c_str_ar[0])
# ci=float(c_str_ar[1])
# dr=float(d_str_ar[0])
# di=float(d_str_ar[1])
# c=complex(cr,ci)
# d=complex(dr,di)

# val_add=c+d
# val_sub=c-d
# val_mul=c*d
# val_div=c/d
# mod_c=abs(c)
# mod_d=abs(d)

# custom_print(val_add)
# custom_print(val_sub)
# custom_print(val_mul)
# custom_print(val_div)

# print("%.2f" %mod_c)
# print("%.2f" %mod_d)
# Above code is not accepted on hackerrank, There's error somewhere in the above code. One may correct the error and keep the solution the way it was created. For now I'm adding mine, they way Hackerrank asks to solve it.

import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)
        
    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)
        
    def __mul__(self, no):
        return Complex(self.real * no.real - self.imaginary * no.imaginary, self.real * no.imaginary + self.imaginary * no.real)

    def __truediv__(self, no):
        divider = no.real ** 2 + no.imaginary ** 2
        return Complex((self.real * no.real + self.imaginary * no.imaginary)/divider, (self.imaginary * no.real - self.real * no.imaginary)/divider)
        
    def mod(self):
        return Complex(math.sqrt(self.real ** 2 + self.imaginary ** 2), 0.00)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
