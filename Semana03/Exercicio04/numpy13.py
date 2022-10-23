import numpy as np

# Datatypes
# https://numpy.org/devdocs/user/basics.types.html

# O proprio numpy escolhe o datatype por default
x = np.array([1, 2])
print(x.dtype)

# O proprio numpy escolhe o datatype por default
x = np.array([1.0, 2.0])
print(x.dtype)

# Forçando um determinado datatype
x = np.array([1, 2], dtype=np.int64) # 8 bytes
print(x.dtype)

x = np.array([1, 2], dtype=np.float32) # 4 bytes
print(x.dtype)