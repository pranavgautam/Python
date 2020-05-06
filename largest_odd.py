#largest odd number out of 10

i=10
largest_odd=0

while(i!=0):
    x=int(raw_input('Enter an Integer: '))
    if(x>largest_odd):
        if(x%2!=0):
            largest_odd=x
    i -= 1

if(largest_odd!=0):
    print str(largest_odd) + ' is the largest odd number entered.'
else:
    print 'No Odd Number Entered'
