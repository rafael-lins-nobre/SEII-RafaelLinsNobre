import numpy as np

a = np.array([[1,2], [3, 4], [5, 6]])
print(a)

# mesmas dimensoes com True or False como condicao
bool_idx = a > 2
print(bool_idx)
print(a[bool_idx])

# Fazendo os comandos acima em uma unica linha
print(a[a > 2])

# np.where(): mesmas dimensoes com valores modificados com base no condicional
b = np.where(a>2, a, -1)
print(b)

# fancy indexing: acessando multiplos index ao mesmo tempo
a = np.array([10,19,30,41,50,61])
print(a)
b = a[[1,3,5]]
print(b)
even = np.argwhere(a%2==0).flatten()
print(even)
a_even = a[even]
print(a_even)