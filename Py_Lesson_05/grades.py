def calcPoints(grade):
    if grade == "A":
        return 4.0

    if grade =="B":
        return 3.0
    
    if grade =="C":
        return 2.0

    if grade =="D":
        return 1.0

    if grade=="F":
        return 0


gradeMath = input("Please enter the grade for this class :")
gradeEng = input("Please enter the grade for this class :")
gradeSci = input("Please enter the grade for this class :")
gradeLan = input("Please enter the grade for this class :")
gradeHis = input("Please enter the grade for this class :")
gradeArt = input("Please enter the grade for this class :")
gradePe = input("Please enter the grade for this class :")

gPoints = (calcPoints(gradeEng)+ calcPoints(gradeMath)+calcPoints(gradeSci)+calcPoints(gradeLan)+calcPoints(gradeHis)+calcPoints(gradeArt)+calcPoints(gradePe))/7
print("Your GPA: ",gPoints)
