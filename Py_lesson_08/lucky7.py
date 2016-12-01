num = int(input("Number: "))
def lucky(num):
    if num > 0:
        if (num % 10) == 7:
            return 1 + lucky (int(num/10))
        else:
            return 0 + lucky (int(num/10))

    else:
        return 0

print(lucky(num))

