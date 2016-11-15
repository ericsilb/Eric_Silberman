import math
math.pi

def calcArea(r):
 return 4 * math.pi * (r**2)

def areaPrint(area):
    print("{:>0}{:3.5f}".format("The area of your sphere is :",calcArea(r)))


r = int(input("Enter the radius of your sphere : "))
areaPrint(r)
