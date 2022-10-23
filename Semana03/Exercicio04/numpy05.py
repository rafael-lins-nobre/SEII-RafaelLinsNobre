import numpy as np

l1 =[1,2,3]
l2 = [4,5,6]
a1 = np.array(l1)
a2 = np.array(l2)

dot = 0
for i in range(len(l1)):
    dot += l1[i] * l2[i]
print("dot of list:", dot)

dot = np.dot(a1,a2)
print('dot of array:',dot)

#sum_array = a1 * a2
#dot = np.sum(sum_array)
dot = (a1*a2).sum()
print("manual dot of array:",dot)

dot = a1 @ a2
print("dot of array com @:",dot)