start = int(input("Please enter your starting number: "))
seq = int(input("Please enter your sequence size: "))
seqList = []

for i in range (0,seq):
    seqList.append(0)
    if i == 0 or i == 1:
        seqList[i]= start
    else:
        seqList[i] = (seqList[i-2]+seqList[i-1])
print(seqList)
        
        
