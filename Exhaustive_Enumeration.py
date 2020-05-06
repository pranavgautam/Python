#Approximate square root using Exhaustive Enumeration Search

import math

x = float(raw_input('Enter a float: '))

epsilon = 0.01

step = epsilon ** 3

numGuesses = 0

ans = 0.0

if x < 0:
    print 'Failed on square root of ', x
else:
    while abs(ans**2 - x) >= epsilon and ans**2 <= x:
        ans += step
        numGuesses += 1
 
    print 'numGuesses = ', numGuesses

    if abs(ans**2 - x) >= epsilon:
        print 'Failed on square root of ', x
    else:
        if (math.ceil(ans) ** 2 == x):
            print math.ceil(ans), ' and ', -(math.ceil(ans)), ' are square roots of ', x
        elif (math.floor(ans) ** 2 == x):
            print math.floor(ans), ' and ', -(math.floor(ans)), ' are square roots of ', x
        else:
            print ans, ' and ', -ans, ' are close to square roots of ', x
            print 'On squaring ', ans, '(or ', -ans, ') we get ', ans**2

