class method:
    brand = "MAC"
    #{🟢. Instance method
    def __init__(self, name,storage,model):
        self.name = name
        self.storage = storage
        self.model = model
    def production(self):
        print(f"The latest model of our barnd is {self.name} &  model is {self.model} it has {self.storage} of storage ")

    # }🔴
    @classmethod
    def info(self):
        return self.brand

    @staticmethod
    def gb_to_bytes(gb):
        return gb * (1024 **3)


launch = method("MAC","2TB","Latest 3.10")

launch.production()
launch.info()

print(method.info())

print(method.gb_to_bytes(16))