#42 mins
inp = input().split()

row = int(inp.pop(0))
col = int(inp.pop(0))
rows = []

for i in range(row):
    l = len(inp[i])
    rows.append(bin(int(inp[i], 16))[2::].zfill(l*4)[0:col])


def makeSub(r, c, l):
    sub = []
    for i in range(r+1):
        sub.append(l[i][0:c+1])
    return sub


def checkSub(sub, srows, l):
    row = 0
    if len(l[0]) % len(sub[row]) != 0:
        return False
    if len(l) % len(sub) != 0:
        return False
    for i in range(len(l)):
        if l[i] != (sub[row] * int((len(l[i]) / len(sub[row])))):
            return False
        row += 1
        if row >= srows:
            row = 0
    return True
    

answers = []
for r in range(row):
    for c in range(col):
        sub = makeSub(r, c, rows)
        if checkSub(sub, len(sub), rows):
            answers.append([r+1, c+1])


lowest = [answers[0][0] * answers[0][1], answers[0][0], answers[0][1]]
for i in range(len(answers)):
    if answers[i][0] * answers[i][1] < lowest[0]:
        lowest[0] = answers[i][0] * answers[i][1]
        lowest[1] = answers[i][0]
        lowest[2] = answers[i][1]

print(lowest[1], lowest[2])