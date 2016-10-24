def format(item, price):
    print("* {:>20} .......     {:<11.3}".format(item, price))

def discount(sub):
    if subtotal >= 2000:
        return sub * 0.15

    if not subtotal >= 2000:
        return 0

item1 = input("What is item 1: ")
price1=float(input("What is the price for 1: "))
item2 = input("What is item 2: ")
price2=float(input("What is the price for 2: "))
item3 = input("What is item 3: ")
price3=float(input("What is the price for 3: "))
item4 = input("What is item 4: ")
price4=float(input("What is the price for 4: "))
subtotal = price1+price2+price3+price4
tax = 0.08*subtotal
total = discount(subtotal) + subtotal + tax


print("<<<<<<<<<<<< Receipt >>>>>>>>>>>>>>")
format(item1, price1)
format(item2, price2)
format(item3, price3)
format("Subtotal: ", subtotal)
format("Tax: " , tax)
format("Total: " , total)
print("____________________________")
print("*Thank you for your support *")    
