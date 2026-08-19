def add(num1 = 0,num2 = 0):  #default arguments
    return num1+num2
result = add(3,5)
print(result)


def add1(num1, *num2): #variable length arguments
    sum = num1
    for n in num2:
        sum += n
    print(num2)
    return sum 

result = add1(23,54,76,24,65,65)
print(result)


def person(name,age):
    print(f"name : {name}")
    print(f"age : {age}")

person(age = 23, name = "yash") #Keyword argument *args 

print()

def person1(name, **kwargs):
    print(f"name : {name}")
    for k,v in kwargs.items():
        print(f"{k} : {v}")
    # print(kwargs)

person1(name = "Narendra", age = 24, loc = "Bombay", profession = "Software Developer")