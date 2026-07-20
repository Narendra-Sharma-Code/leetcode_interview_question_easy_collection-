class Car:
    def __init__(self, model, brand, launched_yr, color):
        self.model = model
        self.brand = brand
        self.launched_yr = launched_yr
        self.color = color
    def start(self):
        print(f"You Chose a car which is {self.model} {self.brand} {self.launched_yr} {self.color}")
    
my_car = Car("Defender", "RangRover", "2026", "Red")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.launched_yr)
# print(my_car.color)
my_car.start()


