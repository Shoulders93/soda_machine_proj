class Coin:
    def __init__(self, name, value):
        self.name = name
        self.value = value


#Removed parameters from super init
class Penny(Coin):
    def __init__(self):
        super().__init__("Penny", 0.01)

class Nickel(Coin):
    def __init__(self):
        super().__init__("Nickel", 0.05)

class Dime(Coin):
    def __init__(self):
        super().__init__("Dime", 0.10)

class Quarter(Coin):
    def __init__(self):
        super().__init__("Quarter", 0.25)



