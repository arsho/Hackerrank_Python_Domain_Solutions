"""
Title     : Between Two Sets
Subdomain : Implementation
Domain    : Python
Author    : Imtiaz Ahmed
Created   : 27 August 2022
Problem   : https://www.hackerrank.com/challenges/between-two-sets/problem
"""

def getMultiples(num, toRange):
    # returns all the multiples of a number in a list without any loop
    multiples = range(num, toRange, num)
    return [*multiples]

def getCommonMultiples(arr):
    """
    gets all the multiples of each item in a list and set them in a list of lists then returns the common values of each list in a single list
    """ 
    multiples_lists = []
    for num in arr:
        multiples = getMultiples(num, 101) 
        #100 is the constraint range in the problem set
        multiples_lists.append(multiples)
    common_multiples = list(set.intersection(*map(set, multiples_lists)))
    return common_multiples

def getFactors(num):
    # returns all the factors of a number in a list
    factors = []
    for i in range(1, num+1):
        if num % i == 0:
            factors.append(i)
    return factors

def getCommonFactors(arr):
    """
    gets all the factors of each item in a list and sets them in list of lists. Then return the common values of each list in a single list
    """
    factors_lists = []

    for number in arr:
        factors = getFactors(number)
        factors_lists.append(factors)
    
    common_factors = list(set.intersection(*map(set, factors_lists)))
    return common_factors

def getTotalX(a, b):
    # main function
    common_multiples = getCommonMultiples(a)

    common_factors = getCommonFactors(b)

    return len(list(set.intersection(*map(set, [common_multiples, common_factors]))))