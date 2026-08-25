#In python array is used store multiple values of similar types. 
# we can use list but list stores it's value's in different place(address) which can take time for proccessing complex operation.
#array has unicode charachter like (i: integer, f: float)
#array module is used for operating on array

from array import *

arr1 = array("i",[1,3,53,56,7,34])
print(type(arr1))
for n in arr1:
    print(n)
print(arr1.buffer_info()) #this gives address and size it consumed in bytes

print()

arr2 = array("f",[2.5,4.8,-3.2,6.7])
for m in arr2:
    if m < 0:
        continue
    print(m)

