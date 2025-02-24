import numpy as np
a = np.array([1, 2, 3]) #ndarray 객체 생성
print('a :',a)
print('a.shape :',a.shape) #형태
print('a.ndim :',a.ndim) #차원
print('a.dtype :',a.dtype) #자료형
print('a.itemsize :',a.itemsize) #차지하는 메모리 크기
print('a.size :',a.size) #항목 수
b = np.array([4, 5, 6], dtype= 'int64') #dtype = np.int64
print('b.dtype :',b.dtype)
#서로 다른 자료형의 값을 원소로 가질 수 없음. 