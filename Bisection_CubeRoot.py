#Approximate cube root using Bisection Search

import math

x = float(raw_input('Enter a float: '))

y = abs(x)

epsilon = 0.01

low = min(-y, 0.0)

high = max(0.0, y)

numGuesses = 0

ans = (high + low)/2.0

while abs(ans**3 - y) >= epsilon:
    numGuesses += 1
    if ans**3 < y:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
 
print 'The program made ', numGuesses, ' guesses in total'

if (math.ceil(ans) ** 3 == y) and x < 0:
    print -(math.ceil(ans)), ' is the cube root of ', x
elif (math.ceil(ans) ** 3 == y) and x >= 0:
    print math.ceil(ans), ' is the cube root of ', x
elif (math.floor(ans) ** 3 == x) and x < 0:
    print -(math.floor(ans)), ' is the cube root of ', x
elif (math.floor(ans) ** 3 == x) and x >= 0:
    print math.floor(ans), ' is the cube root of ', x
else:
    if x < 0:
        print -ans, ' is close to cube root of ', x
        print 'On cubing ', -ans, ' we get ', -ans**3
    else:
        print ans, ' is close to cube root of ', x
        print 'On cubing ', ans, ' we get ', ans**3
