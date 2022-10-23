import numpy as np

# Random numbers
a = np.random.random((3,2)) # distribuicao uniforme entre 0-1
print(a)
b = np.random.randn(3,2) # DIstribuicao normal/Gaussiana, media 0 e variancia 1
                         # nao eh um tuple como argumento, cada dimensao um argumento
print(b)

R = np.random.randn(10000)
print(R.mean(), R.var(), R.std())

R = np.random.randn(10, 3)
print(R.mean()) # media do array inteiro

# random integer, low,high,size; high is exclusive
R = np.random.randint(3,10,size=(3,3)) # if we only pass one parameter, then from 0-x
print(R)

# with integer is between 0 up to integer exclusive
c = np.random.choice(7, size=10)
print(c)
# with an array it draws random values from this array
d = np.random.choice([1,2,3,4], size=8)
print(d)