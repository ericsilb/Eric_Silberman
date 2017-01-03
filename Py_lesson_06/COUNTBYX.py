


to= int(input("What number do you want to count up to: "))
by= int(input("What number do you want to count by: "))
output = ""
def printPat(output):
    global to, by
    for i in range(by, to+1, by):
        output+= str(i) + "\t"
    return output
    
print(printPat(output))
