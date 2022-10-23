import numpy as np

# dimensoes do array:
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(a)

# indexacao de array
b = a[0,1]
print(b)

# Slicing
row0 = a[0,:]
print(row0)

col0 = a[:, 0]
print(col0)

slice_a = a[0:2,1:3]
print(slice_a)

# index começando do final: -1, -2 etc...
last = a[-1,-1]
print(last)
