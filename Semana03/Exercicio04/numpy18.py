import numpy as np

# loading from csv
# https://www.python-engineer.com/videos/how-to-load-data/

# 1) load with np.loadtxt()
# skiprows=1
data = np.loadtxt('FILE_NAME', delimiter=",",dtype=np.float32)
print(data.shape, data.dtype)

# 2) load with np.genfromtxt()
# skip_header=0, missing_values="---", filling_values=0.0
data = np.genfromtxt('FILE_NAME', delimiter=",", dtype=np.float32)
print(data.shape)