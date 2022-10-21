# ======= Codigo 1 ==========
x = 'global x'

def test():
    global x
    x = 'local x'
    y = 'local y'
    print(y)
    print(x)

test()
print(x)

# ======= Codigo 2 ==========
import builtins
#def min():  #wrong use of the definition
#    pass

# ======= Codigo 3 ==========
m = min([5, 1, 4, 2, 3])
print(m)

def test(z):
    x = 'local x'
    print(z)

test('local z')
#print(z) #this will cause an error

# ======= Codigo 4 ==========
x = 'global x'

def outer():
    x = 'outer x'

    def inner():
        #nonlocal x
        x = 'inner x'
        print(x)
        
    inner()
    print(x)

outer()
print(x)