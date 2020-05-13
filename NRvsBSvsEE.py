#Newton Raphson v/s Bisection Search v/s Ekhaustive Enumeration

import math

print''
print''
k = float(raw_input('Enter a float: '))

print''

epsilon = 1.0

while epsilon > 0.01:
    epsilon = float(raw_input('Enter the value of epsilon, such that epsilon =< 0.01: '))
    
guess = 0.0

iteration_count = 0

low = 0.0

high = max(1.0, k)

print''
print''
print 'K set to ', k
print ''
print 'Epsilon set to ', epsilon
print''

print'****************************************************'
print'********** RUNNING EXHAUSTIVE ENUMERATION **********'
print'****************************************************'
print''
print''

if k < 0:
    print 'Failed on square root of ', k
else:
    while abs(guess**2 - k) >= epsilon and guess**2 <= k:
        guess += epsilon
        iteration_count += 1
 
    print 'No. of Iterations = ', iteration_count
    print''

    if float(abs(guess**2 - k)) >= epsilon:
        #print (guess**2 - k)
        print 'Failed on square root of ', k
    else:
        if (math.ceil(guess) ** 2 == k):
            print math.ceil(guess), ' and ', -(math.ceil(guess)), ' are square roots of ', k
            print''
        elif (math.floor(guess) ** 2 == k):
            print math.floor(guess), ' and ', -(math.floor(guess)), ' are square roots of ', k
            print''
        else:
            print guess, ' and ', -guess, ' are close to square roots of ', k
            print''
            print 'On squaring ', guess, '(or ', -guess, ') we get ', guess**2
            print''

guess = 0.0

iteration_count = 0

print''
print''
print'****************************************************'
print'********** END OF EXHAUSTIVE ENUMERATION ***********'
print'****************************************************'
print''
print'****************************************************'
print'************* RUNNING BISECTION SEARCH *************'
print'****************************************************'
print''
print''

if k < 0:
    print 'Failed on square root of ', k
else:
    while abs(guess**2 - k) >= epsilon:
        iteration_count += 1
        if guess**2 < k:
            low = guess
        else:
            high = guess
        guess = (high + low)/2.0
 
    print 'No. of Iterations = ', iteration_count
    print''

    if (math.ceil(guess) ** 2 == k):
        print math.ceil(guess), ' and ', -(math.ceil(guess)), ' are square roots of ', k
        print''
    elif (math.floor(guess) ** 2 == k):
        print math.floor(guess), ' and ', -(math.floor(guess)), ' are square roots of ', k
        print''
    else:
        print guess, ' and ', -guess, ' are close to square roots of ', k
        print''
        print 'On squaring ', guess, '(or ', -guess, ') we get ', guess**2
        print''

guess = k/2.0

iteration_count = 0
print''
print''
print'****************************************************'
print'************** END OF BISECTION SEARCH *************'
print'****************************************************'
print''
print'****************************************************'
print'************** RUNNING NEWTON RAPHSON **************'
print'****************************************************'
print''
print''
if k < 0:
    print 'Failed on square root of ', k
else:
    while abs(guess * guess -k) >= epsilon:
        guess -= ((guess**2) - k)/(2 * guess)
        iteration_count += 1
        
    print 'No. of Iterations = ', iteration_count
    print''
    if abs(guess**2 - k) >= epsilon:
        print 'Failed on square root of ', k
    else:
        if (math.ceil(guess) ** 2 == k):
            print math.ceil(guess), ' and ', -(math.ceil(guess)), ' are square roots of ', k
            print''
        elif (math.floor(guess) ** 2 == k):
            print math.floor(guess), ' and ', -(math.floor(guess)), ' are square roots of ', k
            print''
        else:
            print guess, ' and ', -guess, ' are close to square roots of ', k
            print''
            print 'On squaring ', guess, '(or ', -guess, ') we get ', guess**2
            print''

print''
print''
print'****************************************************'
print'*************** END OF NEWTON RAPHSON **************'
print'****************************************************'
print''
print''
