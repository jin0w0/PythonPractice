import numpy as np

a = np.zeros((2, 3)) #영행렬
print('a :', a)
b = np.ones((2, 3))
print('b :', b)
c = np.full((2, 3), 100)
print('c :', c)
d = np.eye(3) # identity matrix 단위행렬
print('d :', d)
e = np.random.random((2, 3))
print('e :', e)
# 
print('np.arange(0, 10, 2) :', np.arange(0, 10, 2)) #0에서 10미만 2씩 건너뜀
print('np.linspace(0, 10, 5) :', np.linspace(0, 10, 5)) #0에서 10사이 값 5개