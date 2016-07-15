'''
Title     : Find Angle MBC
Subdomain : Math
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
import math
ab = float(input())
bc = float(input())
ac = math.sqrt((ab*ab)+(bc*bc))
bm = ac / 2.0
mc = bm
#let, 
b = mc
c = bm
a = bc
#where b=c
angel_b_radian = math.acos(a / (2*b))
angel_b_degree = int(round((180 * angel_b_radian) / math.pi))
output_str = str(angel_b_degree)+'°'
print(output_str)
