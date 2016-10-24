def passCheck(user,password,userR,passwordR):
    if  userR==user and password == passwordR:
        print("You are granted access!")
    elif user != userR and password != passwordR:
        print("Your password and username are worng!")
    elif user != userR:
        print("Your username is wrong!")
    elif password != passwordR:
        print("Your password is wrong!")
    elif user != userR and password != passwordR:
        print("Your password and username are worng!")



user = input("Enter the User name: ")
password = input("Enter the password: ")
userR = "Tphs"
passwordR = "Falcons"
passCheck(user,password,userR,passwordR)
    
    
            
            
            

    

