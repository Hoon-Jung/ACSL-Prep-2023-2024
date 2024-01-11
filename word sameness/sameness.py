# BLAMEABLENESSES BLAMELESSNESSES --> -35
# MEZZAMINES RAZZMATAZZ --> -5
# ABBREVIATIONS ABBREVIATORS --> -4
# ABCDEFGHIJKLMNO ABKCLDZZHQJWWLX --> -86
# ABCDEFGHIJKL ABXEWFRRH --> -52


inp = "ABCDEFGHIJKLMNO ABKCLDZZHQJWWLX"
inp = inp.split()
w1 = list(inp[0])
w2 = list(inp[1])

def sameindex(w1, w2):
    removes = []
    for i in range(len(w1)):
        try:
            if w1[i] == w2[i]:
                removes.append(i)
            else:
                pass
        except:
            pass
    
    for j in range(len(removes)):
        w1.pop(removes[j]-j)
        w2.pop(removes[j]-j)

    return w1, w2


def infront(w1, w2):
    for i in range(len(w1)):
        try:
            if w1[i] == w2[i+1]:
                return i
        except:
            return -1
    return -1


keepgoing = True
while keepgoing:
    w1, w2 = sameindex(w1, w2)
    if infront(w1, w2) != -1:
        if (infront(w2, w1) < infront(w1, w2)) and (infront(w2, w1) != -1):
            w1.pop(infront(w2, w1))
        elif (infront(w2, w1) == infront(w1, w2)):
            w2.pop(infront(w1, w2))
        else:
            w2.pop(infront(w1, w2))
    elif infront(w2, w1) != -1:
        w1.pop(infront(w2, w1))
    else:
        keepgoing = False



score = 0
for i in range(len(w2)):
    if i >= len(w1):
        score += 1
    else:
        score += ord(w1[i]) - ord(w2[i])


if len(w1) > len(w2):
    score += len(w1) - len(w2)
print(score)