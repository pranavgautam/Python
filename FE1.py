#Finger Excercise 1: find the largest odd numbers out of 3, prompt a response if there are no odd numbers

x=90
y=110
z=61

if(x>y and x>z and x%2 !=0):
    print 'X is the largest odd number'
elif(y>z and y%2!=0):
    print 'Y is the largest odd number'
elif(z%2!=0):
    print 'Z is the largest odd number'
else:
    print 'No Odd Numbers Found'
    
