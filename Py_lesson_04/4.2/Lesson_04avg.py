def calcAvg(num1,num2,num3):
    return (num1 + num2 + num3)/3

def avgPrint(num1,num2,num3):
    print("The avg of these numbers is ",calcAvg(num1,num2,num3))
    

num1 = int(input("Please enter num 1: "))
num2 = int(input("Please enter num 2: "))
num3 = int(input("Please enter num 3: "))
avgPrint(num1,num2,num3)
