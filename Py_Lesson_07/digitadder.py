number =  int(input("Number: "))
Sum = 0
num = number

while num > 0:
    Sum += num % 10
    num = int(num/10)

print("The sum of the digits in",number,"is",Sum)
