size = int(input("Size of the table: "))
inte = int(input("Iteger: "))

def printGraph():
    for i in range(1,size,1):
        x = i * inte
        print("{:>5.1f} | {:<10.1f}".format(i,x))

printGraph();
    

