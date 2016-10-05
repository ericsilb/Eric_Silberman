def main(h,l,w):
    return float((h*l*w)/1728)

h = int(input("Enter the height of the box in inches: "))
l = int(input("Enter the length of the box in inches: "))
w = int(input("Enter the length of the box in inches: "))

print("The volume of your box is", main(h,l,w), "cubic feet")


