import numpy as np

# Resolvendo sistemas lineares
# x1+x2=2200
# 1.5 x1 + 4 x2 = 5050
# 2 equacoes e 2 icognitas
A = np.array([[1, 1], [1.5, 4]])
b = np.array([2200,5050])

# Ax = b <=> x = A-1 b

# But: usar inverso eh devagar e menos preciso
x = np.linalg.inv(A).dot(b) # nao eh recomendado
print(x)
x = np.linalg.solve(A,b) # Melhor forma de fazer
print(x)