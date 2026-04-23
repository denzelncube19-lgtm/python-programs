class stocks:
    def __init__(self,name,price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def update_price(self,new_price):
        self.price += new_price
    
    def update_quantity(self,new_quantity):
        self.quantity += new_quantity

    def display(self):
        print("name : ",self.name)
        print("price : ",self.price)
        print("quantity : ",self.quantity)
        print("total stocks is :", self.quantity * self.price)

stock1 = stocks("car",500,2)
stock2 = stocks("laptops",30,50)
print("\n")
stock1.display()
stock2.display()
print("\n")
print("updated stock\n")
stock1.update_price(-200)
stock2.update_quantity(4)
stock1.display()
stock2.display()