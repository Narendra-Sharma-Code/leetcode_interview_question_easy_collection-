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
import random
import time

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
# foods = []
# prices = []
# total = 0
# while True:
#     food = input("Enter food to buy(q to quite): ")
#     if food.lower() == "q":
#         break
#     else:
#         price = float(input(f"Enter price of {food}: $"))
#         foods.append(food)
#         prices.append(price)
# print("---- YOUR FOOD CART HAS -----")
# for x in foods:
#     print(x, end=" ")
# for price in prices:
#     total += price
# print()
# print(f"Your total bill is ${round(total, 2)}")

#2D collection = a collection of collections
# foods = ["Pizza", "Burger", "Fries"]
# veggies = ["Broccoli", "Spinach", "Carrots"]
# drinks = ["Coke", "Pepsi", "Sprite"]

# grocery_list = [foods, veggies, drinks]
# print(grocery_list[0][1])
# for x in grocery_list:
#     for y in x:
#         print(y,end=" ")
#     print()

#QUIZZ GAME🟢
# questions = (("In India how many states are there"),
#              ("How many bones are there is human body"),
#              ("At what age a person is eligible for Driving License"),
#              ("which is the hottest planet in solar system"))
# options = (("12","34","45","26"),
#            ("34","206","456","420"),
#            ("10","15","18","24"),
#            ("mercury","venus","earth","sun"))
# answers = ("B","B", "C", "C")
# score = 0
# guesses = []
# question_num = 0
# for question in questions:
#     print("--------------")
#     print(question)
#     for option in options[question_num]:
#         print(option)

#     guess = input("Enter answer as(A,B,C,D): ").upper()
#     guesses.append(guess)
#     if guess == answers[question_num]:
#         score += 1
#         print("CORRECT!")
#     else:
#         print("ICORRECT!")
#         print(f"{answers[question_num]} is the Correct answer")
#     question_num += 1

# print("--------------")
# print("RESULTS")
# print("--------------")

# print("Answers: ", end=" ")
# for answer in answers:
#     print(answer, end=" ")  

# print()
# print("Guesses: ", end=" ")
# for guess in guesses:
#     print(guess, end=" ")
# score = int(score / len(questions) * 100)
# print()
# print(f"Your score is: {score}%")🔴

#dictionary{}🟢
#a collection of {key:value} pairs that are ordered, changeable and no duplicates
# captials = {"USA":"Washington DC",
#             "India":"New Delhi",           
#             "Russia":"Moscow",
#             "China":"Beijing",
#             "Japan":"Tokyo"
#             }
# print(captials.get("USA"))
# print(captials.get("India"))
# if captials.get("Japan"):
#     print("Japan is present in the dictionary")
# else:
#     print("Japan is not present in the dictionary")

# captials.update({"Germany":"Berlin"})
# captials.update({"USA":"New York"})
# captials.pop("China")
# captials.popitem()
# captials.clear()
# key = captials.keys()
# print(key) 
# for key in captials.keys():
#     print(key)        

# values =  captials.values()
# print(values)

# items = captials.items()
# # print(items)
# for key, value in captials.items():
#     print(f"{key}: {value}")
# 🔴

#concession stand program 🟢
# menu = {
#     "pizza": 60.0,
#     "brownie": 80,
#     "popcorn": 150,
#     "fries": 40,
#     "soda": 30,
#     "cold drink": 80,
#     "burger": 100
#     }

# cart = []
# total = 0
# print("----------MENU----------")
# for key,value in menu.items():
#     print(f"{key:10}: {value:.2f}")
# print("------------------------")

# while True:
#     food = input("Enter Your Order food item(q for quit): ").lower()
#     if food == "q":
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)
# print()
# print("------Your Order---------")
# for food in cart:
#     total += menu.get(food)
#     print(food, end=" | ")
# print()
# print(f"Total is: {total:.2f}")
# 🔴
    
#Random Numbers 🟢


# # numbers = random.randint(1,10)
# low = 1
# high = 1000
# options = ("rock","paper", "scissors")
# cards = [2,3,4,5,6,7,8,9,"J","Q","K","A"]

# # numbers = random.randint(low,high)
# # numbers = random.random()
# option = random.choice(options)
# random.shuffle(cards)
# print(cards)
# 🔴

#random guess game 🟢
# low = 1
# high = 100
# answer = random.randint(low,high)
# guesses = 0
# is_running = True

# print("--Python Number Guessing Game--")
# print(f"Guess a number between {low} and {high}")
# while is_running:
#     guess = input("Guess a number: ")
#     if guess.isdigit():
#         guess = int(guess)
#         guesses += 1
#         if guess not in range(low,high):
#             print("Invalid guess")
#         elif guess > answer:
#             print("Too high,Try again!")
#         elif guess < answer:
#             print("Too low, Try again!")
#         else:
#             print("Correct Answer!!👍")
#             print(f"You Took {guesses} tries to Crack thisss☠️")
#             is_running = False
#             # break
#     else:
#         print("Invalid Guess")
# 🔴  

# #Rock, Paper, Scissors Game🟢
# options = ("rock", "paper", "scissors")
# is_playing = True

# while is_playing:
#     player =  None
#     computer = random.choice(options)
#     print("---Python Rock | Paper | Scissors. Game--- ")
    
#     while player not in options:
#         player = input(f"Enter your Choice: ").lower()

#     print(f"Player: {player}")
#     print(f"Computer: {computer}")
#     if player == "rock" and computer == "paper":
#         print("Congratsss You Win!!")
#     elif player == "paper" and computer == "rock":
#         print("Congratsss You Win!!")
#     elif player == "scissors" and computer == "paper":
#         print("Congratsss You Win!!")
#     elif player == computer:
#         print("WHooooooo it's a tie!!")
#     else: 
#         print("You lose, Bitchhhh!!")
    
#     respawn = input("You wanna Play again(y/n):").lower()
#     if respawn != "y":
#         is_playing = False
# print("Thanks for playing this game, see you next time!!")
# 🔴


#Functions = a block of code that is executed only when it is called 🟢

# def happ_birthday(name,age):
#     print(f"Happy birthday to {name}")
#     print(f"you are {age} year's old")
# happ_birthday("BroCode", 26)🔴

#return: statement used to end a function and send a result back to the caller 🟢
# def candidate_name(first,last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return first + " " + last

# full_name = candidate_name("narendra","sharma")
# print(full_name)
# print(candidate_name("Yellow","Flash"))🔴

#default parameter = a parameter that assumes a default value if a value is not provided in the function call 🟢
#make your function more flexible by allowing the user to specify only the parameters they want to change
#1 positional argument 2. default argument 3. keyword argument 4. arbitrary 

# def coupon(price,discount=0.037,tax=0.034):
#     return price * (1-discount) * (1+ tax)
# print(coupon(500,0.3,0.04))
# print(coupon(300))

# def count(end, start =10):
#     for x in range(start,end+1):
#         print(x)
#         time.sleep(3)
#     print("DONE!")
# count(18,15)

# print("Welcome to dice rolling simulator")
# dice = input("roll the dice(Enter 'r' to roll): ") 
# dice = dice.lower()
# while dice == "r":
#     print(f"You rolled a {random.randint(1,6)}")
#     dice = input("roll the dice(Enter 'r' to roll): ")
#     dice = dice.lower()
# print("Thanks for playing this game, see you next time!!")

#keyword argument = an argument proceded by an identififier. helps with readability. order of argument doesn't matter🟢

# def student(name,std,div):
#     print(f"Hello {name}, you are currently in {std}-{div}")
# student("narendra",10,"A") ||positional argument
# student(div="A", std= 10,name="Narendra") || keyword argument

# def get_number(country,area,first,last):
#     return f"{country}-{area}-{first}-{last}"
# phone_num = get_number(first=702123, last= 12480, country=91, area=101)
# print(phone_num)🔴

# *args = allows you to pass multiple non-keyword arguments
# **kwargs = allows you to pass multiple keyword arguments🟢
# *unpacking operator
# ------*args------
# def get_arg(*nums):
#     for num in nums:
#         print(num, end=" ")

# get_arg(1,4,6,7,3,7)

# print()
# -------**kwargs start--------
# def get_address(**address):
#     for keys,values in address.items():
#         print(keys,values)

# get_address(state="Monaco", street= "101", Home="Yupp")

# def analytic(*args,**kwargs):
#     print(args,kwargs) 
#     for x in kwargs.keys():
#         print(x)

# analytic(
#     "Engr","Narendra Sharma",
#     intro= "Fighter",
#     proficiency = "KO specialists"
# )# # 🔴

#Iterables = An object that can return its element ine at a time.🟢
#.           allowing it to be iterated over in a for loop

# nums = [1,2,3,4,5,6,7,8,9]
# for num in reversed(nums):
#     print(num, end= " ")
# tuples = (1,2,3,4,5,6,7,8,9)
# for tups in reversed(tuples):
#     print(tups)
# sets = {1,2,3,4,5,6,7,8,9,0}
# for set in sets:
#     print(set)

# dict = {"a":1,"b":2,"c":3}
# for key in dict.values():
#     print(key)🔴

