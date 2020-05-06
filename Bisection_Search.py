#Approximate square root using Bisection Search

import math

x = float(raw_input('Enter a float: '))

epsilon = 0.01

low = 0.0

high = max(1.0, x)

numGuesses = 0

ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
 
print 'numGuesses = ', numGuesses
print ans, ' is close to square root of ', x

if (math.ceil(ans) ** 2 == x):
    print math.ceil(ans), ' is the real root'
