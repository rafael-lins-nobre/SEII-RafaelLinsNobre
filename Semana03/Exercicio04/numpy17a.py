import numpy as np

# eigenvalues
a = np.array([[1,2], [3,4]])
eigenvalues, eigenvectors = np.linalg.eig(a)
# Note: use eigh if your matrix is symmetric (faster)
print(eigenvalues)
print(eigenvectors) # column vectors
print(eigenvectors[:,0]) # column 0 corresponding to eigenvalue[0]

# verify: e-vec * e-val = A * e-vec
d = eigenvectors[:,0] * eigenvalues[0]
e = a @ eigenvectors[:, 0]
print(d, e)
print(d == e) # numerical issues

# correct way to compare matrix
print(np.allclose(d,e))