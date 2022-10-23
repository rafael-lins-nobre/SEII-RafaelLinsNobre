import numpy as np

# Gerando dados

a = np.zeros((2,3)) # size tem que ser um tuple
b = np.ones((2,3))
print(a)
print(b)

# Valor especifico
c = 5 * np.ones((3,3))
print(c)
c = np.full((3,3),5.0)
print(c)

# Matriz identidade
d = np.eye(3) #3x3
print(d)

# arange
e = np.arange(10)
print(e)

# linspace
f = np.linspace(0, 10, 5)
print(f)