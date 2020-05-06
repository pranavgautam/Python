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
 
print 'The program made ', numGuesses, ' guesses in total'

if (math.ceil(ans) ** 2 == x):
    print math.ceil(ans), ' is square root of ', x
elif (math.floor(ans) ** 2 == x):
    print math.floor(ans), ' is square root of ', x
else:
    print ans, ' is close to square root of ', x
    print 'On squaring ', ans, ' we get ', ans**2
        
