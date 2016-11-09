count= int(input("How much do you want to count up: "))
x= int(input("By how much do you want to count up: "))

def printPat():
    for i in range(0, count, x):
        print(i)
    
printPat()
