class ios:
    brand = "Apple"
    def __init__(self,device,chip,color,screen):
        print("This is a init method")
        self.device = device
        self.chip = chip
        self.color = color
        self.screen = screen
        
    def computer(self):
        print(f"Device: {self.device}")

laptop = ios("HP","i5","Black","15 inch")
laptop.computer()
print(laptop.brand,laptop.device,laptop. chip,laptop.color,laptop.screen)  
