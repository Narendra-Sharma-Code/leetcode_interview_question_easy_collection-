class abc:
    def __new__(cls):
        print("constructor called")         #behind the scene by default constructor is called when we create an object of class but by default we are overding by the built me function called __new__ and we are not calling the init method by default so we have to call it explicitly if we want to call it            
        return super().__new__(cls)  #this is the default constructor of the class which is called when we create an object of the class 

    def __init__(self):
        
        print("init called")

    def show(self):
        print("in show")

object1 = abc()             #() is kinda constructor 
object1.show()        #one method(type) of calling show object but in this by default init method will get called 

object2 = abc.__new__(abc)   # this is another way of creating an object and this init method is not called bydefault & __new__ is a built in method and we can modify it by our preference and we can call it explicitly if we want to call it
object2.show()
object2.__init__()          # we have to call the init method explicitly if we want to call it
