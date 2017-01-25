class Car:
     def __init__(self, p,i,e,t):
         self.paint = p
         self.interior = i
         self.engine = e
         self.tires = t
     def setCustom(self, p,i,e,t):
         self.paint = p
         self.interior = i
         self.engine = e
         self.tires = t
         
     def getPaint(self):
          return self.paint
     
     def getInterior(self):
          return self.interior
     
     def getEngine(self):
          return self.engine
     
     def getTires(self):
          return self.tires

def Main():
    p = input("paint: ")
    i = input("interior: ")
    e = input("engine: ")
    t = input("tires: ")
    new = Car(p,i,e,t)
    print("Your vehicle is ready......")
    print("Paint:        ",new.getPaint())
    print("Interior:     ",new.getInterior())
    print("Engine:       ",new.getEngine())
    print("Tires:     ",new.getTires())
    print("\n")
          
Main()
class Human:
    def __init__(self,h,e,s):
        self.hair = h
        self.eyes = e
        self.skin = s
    def setHES(self,h,e,s):
        self.hair = h
        self.eyes = e
        self.skin = s
          
    def getHair(self):
         return self.hair
     
    def getEyes(self):
         return self.eyes
     
    def getSkin(self):
         return self.skin

def main():
    hair = input("Hair: ")
    eyes = input("Eyes: ")
    skin = input("Skin: ")
    new2 = Human(hair,eyes,skin)
    print("My info...")
    print("Hair  ",new2.getHair())
    print("Eyes: ",new2.getEyes())
    print("Skin: ",new2.getSkin())
    new2.setHES("red","orange", "yellow")
    print("Friends info: ")
    print("Hair: ",new2.getHair())
    print("Eyes: ",new2.getEyes())
    print("Skin: ",new2.getSkin())
main()
          
          
     
    
          
