#Newton-Raphson method of finding square root

epsilon = 0.0000000001

k = 24.0

guess = k/2.0

iteration_NR = 0

while abs(guess * guess -k) >= epsilon:
    guess -= ((guess**2) - k)/(2 * guess)
    iteration_NR += 1
print 'Square root of ', k, ' is about ', guess
print iteration_NR
