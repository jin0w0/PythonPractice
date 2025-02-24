import numpy as np
a = np.array([1, 2, 3])
print('a :', a)
print('a.max() :',a.max())
print('a.min() :',a.min())
print('a.mean() :',a.mean())

b = np.array([[1, 1], [2, 2], [3, 3]])
print('b :', b)
print('b.flatten()',b.flatten()) #배열의 평탄화 메서드

c = np.array([[4, 5, 6], [7, 8, 9]])
print('c :', c)
print('np.append(a, c) :',np.append(a, c))
print('np.append([a], c, axis = 0) :\n',np.append([a], c, axis = 0))

print('np.random.rand(3, 3) :', np.random.rand(3, 3)) # 3x3 난수 생성성
print('np.random.randint(0, 10, size = 20) :', np.random.randint(0, 10, size = 20)) #0에서 10사이 20개의 난수 생성