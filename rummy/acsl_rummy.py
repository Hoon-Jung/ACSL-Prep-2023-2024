inp = '8H, 8C, 8S, 2C, 7S, 9H, KD'  # 8S, 8H, 8C, KD, 9H, 7S, 2C
inp = '3S, 4S, TD, 9S, KC, 5S, 6S'                           # 3S, 4S, 5S, 6S, KC, TD, 9S
inp = 'KS, JS, KH, JH, KC, JC, 6D'                          # JS, JH, JC, KS, KH, KC, 6D
inp= '5H, TD, 6H, JD, 7H, QD, 3C'                          # 5H, 6H, 7H, TD, JD, QD, 3C
inp= '2C, 2D, 4S, 6C, 7H, 7S, 8C'                            # 8C, 7S, 7H, 6C, 4S, 2C, 2D
inp= 'AH, 2H, 3H, 4H, 7S, TC, 9H'                          # AH, 2H, 3H, 4H, TC, 9H, 7S
inp= '3S, QC, 8H, 4H, 8D, 4C, 8C'                         # 8H, 8C, 8D, QC, 4H, 4C, 3S
inp= '5S, QS, 9C, 5H, TS, 5C, JS'                           #  TS, JS, QS, 5S, 5H, 5C, 9C
inp= '2S, 7D, 5H, JS, 9C, TH, 3C'                           # JS, TH, 9C, 7D, 5H, 3C, 2S
inp= '2S, 9D, 9S, 2H, 9C, 2C, 9H'                          # 9S, 9H, 9C, 9D, 2S, 2H, 2C <-- according to the rules the answer must be ['2S', '2H', '2C', '9S', '9H', '9C', '9D']

inp = [list(x) for x in inp.split(", ")]
print(inp)


def makenumbers(input):
    for i in range(len(input)):
        if input[i][0] == "A":
            input[i][0] = "1"
        if input[i][0] == "T":
            input[i][0] = "10"
        if input[i][0] == "J":
            input[i][0] = "11"
        if input[i][0] == "Q":
            input[i][0] = "12"
        if input[i][0] == "K":
            input[i][0] = "13"
        if input[i][1] == "S":
            input[i][1] = "4"
        if input[i][1] == "H":
            input[i][1] = "3"
        if input[i][1] == "C":
            input[i][1] = "2"
        if input[i][1] == "D":
            input[i][1] = "1"
        input[i] = list(map(int, input[i]))
    return input


def makeletters(input):
    for i in range(len(input)):
        if input[i][0] == 1:
            input[i][0] = "A"
        if input[i][0] == 10:
            input[i][0] = "T"
        if input[i][0] == 11:
            input[i][0] = "J"
        if input[i][0] == 12:
            input[i][0] = "Q"
        if input[i][0] == 13:
            input[i][0] = "K"
        if input[i][1] == 4:
            input[i][1] = "S"
        if input[i][1] == 3:
            input[i][1] = "H"
        if input[i][1] == 2:
            input[i][1] = "C"
        if input[i][1] == 1:
            input[i][1] = "D"
        input[i] = list(map(str, input[i]))
        input[i] = "".join(input[i])
    return input




def fourinarow(input):
    #return 4 in a row and then rest of input
    pass

def solverun(input):
    input.sort(key=lambda x: [x[1], x[0]])
    input.insert(0, [0, 0])
    prev = 0
    curr = 0
    temp = []
    run = []
    runlen = 0
    for i in range(1, len(input)):
        curr = input[i][1]
        if curr == prev and input[i][0] - 1 == input[i-1][0]:
            runlen += 1
            if temp == []:
                temp.append(input[i-1])
                temp.append(input[i])
            else:
                temp.append(input[i])
        else:
            if runlen >= 2:
                run.append(temp.copy())
            temp = []
            runlen = 0
        prev = input[i][1]
    if runlen >= 2:
        run.append(temp.copy())
    return run


def solveset(input):
    input.sort()
    input.insert(0, [0, 0])
    prev = 0
    curr = 0
    temp = []
    sets = []
    setlen = 0
    for i in range(1, len(input)):
        curr = input[i][0]
        if curr == prev:
            setlen += 1
            if temp == []:
                temp.append(input[i-1])
                temp.append(input[i])
            else:
                temp.append(input[i])
        else:
            if setlen >= 2:
                temp.sort(key=lambda x: x[1], reverse=True)
                sets.append(temp.copy())
            temp = []
            setlen = 0
        prev = input[i][0]
    if setlen >= 2:
        temp.sort(key=lambda x: x[1], reverse=True)
        sets.append(temp.copy())
    return sets


def combine(sets, runs, input):
    ans = []
    if len(runs) >= 1:
        if len(runs) == 2:
            if runs[0][0][0] > runs[1][0][0]:
                ans += runs[1]
                ans += runs[0]
            else:
                ans += runs[0]
                ans += runs[1]
        elif len(runs) == 1:
            ans += runs[0]
    if len(sets) >= 1:
        if len(sets) == 2:
            if sets[0][0][0] > sets[1][0][0]:
                ans += sets[1]
                ans += sets[0]
            else:
                ans += sets[0]
                ans += sets[1]
        elif len(sets) == 1:
            ans += sets[0]
    input.sort(reverse=True)
    for j in range(len(input)):
        if input[j] not in ans:
            ans.append(input[j])
    return ans[:-1]



inp = makenumbers(inp)
print(makeletters(combine(solveset(inp), solverun(inp), inp)))