word1 = input("Enter three words: ")
word2 = input("Enter three words: ")
word3 = input("Enter three words: ")

def makeCenter(word):
    if len(word) >= 20:
        return word
    else:
        return makeCenter(" " + word + " ")

print(makeCenter(word1))
print(makeCenter(word2))
print(makeCenter(word3))
