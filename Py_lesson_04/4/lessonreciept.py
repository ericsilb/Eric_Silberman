def format(item, price):
    print("* {:>20} .......     {:<11.3}".format(item, price))

item1 = input("Please enter item 1: ")
price1 = float(input("Please enter price: "))
item2 = input("Please enter item 2: ")
price2 = float(input("Please enter price for item 2: "))
item3 = input("Please enter item 3: ")
price3 = float(input("Please enter price for item 3: "))
subtotal =(price1 + price2 + price3)
tax = (0.08 * subtotal)
total=(subtotal + tax);


print("<<<<<<<<<<_Reciept_>>>>>>>>>>>>")


format(item1, price1)
format(item2, price2)
format(item3, price3)


format("Subtotal: ", subtotal)
format("Tax: " , tax)
format("Total: " , total)
print("____________________________")
print("*Thank you for your support *")
