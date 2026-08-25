num = [23,56,2,45,67,78,87,23,12.34, 34.56, 45.67, 56.78, 67.89, 78.90]

# is_even = lambda n : n % 2 == 0           #traditional lambda way


result = list(filter(lambda n : n % 2 == 0 ,num))
print(result)

# task
list1 = [10,55,32,75,90,41,68,50,34]

greater = lambda l : l >= 50
result1 = list(filter(greater,list1))
print(result1)