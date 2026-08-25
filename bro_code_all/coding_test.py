# Write a program that asks the user for an integer and prints:
# Even if divisible by 2
# Odd otherwise
num = int(input("Please enter an integer: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Write a program to print the following pattern.
# *
# **
# ***
# ****
# *****
for i in range(1, 6):
    print('*' * i)  

# Take an integer input from the user and print its multiplication table from 1 to 10.
# Example:
# Input: 7
# Output:
# 7 x 1 = 7
# ...
# 7 x 10 = 70
num = int(input("Please enter a number: "))
for i in range(1,11):
    print(f"{num} x {i} = {num * i}")

# Write a function
# find_largest(a, b, c)
# that returns the largest among three numbers.

def find_largest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else: 
        return c
a = int(input("Please enter first number: "))
b = int(input("Please enter second number: "))
c = int(input("Please enter third number: "))
print(f"The largest number is: {find_largest(a,b,c)}")

# Given a list
# numbers = [4,7,2,9,1,5]
# Print:
# Largest number
# Smallest number
numbers = [4,7,2,9,1,5]
numbers.sort()
print(numbers[0])
print(numbers[-1])

# Take a string from the user.
# Print:
# Total characters
# Number of vowels
# Number of consonants
# Ignore spaces.
# Example
# Input
# hello world
# Output
# Characters:10
# Vowels:3
# Consonants:7
str = input("Please enter a string: ")
str = str.replace(" ", "")
vowels = 0
consonants = 0
for char in str:
    if char.lower() in 'aeiou':
        vowels += 1
    else:
        consonants += 1
print(f"Characters: {len(str)}")
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")

# Write a program that removes duplicate elements from a list while maintaining the original order.
# Example
# Input
# [1,2,2,3,1,5]
# Output
# [1,2,3,5]

numbers = [1,2,2,3,1,5]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print(unique_numbers)

# Create a dictionary of student marks.
# Example
# {
# "Alice":90,
# "Bob":75,
# "Charlie":88
# }
# Ask the user for a student's name.
# Print the marks if found.
# Otherwise print
# Student not found
student_marks = {
    "Alice": 90,
    "Bob": 75,
    "Charlie": 88
}
student_name = input("Please enter a student's name: ")
if student_name in student_marks:
    print(f"{student_name}: {student_marks[student_name]}")
else:
    print("Student not found")


# Write a function
# frequency(text)
# that returns the frequency of every character using a dictionary.
# Example
# Input

# banana

# Output

# {
# 'b':1,
# 'a':3,
# 'n':2
# }

def frequency(text):
    freq = {}
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq
print(frequency("banana"))

# Create your own module named
# calculator.py
# It should contain four functions:
# add
# subtract
# multiply
# divide
# Create another Python file that imports the module and performs all four operations.
from bro_code_all.calculator import add, subtract, multiply, divide

print(add(5, 3))
print(subtract(5, 3))
print(multiply(5, 3))
print(divide(5, 3))