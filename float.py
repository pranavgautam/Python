#Problem with Float, Finger Excercise

x=0.0

for i in range (10):
    x += 0.1
    print round(x, 53)
if round(x,1) == 1.0:
    print x
else:
    print 'x not 1'
    print round(x, 53)
