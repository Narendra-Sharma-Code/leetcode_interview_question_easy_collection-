class computer:
    def config(self):
        print("Mac book m1 series")

com1 = computer()
com2 = computer()
print(type(com1))

# computer.config(com1)     # behind the scene how it works 

com1.config()



#Task lec 43
class laptop:
    def details(self,brand, ram):
        print(f"brand name {brand} {ram}")

lap1 = laptop()
lap1.details("Dell","16GB")

lap2 = laptop()
lap2.details("HP","8GB")

