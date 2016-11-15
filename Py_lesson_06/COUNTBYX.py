
to= int(input("What number do you want to count up to: "))
by= int(input("What number do you want to count by: "))

def printPat():
    global to, by
    for i in range(by, to+1, by):
        print(i)
    
printPat()
