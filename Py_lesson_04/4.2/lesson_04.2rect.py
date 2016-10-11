def calcPrim(length,width):
    return 2 * length + 2 * width


def surfPrint(length,width):
    print("The surface area of the rectangle is: ",calcPrim(length,width))


length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the length of the rectangle: "))
surfPrint(length,width)

