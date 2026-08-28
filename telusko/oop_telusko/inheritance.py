class parent:
    def property1(self):
        print("prop 1")

    def property2(self):
        print("prop 2")

class child(parent):
    def property3(self):  
        print("prop 3")

    def property4(self):
        print("prop 4")    

class Grandchild(child,parent):
    def property5(self):
        print("prop 5")

    def property6(self):
        print("prop 6")    


wealth = Grandchild()
wealth.property4()

wealth1 = child()
wealth1.property1()
