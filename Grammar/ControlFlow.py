#if
x = int(input("number:"))
if x>0:
    print("x>0")
elif x<0:
    print("x<0")
else:
    print("x=0")
#for
list1 = ['a','b','c']
for i in list1:
    print(i)
dict1 = {'a':'가','b':'나','c':'다'}
for key, value in dict1.items():
    print(key, value)
for i in range(0, 3, 1):
    print(i)