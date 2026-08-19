from array import *

arr1 = array("i",[21,4, 5, 6, 7, 8])
# arr2 = array("i",arr1.tolist()) 
arr2 = array(arr1.typecode,(n for n in arr1))

arr1[2] = 9

print(id(arr1))
print(id(arr2))

print(arr1)
print(arr2)

for i in arr1:
    print(i, end= "-")
print()
for i in arr2:
    print(i, end= "-")
    