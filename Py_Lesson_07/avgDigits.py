number =  int(input("Number: "))
dig = 0
avg = 0

def avgDigits():
    global dig,avg
    num = number
    while num > 0:
        dig += 1
        avg += num % 10
        num = int(num/10)

print("The average of the digits in",number,"is",avgDigits(avg))
avgDigits()

            

