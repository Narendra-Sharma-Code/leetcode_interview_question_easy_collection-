a = 5
print(id(a))
b = 5
print(id(b))
b = 7
print(id(b))
c = 7
print(id(c))
b = 5
print(id(b))
big_number = 10002343443
big_number1 = 10002343443
print(id(big_number))
print(id(big_number1))

a = int("256")
b = int("256")
print(a is b)