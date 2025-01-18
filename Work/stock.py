class Stock:
    def __init__(self,name,shares,price):
        self.name=name
        self.shares=shares
        self.price=price
    def cost(self):
        return self.price * self.shares
    def sell(self):
        return self.shares

stocka = Stock('GOOG',100,490.10)
stockb = Stock('GOOd',200,490.10)
stockc = Stock('GOOc',300,490.10)


listofstocks = [stocka,stockb,stockc]

print(stocka.cost())
print(stocka.sell())
