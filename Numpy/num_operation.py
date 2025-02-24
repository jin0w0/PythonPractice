import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a + b
print('a :', a)
print('b :', b)
print('c (c = a + b) :', c)

#2차원
a = np.array([[1, 2], [3, 4]])
b = np.array([[10, 20], [30, 40]])
print('a :', a)
print('b :', b)
print('a + b :', a + b)
print('a - b :', a - b)
print('a * b :', a * b)
print('a / b :', a / b)

#행렬곱
print('np.matmul(a, b) :', np.matmul(a, b))
print('a @ b :', a @ b)

#행렬의 각 성분에 대한 연산
print('a + 1 :', a + 1)
print('a - 1 :', a - 1)
print('a * 100 :', a * 100)
print('a / 100 :', a / 100)
print('a ** 2 :', a ** 2)