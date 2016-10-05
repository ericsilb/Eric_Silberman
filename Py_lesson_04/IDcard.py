namef= input("Enter your first name:")
namel= input("Enter your last name:")
school = input("Enter your school site:")
year = int(input("Enter the school year:"))
sub = input("Enter your subject:")
title= input("Enter your title:")

print("*" * 33)
print("*""{:<15}{:<6}""          *".format(school, year))
print("*""{:<10}{:<10}""           *".format(namef, namel))
print("*""{:<10}{:<10}"" *".format(title, sub))
print("*" * 33)

