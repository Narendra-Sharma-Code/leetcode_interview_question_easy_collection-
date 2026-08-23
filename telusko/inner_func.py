def outer():
    print("In outer function")
    def inner():
        print("In inner function")

    return inner
something = outer()
something()

def greet():
    def message():
        print("Welcome to Python")

    return message

mesg = greet()
mesg()