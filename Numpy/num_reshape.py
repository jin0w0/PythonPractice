import numpy as np

print('np.arange(0,10).reshape(2, 5) :',np.arange(0,10).reshape(2, 5))
print('np.arange(0,24).reshape(4, 3, 2) :',np.arange(0, 24).reshape(4, 3, 2)) #텐서, 3차원 배열

#전치 transpose
a = np.arange(6).reshape(3, 2)
print('a :', a)
print('np.transpose(a) :', np.transpose(a))
