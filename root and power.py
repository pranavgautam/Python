#Write a program that asks the user to enter an integer and prints two integers, root
#and pwr, such that 0 < pwr < 6 and root**pwr is equal to the integer entered by the user.
#If no such pair of integers exists, it should print a message to that effect.

x = int(raw_input('Enter an Integer: '))

root = 2

power = 6

if abs(x) < 4:
    print 'No root and power pair exists'
else:
    while power > 0:
        while root**power < abs(x):
            root = root + 1
        if root**power==abs(x):
            break          
        power = power - 1
        root = 2
    if power < 2:
        print 'power is 1'
    elif x < 0 and power%2 == 0 :
        print 'No root and power pair exists'
    elif x < 0 and power%2 != 0 :
        root = -root
    print 'Root: ' + str(root)
    print 'Power: ' + str(power)
  
