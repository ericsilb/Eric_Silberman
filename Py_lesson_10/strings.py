go = input("Please enter 16 Strings: ")
wordsList = []
spList = go.split(" ")
spot = 0
for i in range(0,4):
    output = ""
    wordsList.append([])
    for j in range(0,4):
         wordsList[i].append(spList[spot])
         output += str(wordsList[i][j]) + " "
         spot+= 1
    print(output)
    
           
