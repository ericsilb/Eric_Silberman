import random
class Inventor:
    def __init__(self,manu, n, cat = "", price = ""):
        self.manufacturer = manu
        self.name = n
        self.category = cat
        self.upc = random.randint(0,100000)
        self.price = price

    def resetVals(self,manu, n, cat,upc, price):
        self.manufacturer = manu
        self.name = n
        self.category = cat
        self.upc = random.randint(0,100000)
        self.price = price

    def __str__(self):
        return "Item Info...\Manufacturer: " + self.manufacturer + \
        "\nName: " + self.name + \
        "\nCategory: " + self.category + \
        "\nUPC: " + str(self.upc) + \
        "\nPrice: " + str(self.price)
                  
def main():
    name = input("Name :")
    manu = input("Manufacturer: ")
    x = input("Will you be entering category and price information? (y or n)")
    if x == "n":
        item1= Inventor(manu,name)
    else:
        cat= input("Category: ")
        price = input("Price: ")
        item1 = Inventor(manu,name,cat,price)
    print(item1.__str__())
main()
            
    
    
