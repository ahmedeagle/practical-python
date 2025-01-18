#A method that has not yet been invoked by the function call operator () 
# is known as a bound method. It operates on the instance where it originated.

class Stock:
    def __init__(self,name,shares,price):
        self.name=name
        self.shares=shares
        self.price=price
    def cost(self):
        return self.price * self.shares
        
s = Stock('GOOG', 100, 490.10)
c = s.cost  # bounded method not called yet 
print(c) 

print(c())  #called method
