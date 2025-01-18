# super() allows you to access methods and attributes from the parent class in the child class.
# It helps avoid duplicating code when the child class needs to reuse or extend functionality from the parent class.

class Stock:
    def __init__(self, shares, price):
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price  # Calculate total cost
    
class MyStock(Stock):
    def cost(self):   #override
        # Call the parent class's `cost` method using `super()`
        actual_cost = super().cost()
        # Add 25% extra cost
        return 1.25 * actual_cost

mystock = MyStock(2323,3434)   # this calss should add the init arguments
print(mystock.cost())      