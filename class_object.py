#class = blueprint or template. it is the structure of object 
# object = an object is thing which is created from the class
# eg: blueprint(class) -> house(object)
# self: self refers to the current object on which the method is being called 
# __init__ is constructer it runs autmatically whenever an object is created 

# Class → Blueprint or template.
# Object → A real instance created from the class.
# Attributes → Variables that store an object's data (e.g., name, age).
# Methods → Functions defined inside a class that describe what an object can do.
# self → Refers to the current object whose method is being executed.
# __init__ → Constructor that automatically initializes an object when it is created.

# class car:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age

# car1 = car("Benz", 2002)
# print(car1)

# class student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def intro(self):
#         print(f"Hello {self.name} your age age is {self.age}")
# s1 = student("Narendra",24)
# s1.intro()

# class Student:

#     def intro(self):
#         print(self.name)

# s1 = Student()
# s1.intro()


# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# s1 = Student("Narendra",23)
# print(s1.name)
# print(s1.age)

# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#     def display_info(self):
#         print(f"Name: {self.name}")
#         print(f"Salary: {self.salary}")
# emp = Employee("Narendra", 50000)
# emp.display_info()


#Inheritance
# class Animal:
#     def __init__(self, sound):
#         self.sound = sound
#         print(f"Some1 {self.sound}")

# class Dog(Animal):
#     def dog(self, sound):
#         super().__init__(sound)
#         print(f"Some2 {self.sound}")

# dog = Dog("Sound")
# dog.dog("Sound")

# class Cat:
#     def cat(self):
#         print("Meow")
# class rabbit(Cat):
#     pass
# mouse = rabbit()
# mouse.cat()
    
# Encapsulation🟢
# # Private access modifier
# class Person:
#     def __init__(self,name,age):
#         self._name = name
#         self._age = age
    
#     # def display(self):
#     #     print(f"Person name is {self._name} and his age is {self._age}")
# person = Person("Ajay",18)
# person.display()
# print(dir(person))

# #Protected access modifier
# class Student(Person):
#     def __init__(self,name,age,roll_no):
#         super().__init__(name,age)
#         self._roll_no = roll_no
#     def display(self):
#         print(f"Person name is {self._name} and his age is {self._age}. Roll number is {self._roll_no}")

# student = Student("John", 20, 12345)
# student.display()

# class Rectangle:
#     def __init__(self,length,width):
#         self._length = length
#         self._width = width
#     def area(self):
#         return self._length * self._width
# shape = Rectangle(5, 3)
# shape._length(10)
# shape._width(4)
# shape.area()
    
import requests
from bs4 import BeautifulSoup

def print_secret_message(url):
    # Download the published Google Doc
    html = requests.get(url).text

    # Extract plain text from the document
    soup = BeautifulSoup(html, "html.parser")
    lines = soup.get_text("\n").splitlines()

    # Keep only non-empty lines
    lines = [line.strip() for line in lines if line.strip()]

    points = []

    # Skip header row and parse triples:
    # x-coordinate, character, y-coordinate
    i = 0
    while i + 2 < len(lines):
        try:
            x = int(lines[i])
            ch = lines[i + 1]
            y = int(lines[i + 2])
            points.append((x, y, ch))
            i += 3
        except ValueError:
            i += 1

    if not points:
        print("No valid data found.")
        return

    max_x = max(x for x, _, _ in points)
    max_y = max(y for _, y, _ in points)

    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, y, ch in points:
        grid[y][x] = ch

    for row in grid:
        print("".join(row))

print_secret_message("https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub")