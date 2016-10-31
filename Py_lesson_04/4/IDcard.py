def format (item1,sitem1):
    print("*""{:<10}{:<10}""           *".format(item1, sitem1))


item2= input("Enter your first name:")
sitem2= input("Enter your last name:")
item1 = input("Enter your school site:")
sitem1 = int(input("Enter the school year:"))
sitem3= input("Enter your subject:")
item3= input("Enter your title:")

print("*" * 33)
format(item1, sitem1)
format(item2, sitem2)
format(item3, sitem3)
print("*" * 33)





