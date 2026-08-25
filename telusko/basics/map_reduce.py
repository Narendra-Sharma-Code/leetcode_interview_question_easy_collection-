from functools import reduce 

num =[2,4,65,23,56,23,567,45,238,218,548,18]

# store = []
# def evens(*args):
#     for i in args:
#        if i % 2 == 0:
#             store.append(i)
# result = evens(2,4,65,23,56,23,567,45,238,218,548,18)
# print(store)

even_it = list(filter(lambda n : n % 2 == 0,num))
odd_it = list(filter(lambda n : n % 2 != 0,num))
double_even = list(map(lambda n : n * 2,even_it))
sum_even = reduce(lambda a,b : a+b , double_even)
sum_odd = reduce(lambda a,b : a+b,odd_it)

print(f"Evens : {even_it}")
print(f"Odd : {odd_it}")
print(f"Double even : {double_even}")
print(f"Total even : {sum_even}")
print(f"Total odd : {sum_odd}")


# task
list1 = [2,3,4]

cube = list(map(lambda n : n ** 3,list1))
cube1 = reduce(lambda a,b : a + b ,cube)
print(cube)
print(cube1)