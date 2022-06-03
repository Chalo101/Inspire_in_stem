from cmath import sqrt

import math
a =int(input("Enter the coefficient of the first term (a) : "))
b =int(input("Enter the coefficient of the second term: (b) "))
c =int(input("Enter the constant: "))
w =math.sqrt(b**2 - 4*a*c)
# a is the coefficient of first term
# b is the coefficient of the second term
# c is the constant

def find_roots(a,b,c):
    y_1=( -b - w) /(2*a)

    y_2=( -b - w) /(2*a)
    print(f'the roots of the quadratic equation are : {y_1 } {y_2}')

find_roots(a,b,c)