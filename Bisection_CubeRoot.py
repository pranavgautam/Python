#Approximate cube root using Bisection Search

import math

x = float(raw_input('Enter a float: '))

epsilon = 0.01

low = min(x, 0.0)

high = max(1.0, x)

numGuesses = 0

ans = (high + low)/2.0

while abs(ans**3 - x) >= epsilon:
    numGuesses += 1
    if ans**3 < x:
        low = ans
        print ans
    else:
        high = ans
        print ans
    ans = (high + low)/2.0
 
print 'The program made ', numGuesses, ' guesses in total'

if (math.ceil(ans) ** 3 == x):
    print math.ceil(ans), ' is the cube root of ', x
elif (math.floor(ans) ** 3 == x):
    print math.floor(ans), ' is the cube root of ', x
else:
    print ans, ' is close to cube root of ', x
    print 'On cubing ', ans, ' we get ', ans**3
