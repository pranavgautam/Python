#Approximate square root using Bisection Search

import math

x = float(raw_input('Enter a float: '))

epsilon = 0.01

low = 0.0

high = max(1.0, x)

numGuesses = 0

ans = (high + low)/2.0

if x < 0:
    print 'Failed on square root of ', x
else:
    while abs(ans**2 - x) >= epsilon:
        numGuesses += 1
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
 
    print 'The program made ', numGuesses, ' guesses in total'

    if (math.ceil(ans) ** 2 == x):
        print math.ceil(ans), ' and ', -(math.ceil(ans)), ' are square roots of ', x
    elif (math.floor(ans) ** 2 == x):
        print math.floor(ans), ' and ', -(math.floor(ans)), ' are square roots of ', x
    else:
        print ans, ' and ', -ans, ' are close to square roots of ', x
        print 'On squaring ', ans, '(or ', -ans, ') we get ', ans**2
        
