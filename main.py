import numpy as np

a = np.array([1,2,3,4,5])
print(a)

b = np.array([[1,2,3] ,[4,5,6]])
print(b)
print(b.shape)

print(b[0][1])

x = np.zeros([10,5] , dtype = int)
print(x)

q = np.linspace(10,20,5)
print(q)