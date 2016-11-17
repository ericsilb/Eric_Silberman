number = int(input("Number: "))

def getReverse(num):
    rev = 0;
    while num > 0:
        rev *= 10
        rev += (num % 10)
        num = int(num/10)
    return rev

print(number,"reversed is",getReverse(number))
