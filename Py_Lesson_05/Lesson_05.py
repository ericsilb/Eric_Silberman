import random 
playerR = random.randint(1,6)
comptR = random.randint(1,6)

print("You rolled a",playerR)
print("Computer rolled a",comptR)

def rollDice():
     global playerR,comtR

if playerR > comptR:

    print("The winner is player!")

if not playerR > comptR:
    print("The winner is computer!")



