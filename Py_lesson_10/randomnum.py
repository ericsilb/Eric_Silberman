import random
numList = []
for loop in range(0,4):
    numList.append([])
    for i in range(0,4):
        r = random.randint(0, 100)
        numList[loop].append(r)
for nums in numList:
    output = ""
    for num in nums:
        output+= str(num) + " "
    print(output)
   
