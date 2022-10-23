import numpy as np

# Copia
a = np.array([1,2,3])
b = a # Copia apenas a referencia
b[0] = 42
print(a)

a = np.array([1,2,3])
b = a.copy() # Copia genuina eh feita com a funcao copy()
b[0] = 42
print(a)