# def add(a,b):                 # Traditional way
#     return a+b

add = lambda a,b : a+b 

result = add(23,765)
print(result)


operate = lambda num : "Even" if num % 2 == 0 else "Odd"
num = int(input("Enter a number: "))
result = operate(num)
print(result)