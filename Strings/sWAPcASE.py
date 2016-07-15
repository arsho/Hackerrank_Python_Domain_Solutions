'''
Title     : sWAP cASE
Subdomain : Strings
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
__author__ = 'arsho'
inputString=input()
finalString=""
for i in range(0,len(inputString)):
    currentChar=inputString[i]
    if(currentChar.islower() or currentChar.isupper()):
        finalString+=currentChar.swapcase()
    else:
        finalString+=currentChar
print(finalString)
