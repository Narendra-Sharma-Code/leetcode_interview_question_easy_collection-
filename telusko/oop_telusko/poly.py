class laptop:
    def build(self):
        print("Laptop builds..")


class Desktop:
    def build(self):
        print("cyber cafe")


class Tablet:
    def surfing(self):
        print("Watching..")
class Developer:
    def code(self,machine :laptop):
        print("Developing..")
        machine.build()

mac = laptop()
lenovo = Desktop()
samsung = Tablet()

startup = Developer()
# startup.code(mac)
startup.code(lenovo)  
# startup.code(samsung)