import math
class Distance:
     def __init__(self, x1,y1,x2,y2):
         self.xOne = x1
         self.yOne = y1
         self.xTwo = x2
         self.yTwo = y2
         self.distance = 0
     def setValues(self, x1,y1,x2,y2):
         self.xOne = x1
         self.yOne = y1
         self.xTwo = x2
         self.yTwo = y2
         self.distance = 0

     def getDist(self):
          self.distance = math.sqrt((self.xTwo-self.xOne)*(self.xTwo-self.xOne)+(self.yTwo-self.yOne)*(self.yTwo-self.yOne));
          return self.distance
     def getxOne(self):
          return self.x1
     
     def getxTwo(self):
          return self.x2
     
     def getyOne(self):
          return self.y1
     
     def getyTwo(self):
          return self.y2
def main():
     x1 = int(input("x1: "))
     y1 = int(input("y1: "))
     x2 = int(input("x2: "))
     y2 = int(input("y2: "))
     new = Distance(x1,y1,x2,y2)
     new.getDist()
     print("distance = ", new.getDist())
main()
