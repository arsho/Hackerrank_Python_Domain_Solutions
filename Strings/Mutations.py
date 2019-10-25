'''
Title     : Mutations
Subdomain : Strings
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Updated   : 25 October 2019
Problem   : https://www.hackerrank.com/challenges/python-mutations/problem
'''
def mutate_string(string, position, character):
    return string[:position]+character+string[position+1:]

