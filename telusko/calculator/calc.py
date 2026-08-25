def add():
    adding1 = int(input("Enter a number: "))
    adding2 = int(input("Enter a number: "))
    return adding1 + adding2

add1 = lambda a,b: a+b

print("Inside calc", __name__)
if __name__ == "__main__":
    print(f"calc file : {add()}")