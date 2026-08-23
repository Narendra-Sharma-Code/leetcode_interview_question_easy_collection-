# decoraters: gives extra functionality to existing functions without modifying their structure


def log(func):
    def wrap(*arg):
        print(f"values are {arg}")
        return func(*arg)
    return wrap

def greater_first(func):
    def wrap(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return wrap
    

@log
@greater_first
def devide(a,b):
    return a/b

result = devide(23,34)
print(result)