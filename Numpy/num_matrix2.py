import numpy as np
#선형 방정식 풀이 
"""2x + 3y = 1
    x - 2y = 4"""
A = np.array([[2, 3], 
              [1, -2]])
b = np.array([1, 4])
x = np.linalg.solve(A, b)
print('A :\n', A, '\nb :', b)
print('x :',x)

#행렬식
a = np.array([[1, 2],
              [3, 4]])
print('a :\n', a)
print('np.linalg.det(a) :', np.linalg.det(a))