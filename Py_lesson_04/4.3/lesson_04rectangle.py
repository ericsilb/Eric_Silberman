length = int(input("Legth of rectangle: "))
width = int(input("Width of rectangle: "))
perim = 0

def calcPerim():
    global length,width,perim
    perim = (length * 2) + (width * 2)

calcPerim()
print(perim)
            
