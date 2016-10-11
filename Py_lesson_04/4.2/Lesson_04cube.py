def calcSurfA(cubeS):
    return 6 * (cubeS)**2

def surfPrint(cubeS):
    
    print("{:>0}{:3.5f}".format("The surface area of the cube is: ",calcSurfA(cubeS)))


cubeS = int(input("Please enter the side of the cube: "))
surfPrint(cubeS)
