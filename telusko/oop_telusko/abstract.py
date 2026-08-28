from abc import ABC,abstractmethod

class abs(ABC):
    @abstractmethod
    def pay(self):
        pass

class razorpay(abs):
    def pay(self):
        print("razorpay used")


class purchase:
    def __init__(self,gateway):
        self.gateway = gateway
        
    def mode_of_pay(self):
        print(f"using payment method")
        self.gateway.pay()

online_pay = razorpay()
gateway1 = purchase(online_pay)

gateway1.mode_of_pay()