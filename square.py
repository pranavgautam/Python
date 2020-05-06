#Squaring an integer the hard way

x=int(raw_input('Enter an Integer: '))
ans=0
i=abs(x)

while(i!=0):
    ans += abs(x)
    i -= 1
print str(x)+'^2 = '+str(ans)
