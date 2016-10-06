cubeS = int(input("Enter the value of the side: "))
surfaceA = 0

def calcSurf():
    global cubeS,surfaceA
    surfaceA = 6 * (cubeS)**2


calcSurf()
print("Your surface area is: ",surfaceA)
