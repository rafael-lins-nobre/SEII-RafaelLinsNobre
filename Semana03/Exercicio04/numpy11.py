import numpy as np

# Broadcasting

# Broadcasting é um mecanismo que permite o numpy trabalhar com arrays de diferentes
# formatos ao realizar operacoes aritimeticas

x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = x + v  # Adiciona v a cada linha de x usando broadcasting
print(y) 