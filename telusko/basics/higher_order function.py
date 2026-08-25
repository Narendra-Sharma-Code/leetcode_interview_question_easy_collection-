def square(num):
    return num*num

def cube(num):
    return num * num * num

def operate(num, operation):
    for i in num:
        print(operation(i))


nums = [2,3,4,5]
result = operate(nums,cube)
