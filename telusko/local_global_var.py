a = 34          # Global variable
def func():
    a = 23      # Local variable
    globals()["a"] = 56  #using we can access global variable and change it's value insidea function
    print(f"inside : {a}")

func()
print(f"outside : {a}")

          
