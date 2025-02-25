import numpy as np

a = np.array([1, 2, 3])
print('a :', a)
print('a[0] : {}, a[1] : {}, a[2] : {}'.format(a[0], a[1], a[2]))
print('a[-1] : {}, a[-2] : {}, a[-3] : {}'.format(a[-1], a[-2], a[-3]))

a = np.array([1, 2, 3, 4, 5])
print('a :', a)
print('a[np.array([0, 1])] :', a[np.array([0, 1])])
print('a[np.array([0, 1, 2])] :', a[np.array([0, 1, 2])])
print('a[np.array([1, 1, 1, 1, 1, 1, 1])] :', a[np.array([1, 1, 1, 1, 1, 1, 1])])

#2차원
a = np.arange(6).reshape(3, 2)
print('a :\n', a)
print('a[0, 0] : {}, a[0, 1] : {}, a[1, 0] : {}'.format(a[0, 0], a[0, 1], a[1, 0]))
#슬라이싱
a = np.arange(9).reshape(3, 3)
print('a :\n', a)
print('a[0] : {}, a[0, :] : {}, a[:, 0] : {}'.format(a[0], a[0, :], a[:, 0]))
print('a[0:2, :2] : \n{}, \na[1:, 1:] : \n{}, \na[1, 1:] : {}'.format(a[0:2, :2], a[1:, 1:], a[1, 1:])) #a[1, 1:]1차원a[1:2, 1:] 2차원 

#3차원
a = np.arange(24).reshape(4, 3, 2)
print('a :\n', a)
print('a[0, 1, 2] :', a[2, 1, 0])
print('a[0] :', a[0])
print('a[0, 0] :', a[0, 0])

print('np.concatenate((a[0, 0], a[0, 2]), axis = 0) :',np.concatenate((a[0, 0], a[0, 2]), axis = 0)) 
print('np.concatenate((a[0], a[1]), axis = 0) :',np.concatenate((a[0], a[1]), axis = 0)) 
print('np.concatenate((a[0], a[1]), axis = 1) :',np.concatenate((a[0], a[1]), axis = 1)) 