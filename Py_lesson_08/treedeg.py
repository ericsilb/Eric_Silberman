word = input("Word: ")
start = 0
stop = len(word)
def tree(word,start,stop):
    if start <= stop:
        print(word[0:start])
        start+=1
        return tree(word,start,stop)
    else:
        print ("")

    
print(tree(word,start,stop))

