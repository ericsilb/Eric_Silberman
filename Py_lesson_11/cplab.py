class MilesPerHour:
    def __init__(self, d,h,m):
        self.distance = d
        self.hours = h
        self.minutes = m
        self.mph = 0
    def setValues(self, d,h,m):
        self.distance = d
        self.hours = h
        self.minutes = m
        self.mph = 0
    def getDist(self):
        return self.distance
    def getHours(self):
        return self.hours
    def getMins(self):
        return self.minutes
    def getMPH(self):
        self.mph = self.distance/(self.hours + self.minutes / 60.0)
        return self.mph

def main():
    distance =int(input("Distance: "))
    hours =int(input("Hours: "))
    minutes =int(input("Minutes: "))
    new = MilesPerHour(distance, hours, minutes)

    print("If you travel ", new.getDist(), " miles in ", new.getHours(), " and ", new.getMins(), " minutes, you are traveling at ", new.getMPH(), " mph.")


main()
    

    

     
