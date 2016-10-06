r = int(input("What is the radius of your spehere:"))
area = 0
import math
math.pi

def calcArea():
        global r,area
        area = 4*math.pi*(r**2)

calcArea()
print("{:>0}{:3.5f}".format("The area of your sphere is :",area))

