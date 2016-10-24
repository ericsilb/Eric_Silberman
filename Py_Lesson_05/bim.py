w = float(input("please enter your weight in pounds: " ))
h = float(input("please enter your height in inches: "))
Bmi = (703 * w)/h**2

print("Your bmi :",Bmi)

if Bmi < 18.5:
    print("You are underweight")

if 18.5< Bmi <24.9:
    print("You are normal")

if 25< Bmi <29.9:
    print("You are overweight")

if 29.9< Bmi <334.9:
    print("you are obese")

if 35< Bmi <39.9:
    print("You are very obese")

if Bmi> 39.9:
    print("You are morbidly Obese")


