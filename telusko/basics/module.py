import math
num = 36
result = math.sqrt(num)
print(result) 

#what if from this math module i want to use only few function but multiple time then above syntax is kinda repetative
#here is another way for using a particular function from a particular module 

from math import sqrt,ceil, floor,pow,acos,fabs
num1 = 25
result = sqrt(num1)
print(result)

result1 = ceil(64.4)
result2 = floor(64.4)
result3 = pow(10,3)
print(result1,result2,result3)
print("---")
print(help(acos)) 
print("---")
#another way is instead of import math and then state math.function name we can do 
import math as m
num1 = 45
result4 = m.sqrt(num1)
print(result4)
print(help(fabs))

x = -10.7
y = 3
print(m.ceil(x))
print(m.fabs(x))
print(m.pow(y,2))

from calculator.calc import *

result = add(34,78)
print(f"result : {result}")