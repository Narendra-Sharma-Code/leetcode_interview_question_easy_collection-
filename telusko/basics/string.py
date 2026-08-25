print('new\'s "star"')
print("Path: C:\\Python\"day1\"Scripts")
print("abcd'e \"xyz\\\" ")
print('narendra' 'phd')
name = 'Madara'
print(name + " uchiha")
print(name[-1])
print(name[1:5:2])

text = "Hello, I am learning Python \n I am enjoying it"
print(text) 
text1 = "Telusko"
print(text1[-6:6])

s = "hello"
s = 'H' + s[1:] #string are immutable 
print(s)
s = "Python is easy to learn"
words = s.split()
print(words) 
print(len(words))

z = ["Python", "is", "awesome"]
z = "-".join(z)
print(z)

print("Python".find(" "))
print("Python".index("y"))

# Write a Python program that counts the number of vowels in a string.
input = "Hello World"
vowels = "aeiouAEIOU"
count = 0
for char in input:
    if char in vowels:
        count += 1
print("Number of vowels:", count)

# Write a Python program to check whether a string is a palindrome.
palindrome = "madam"
if palindrome == palindrome[::-1]:
    print("The string is a palindrome")

