intList = []
import random
for i in range(0,10):
    intList.append(str(random.randint(1,100)))
print(intList)
output = ""
for i in intList:
    output = output +  i + " "
print(output)
print("\n")

def average(intList):
    Int = 0
    Sum = 0
    for i in intList:
        Int += int(i)
        Sum+=1
    return str(Int/Sum)
print("The average of the above numbers is…", average(intList))
