tup = (12,34,54,23)
print(type(tup))
print(min(tup))
print(max(tup))
print(tup.count(34))

print(tup)
tup1 = tup[::-1]
print(tup1)

# unpacking
value = ("a","b","c",26)
x,y,z,age = value
print(x,y,z,age)

change = ("navin","joseph",[12,43,54,65])
print(change)
print(change[0])
# change[0] = "narendra"  # This will raise an error because tuples are immutable
change[2][1] = "narendra"
print(change)

print(12 in change)
