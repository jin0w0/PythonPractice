import numpy as np
#aixs
a = np.arange(6).reshape(3, 2)
print('a :', a)
print('a.sum() :', a.sum())
print('a.sum(axis = 0) :', a.sum(axis = 0))
print('a.sum(axis = 1) :', a.sum(axis = 1))

print('a.min(axis = 0) :', a.min(axis = 0))
print('a.min(axis = 1) :', a.min(axis = 1))
print('a.max(axis = 0) :', a.max(axis = 0))
print('a.max(axis = 1) :', a.max(axis = 1))
print('a.mean(axis = 1) :', a.mean(axis = 1))

b = np.array([1, 3, 4])
print('b :', b)
print('np.insert(b, 1, 2) :',np.insert(b, 1, 2)) #b에 1위치에 2 추가

c = np.array([[1, 1], [2, 2], [3, 3]])
print('c :', c)
print('np.insert(c, 3, 4, axis = 0) :',np.insert(c, 3, 4, axis = 0))
print('np.insert(c, 1, 4, axis = 1) :',np.insert(c, 1, 4, axis = 1))