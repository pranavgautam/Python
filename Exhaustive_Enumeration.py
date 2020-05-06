#Approximate square root using Exhaustive Enumeration Search

x = float(raw_input('Enter a float: '))

epsilon = 0.01

step = epsilon ** 3

numGuesses = 0

ans = 0.0

while abs(ans**2 - x) >= epsilon and ans**2 <= x:
    ans += step
    numGuesses += 1
 
print 'numGuesses = ', numGuesses

if abs(ans**2 - x) >= epsilon:
    print 'Failed on square root of ', x
else:
    print ans, ' is close to square root of ', x
