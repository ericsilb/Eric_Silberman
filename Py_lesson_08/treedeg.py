word = input("Word: ")
start = 0
stop = len(word)
def tree(word,start,stop):
    if start <= stop:
        print(("{:>10}".format(word[0:start])))
        start+=1
        return tree(word,start,stop)
    else:
        return ""

    
print(tree(word,start,stop))


