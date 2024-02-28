from itertools import permutations

inp = input().split(", ")
iterlist = [i+1 for i in range(len(inp[0]))]
table = [[[] for _ in range(len(inp[0]))] for _ in range(len(inp[0]))]
iterlist = list(permutations(iterlist))
possibles = set()
pdict = {}
alrprinted = False

for j in range(len(iterlist)):
    possibles.add(iterlist[j][:2])

possibles.add((2, 2))
possibles.add((3, 3))
for pair in possibles:
    pdict[str(pair[0]) + str(pair[1])] = []


def scan(numlist):
    lcount = 0
    lmax = 0
    rcount = 0
    rmax = 0
    for i in range(len(numlist)):
        if numlist[i] > lmax:
            lmax = numlist[i]
            lcount += 1
        if numlist[-i-1] > rmax:
            rmax = numlist[-i-1]
            rcount += 1
    return str(lcount) + str(rcount)


for b in range(len(iterlist)):
    pdict[scan(iterlist[b])].append(iterlist[b])



for j in range(len(inp[0])):
    for m in range(len(pdict[str(inp[0][j]) + str(inp[-1][j])])):
        for l in range(len(pdict[str(inp[0][j]) + str(inp[-1][j])][m])):
            table[l][j].append(pdict[str(inp[0][j]) + str(inp[-1][j])][m][l])
for m in table:
    print(m)



def validate(indexes):
    for v in range(len(indexes)):
        for c in range(len(pdict[inp[v+1]])):
            currpossible = True
            for x in range(len(pdict[inp[v+1]][c])):
                if pdict[inp[v+1]][c][x] != table[v][x][indexes[x]]:
                    currpossible = False
                    break
            if currpossible:
                break
        if not currpossible:
            return False
    return True
        


def printind(inds,printed):
    if not printed:
        for m in range(len(inp[0])):
            ans = ""
            for l in range(len(inp[0])):
                ans += str(table[m][l][inds[l]])
            print(ans)
        printed = True
    return printed



for p in range(len(inp[0])):
    for r in range(len(pdict[inp[p+1]])):
        kg = True
        arr = []
        for o in range(len(pdict[inp[p+1]][r])):
            if pdict[inp[p+1]][r][o] not in table[p][o]:
                kg = False
                break
            else:
                temp = []
                for m in range(len(table[p][o])):
                    if table[p][o][m] == pdict[inp[p+1]][r][o]:
                        temp.append(m)
                arr.append(temp)

        if len(arr) == len(inp[0]):
            for ind1 in arr[0]:
                for ind2 in arr[1]:
                    for ind3 in arr[2]:
                        for ind4 in arr[3]:
                            if len(arr) == 5:
                                for ind5 in arr[4]:
                                    if validate([ind1, ind2, ind3, ind4, ind5]):
                                        alrprinted = printind([ind1, ind2, ind3, ind4, ind5], alrprinted)
                            else:
                                if validate([ind1, ind2, ind3, ind4]):
                                    alrprinted = printind([ind1, ind2, ind3, ind4], alrprinted)
