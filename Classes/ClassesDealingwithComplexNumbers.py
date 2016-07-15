'''
Title     : Classes: Dealing with Complex Numbers
Subdomain : Classes
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
# Enter your code here. Read input from STDIN. Print output to 


c_str_ar=raw_input().strip().split()
d_str_ar=raw_input().strip().split()

def custom_print(n):
    r=n.real
    i=n.imag
    ret_str=""
    if(i==0 and r==0):
        ret_str="0.00"
    elif(r==0):        
        tmp_str="%.2f" %i
        ret_str=tmp_str+"i"
    elif(i==0):        
        tmp_str="%.2f" %r
        ret_str=tmp_str
    else:
        tmp_str1="%.2f" %r
        tmp_str2="%.2f" %i     
        if(i>0):
            ret_str=tmp_str1+" + "+tmp_str2+"i"
        else:
            i=i*-1
            tmp_str2="%.2f" %i                 
            ret_str=tmp_str1+" - "+tmp_str2+"i"
    print ret_str

cr=float(c_str_ar[0])
ci=float(c_str_ar[1])
dr=float(d_str_ar[0])
di=float(d_str_ar[1])
c=complex(cr,ci)
d=complex(dr,di)

val_add=c+d
val_sub=c-d
val_mul=c*d
val_div=c/d
mod_c=abs(c)
mod_d=abs(d)

custom_print(val_add)
custom_print(val_sub)
custom_print(val_mul)
custom_print(val_div)


print "%.2f" %mod_c
print "%.2f" %mod_d
