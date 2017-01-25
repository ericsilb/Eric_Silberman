
equation = input("Eqaution: ")
equ = equation.split(" ")
i = 0

while i < len(equ):
    if i < len(equ) and (equ[i] == "*" or equ[i] == "/"):
        if equ[i] == "*":
            equ[i] = int(equ[i-1]) * int(equ[i+1])
        else:
            equ[i] = int(equ[i-1]) / int(equ[i+1])
        equ.pop(i-1)
        equ.pop(i)
    else:

        i += 1
i = 0
while i < len(equ):
    if i < len(equ) and (equ[i] == "+" or equ[i] == "-"):
        if equ[i]=="+":
            equ[1] = int(equ[i-1]) + int(equ[i+1])
        else:
            equ[i] = int(equ[i-1]) - int(equ[i+1])
        equ.pop(i-1)
        equ.pop(i)
    else:
        i += 1

print(equ)
    
