'''
Title     : Validating Roman Numerals
Subdomain : Regex and Parsing
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
def my_func(s):
    s = s.upper()
    ##res=re.match(r'^(?=[MDCLXVI])M*(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$',s)
    res=re.search(r'^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$',s)
    if(s=="MMMM"):
        print "False"
    else:
        if res:
            print "True"
        else:
            print "False"
my_func(raw_input())
