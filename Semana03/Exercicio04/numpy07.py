import numpy as np

a = np.array([[1,2], [3,4]])
print(a)
print(a.shape)
print ('')

# linhas primeiro, depois colunas
print(a[0])
print(a[0][0])
print(a[0,0])
print('')

# slicing
print(a[:,0]) # todas as linhas na coluna 0
print(a[0,:]) # todas as colunas na linha 0

# transposicao
print(a.T)

# multiplicacao de matrizes
b = np.array([[3, 4], [5,6]])
c = a.dot(b)
print('c:',c)
d = a * b # elementwise multiplication
print('d:',d)


# determinante
c = np.linalg.det(a)
print(c)

# inversa
c = np.linalg.inv(a)
print(c)

# diagonal
c = np.diag(a)
print(c)

# diag on a vector returns diagonal matrix (overloaded function)
c = np.diag([1,4])
print(c)