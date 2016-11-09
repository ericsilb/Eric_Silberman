num =int(input("Please enter number: "))
fact = 1
def factorial():
    global fact
    for i in range(1, num+1):
        fact *= i
    print (fact)

factorial()
