import random

class User:
   def __init__(self, fName, lName, avat = ""):
       self.firstName = fName
       self.lastName = lName
       self.avatar = avat
       self.userID = random.randint(0, 1000000)

   def __str__(self):
       return "Customer Info...\nFirst Name: " + self.firstName + \
                               "\nLast Name: " + self.lastName + \
                               "\nAvatar: " + self.avatar + \
                               "\nUser ID#: " + str(self.userID)
def main():
    firstName = input("Firstname: ")
    lastName = input("Last name: ")
    user1= User(firstName, lastName)
    x = input("Would you like to use a public avatar? (y or n)")

    if x == "n":
        user1 =User(firstName,lastName)
    else:
        avatar = input("Avatar name: ")
        user1 =User(firstName,lastName,avatar)
    print(user1.__str__())
main()
        
