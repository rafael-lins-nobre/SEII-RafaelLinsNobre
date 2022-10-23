import numpy as np

# reshape
a = np.arange(1, 7)
print(a)

b = a.reshape((2, 3)) # 2 linhas, 3 colunas
print(b)

c = a.reshape((3, 2)) # 3 linhas, 2 colunas
print(c)
print('')

# newaxis is used to create a new axis in the data
# needed when model require the data to be shaped in a certain manner
print(a.shape)
d = a[np.newaxis, :]
print(d)
print(d.shape)

e = a[:, np.newaxis]
print(e)
print(e.shape)