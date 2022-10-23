import numpy as np

print(np.__version__)
print('')

a = np.array([1,2,3,4,5])
print(a)
print(a.shape)
print(a.dtype)
print(a.ndim)
print(a.size)
print(a.itemsize)
print('')

print(a[3])
a[3] = 10
print(a)
print('')

b = a * np.array([2,0,2,1,2])
print('array b:', b)