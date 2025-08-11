class SimpleCoffee:
    def cost(self) -> int:
        return 100
    
    def desc(self) -> str:
        return "черный кофе"
    

class CoffeeDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()
    
    def desc(self):
        return self._coffee.desc()
    

class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 10
    
    def desc(self):
        return super().desc() + " с молоком"
    
class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 5
    
    def desc(self):
        return super().desc() + " с сахаром"
    

class SyrupDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 30
    
    def desc(self):
        return super().desc() + " с сиропом"
    


coffee = MilkDecorator(SugarDecorator(SimpleCoffee()))

print(coffee.cost(),coffee.desc())


coffee = SimpleCoffee()
print(coffee.cost(),coffee.desc())

coffee = SyrupDecorator(MilkDecorator(SugarDecorator(SimpleCoffee())))
print(coffee.cost(),coffee.desc())