#Using Functions

def maximum(x, y):
    if x > y:
        return x
    else:
        return y

def isIn(x, y):
    if x in y or y in x:
        return True
    else:
        return False

#Scoping

def f(x):
    def g():
        x = 'abc'
        print 'x = ', x
    def h():
        z = x
        print 'Z = ', z
    x += 1
    print 'X = ', x
    h()
    g()
    print 'X = ', x
    return g

x = 3

z = f(x)

print 'X = ', x
print 'Z = ', z
z()

print''

print maximum(int(raw_input('Enter X: ')), int(raw_input('Enter Y: ')))

print''

print''

print isIn(str(raw_input('Enter String 1: ')), str(raw_input('Enter String 2: ')))

print''
