#Cube Root

x=int(raw_input('Enter an Integer: '))

ans=0

while ans**3 < abs(x):
    ans += 1
    
if ans**3!=abs(x):
    print str(x) + ' is not a perfect cube. So sorry for loss.'
else:
    if x<0:
        ans = -ans
    print 'Cube root of ' + str(x) + ' is ' + str(ans)
