import numpy as np

# Concatenação

a = np.array([[1, 2], [3, 4]])
print(a)
b = np.array([[5, 6]])
print(b)
c = np.concatenate((a, b), axis=None)
print(c)
d = np.concatenate((a, b), axis=0)
print(d)
e = np.concatenate((a, b.T), axis=1)
print(e)

print('')

# hstack: Stacka arrays em sequencia horizontalmente (referente a colunas). Precisa de um tuple
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
c = np.hstack((a,b))
print(c)
a = np.array([[1,2], [3,4]])
b = np.array([[5,6], [7,8]])
c = np.hstack((a,b))
print(c)

print('')

# vstack: Stacka arrays em sequencia verticalmente (referente a linhas). Precisa de um tuple
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
c = np.vstack((a,b))
print(c)
a = np.array([[1,2], [3,4]])
b = np.array([[5,6], [7,8]])
c = np.vstack((a,b))
print(c)
