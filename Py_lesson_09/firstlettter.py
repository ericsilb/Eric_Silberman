wordList = ["Math","Science","Englih","Biology","Compt"]
line = ""
def runfirst(line):
    for i in wordList:
        line += i[0]
    return line
print(runfirst(line))

