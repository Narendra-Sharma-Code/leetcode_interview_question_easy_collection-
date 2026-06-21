#Variables = A container for storing data values
#String = A sequence of characters, enclosed in quotes
#Integer = A whole number, positive or negative, without decimals
#Float = A number that has a decimal point
#Boolean = A data type that can only be True or False
#List = A collection of items that are ordered and changeable, enclosed in square brackets
#Tuple = A collection of items that are ordered and unchangeable, enclosed in parentheses
#Set = A collection of unique items that are unordered and unindexed, enclosed in curly braces
#Dictionary = A collection of key-value pairs that are unordered, changeable, and indexed, enclosed in curly braces
import math
#Example of variables
#string
# name = "Bro Code"
city = "Miami"

#integer
age = 24

#float
distance = 5.7
quantity = 9
pi = 3.14

#boolean
is_online = True
is_happy = False    

#Typcasting = the process of converting a variable from one data type to another
#str(),int(),float(),bool()

age = str(age)
pi = int(pi)
name_num = "24"
name_num = int(name_num)    

#user_input = a function that allows the user to input data into the program

# user_name = input("Hello Your Name is: ")
# user_age = int(input("What's your age: "))
# user_age += 1
# print(f"User Name is {user_name}")
# print("Happy Birthday")
# print(f"{user_name} turns to {user_age}")

#Exercise find Area of a Rectangle A = lw
# length = float(input("Enter length: "))
# width = float(input("Enter Width: "))
# Area_of_rectangle = length * width

#Madlib Game = a game where you create a story by filling in the blanks with words

# print(f"Today i went to the {city} and met {name}. He is {age} years old. We walked {distance} miles and bought {quantity} items. The value of pi is approximately {pi}. Is he online? {is_online}. Is he happy? {is_happy}. The area of the rectangle is {Area_of_rectangle}.")

#arithmatic operators = +, -, *, /, %, **, //
dost = 10
# dost = dost +1
# dost += 1
# dost = dost -1 
# dost -= 1
# dost = dost * 4
# dost *= 4
# dost = dost / 2 
# dost /= 2
# dost = dost % 2
# dost %= 2
# dost = dost ** 2
# dost **= 2

x = 3.14
y = -5
z = 36

# result = round(x)
# result = abs(y)
# result = pow(3,x)
# result = min(x,y,z)
# result = max(x,y,z)
# print(result)

#built in math module

# print(math.ceil(x))
# print(math.floor(x))
# print(math.pi)
# print(math.e)
# print(math.sqrt(z))

#Exercise circumference of a circle 2*pi*r
# radius = float(input("Enter Radius of a circle: "))
# result = 2*math.pi*radius
# print(f"Circumference of a circle is {round(result,2)}")

#Exercise area of a circle A= pi*r^2

# r = float(input("Enter Radius of circle: "))
# area = math.pi * pow(r,2)
# print(f"Area of a circle is {round(area,2)}cm²")

#Exercise hypotanious of a triangle c = underroot(a^2 + b^2)
# sideA = float(input("Enter Side A value: "))
# sideB = float(input("Enter Side B value: "))
# hyp = math.sqrt(pow(sideA,2) + pow(sideB,2))
# print(f"hypotaneous of right angeled triangle is: {round(hyp,2)}")

#If = Do some code only if some condition is True
#else do something else
# user_age = int(input("Enter Your Age: "))

# if user_age >= 100:
#     print("You are too old for sign-up")
# elif user_age >=18:
#     print("You are eligible for signing in")
# elif user_age <0: 
#     print("you are not born yet")
# else:
#     print("you are not 18+")

# name = input("Enter your name: ")
# if name == "":
#     print("You did not type in your name")
# else:
#     print(f"Hello {name}")

# for_sale = True
# if for_sale:
#     print("this item is for sale")
# else:
#     print("this item is not for sale")

# is_online = False
# if is_online:
#     print("you are online")
# else:
#     print("the person you are trying to reach is offline")

#Exercise python calculator
# operator = input("Enter an operator from this(+ - * /): ")
# num1 = float(input("Enter a number: "))
# num2 = float(input("Enter second number: "))
# if operator == "+":
#     print(num1 + num2)
# elif operator == "-":
#     print(num1 - num2)
# elif operator == "*":
#     print(num1*num2)
# elif operator == "/":
#     print(num1/num2)
# else:
#     print(f"your chosen operator {operator} is not a valid operator")


#Exercise weight conversion using conditional statement
# weight = float(input("Enter your weight: "))   
# unit = input("Enter unit of weight K/L: ")
# if unit == "K":
#     weight = weight *2.205
#     unit = "L"
#     print(f"your weight is {round(weight,2)} {unit}")
# elif unit == "L":
#     weight = weight /2.205
#     unit = "K"
#     print(f"your weight is {round(weight,2)}{unit}")
# else:
#     print(f"entered unit {unit} was not valid")

#Exercise Temperature conversion
# unit = input("Is this temperature is in Celsius or Fahrenheit(C/F): ")
# temp = float(input("Enter value of Temperature: "))

# if unit == "C":
#     result = round((9*temp)/5 + 32, 2)
#     print(f"converted Temperature is {round(result,2)}℉")
# elif unit == "F":
#     result = round((temp - 32) * 5/9, 2)
#     print(f"converted temperature is {round(result,2)}")
# else:
#     print(f"Entered unit {unit} is not valid")

# logical operators = evaluate multiple condition (and, or, not)
                    # or = either one condition is true
                    # and = both conditions must be true
                    # not = inverts the result, returns False if the result is true
# temp = 21
# is_raining = False
# if temperature > 30 or temperature < 0 or is_raining:
#     print("the outdoor plan is cancel")
# else:
#     print("the outdoor plan is onn!!")
# if 25 > temp >10 and not is_raining:
#     print("it is warm outside!!")
# else:
#     print("bhagooo penchoo")

#Conditional Expression: A one-line shortcut for if else statement(ternary operator)
# print or assign one of two value based on condition 
# x if condition else y

# num = 8
# a = 4
# b = 9
# user_role = "Admin"

# print("Positive" if num >=0 else "Negative") 
# result = "Even" if num % 2 == 0 else "Odd"
# max_num = a if a >b else b
# min_num = a if a < b else b
# access = "Full access" if user_role == "Admin" else "Limited access"
# print(access)


#String Methods = built-in functions that perform specific operations on strings
# name = input("Enter your name: ")
# result = name.capitalize()
# result = name.upper()
# result = name.lower()
# result = name.find("n")
# result = name.rfind("N")
# result = len(name)
# result = name.isdigit()
# result = name.isalnum()
# result = name.count("n")
# result = name.replace("b", " ")
# print(result)

#validate user input exercise
# rule: 1. username is not more than 12 charachters
# 2. username must not contain any spaces
# 3. username must not contain any digits

# username = input("Enter your username: ")

# length = len(username)
# space = username.replace(" ", "")
# digit_less = space.isalpha()

# if length < 12 and digit_less:
#     print(f"This user {space} is valid")
# else:
#     print(f"{username} is not a valid username")

#Indexing = accessing elements of a sequence using [](indexing operator)
#[start:stop:step]

# credit_number = "123-456-789-06543"
# print(credit_number[0:-1])
# print(credit_number[::-1])
# print(credit_number[0::2])
# print(credit_number[0:9])
# last_digit = credit_number[-4:]
# print(f"XXXX-XXX-XXX-{last_digit}")

# format specifiers = {value:flags}format a value based on what flag is inserted 
# price1 = 3.143443
# price2 = 86.4542345
# price3 = 43500.1235541
# print(f" Price is ${price3:,.2f}")

#WHile loop = execute some code while some condition is true
# user_name = input("Enter your name: ")

# while user_name == "":
#     print("You did not enter your name")
#     user_name = input("Enter your name: ")
# print(f"Hello {user_name}")

# ❌user_age = int(input("Enter your age: ")) this line has error
# while user_age < 0:
#     print("Enter valid age")
#     user_age = int(input("Enter valid age: "))
#     print("You will be stuck in this matrix until you enter a valid age")
#     user_age = int(input("Enter your age again: "))
# print(f"Your age is {user_age}"). this is a faulty code❌

# while True:
#     try:
#         user_age = int(input("Enter your: "))
#         if user_age <= 0:
#             print("Age can not be negative or zero")
#         else:
#             break
#     except ValueError:
#         print("Enter valid age")
# print(f"Your age is {user_age}")

#food = input("what's your fav dish(enter q for quit): ")
# while not food == "q":
#     print(f"Your fav dish is {food} ")
#     food = input("what's your fav dish(enter q for quit): ")
# print(f"your fav dish is {food}")

# while True:
#     try:
#         food = input("what's your fav dish(enter q for quit):")
#         if food == "q":
#             break 
#         print(f"Your fav dish is {food}")
#     except ValueError:
#         print("Enter valid dishname")

# num = int(input("Enter a number between 1 to 10:  "))
# while 0 < num <11: 
#     print(f"you have chosen {num}")
#     num = int(input("Enter num again: "))
# print(f"your last chosen number was: {num}")

# num = int(input("Enter a number between 1 to 10:  "))
# while num < 1 or num >10: 
#     print(f"you have chosen {num} which is wrong")
#     num = int(input("Enter num again: "))
# print(f"your last chosen number was: {num}")

# python compound interest calculater formula: A = P* pow((1 + r/n),t)
# principle = 0
# rate = 0
# time = 0

# while principle <= 0:
#     principle = int(input("Enter principle amount: "))
#     if principle < 0:
#         print("Principle amount can't be negative or equal to zero ")
#     else: break

# while rate <= 0:
#     rate = float(input("Enter Rate of Interest: "))
#     if rate <= 0:
#         print("Interest Rate can't be negative or equal to zero ")
#     else: break

# while time <= 0:
#     time = int(input("Enter Time in year's: "))
#     if time <= 0:
#         print("Time can't be negative or equal to zero ")
#     else: break
# total = principle * pow((1 + rate / 100),time) 
# print(f"Balance amount for {time} years is {round(total,2)}")

#for loop: executes a block of code for a fixed number of times
# you can iterate over a range, string, sequence, etc

# for counter in range(1,11):
#     print(counter)

# card_num = "123124-35245-5674-46574"
# for x in card_num:
#     print(x)
# for x in range(1,11,2):
#     if x == 1:
#         continue
#     else:
#         print(x) 

#Python Countdown Program

# import time
# my_time = int(input("Enter time in seconds: "))
# for x in range(my_time,0,-1):
#     seconds = x % 60
#     minutes = int(x /60) % 60
#     hour = int(x /3600)
#     print(f"{hour:02d}:{minutes:02d}:{seconds:02d}")
#     time.sleep(1)

#nested loops = a loop inside another loop(outer loop and inner loop):
#outerloop:         }
#    innerloop:     }       syntax

# rows = int(input("Enter number of rows: "))
# columns = int(input("Enter number of columns: "))
# symbol = input("Enter number of symbol: ")

# for x in range(columns):
#     for y in range(rows):
#         print(symbol, end="-- ")
#     print()

#Type of Collection:single variable that can hold multiple values:
    #List[]: ordered and changeable. Duplicates OK
    #Set{}: unordered and immutable. Duplicates NOT OK, but add/remove ok
    #Tuple(): ordered and unchangeable. Duplicates OK. Faster
    # Dictionary: ordered and changeable || don't know about this yet
# List[]🟢
# car = ["BMW", "Toyota", "Honda", "Mercedes"]
# print(car[3]).  || [start:stop:end]

# for x in car:
#     print(x) 

# print(dir(car)). || this will show all the built in methods for list data type
# print(help(car))  || this will discribe all the built in methods for list data type
# print(len(car))

# print("BMW" in car) || returns True if the value is found in the list
# car.append("Audi") #|| adds an element to the end of the list
# car.insert(1,"Lexus") #|| adds an element at the specified position
# car.remove("Honda") #   || removes the first item with the specified value                      
# car.remove("Lexus") #   || removes the first item with the specified value
# print(car.count("BMW")) #   || returns the number of times the specified value appears in the list§
# print(car)
# List[] end🔴

# set{}🟢
color = {"Red", "Green", "Blue", "Yellow"}
# color.pop()
# color.remove("Red")
# color.add("grey")
# color.add("Red")
# print("grey" in color)
# print(color)
# set{}end🔴

#tuple()🟢
# game = ("cricket", "football", "basketball", "durby")
# print(dir(game))
# print(help(game))
# print(game.index("football"))
# print(game.count("football"))

#Shopping cart program
foods = []
prices = []
total = 0
while True:
    food = input("Enter food to buy(q to quite): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter price of {food}: $"))
        foods.append(food)
        prices.append(price)
print(f"---- YOUR FOOD CART HAS -----")
for x in foods:
    print(x, end=" ")
for price in prices:
    total += price
print()
print(f"Your total bill is ${round(total, 2)}")