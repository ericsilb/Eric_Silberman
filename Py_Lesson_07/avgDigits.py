number =  int(input("Number: "))

def avgDigits(num):
    dig = 0;
    avg = 0;
    while num > 0:
        dig += 1
        avg += (num % 10)
        num = int(num/10)
    return avg / dig


print("The average of the digits in",number,"is",avgDigits(number))


            





