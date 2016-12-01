sent = input("Sentence: ")
def replace(sent):
    if not (" ") in sent:
        return sent
    else:
        return sent[0:sent.index(" ")] + "_" + replace(sent[sent.index(" ") + 1:len(sent)])

print(replace(sent))

