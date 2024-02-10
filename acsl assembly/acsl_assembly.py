#make dictionary and add all variables and like the transition names like DONE and then call them on the indexes ykwim
inps = list(map(int, input().split()))
acc = 0
variables = {}
allcode = []
while True:
    code = input().split()
    if code == []:
        break
    allcode.append(code)


def goto(locsearch):
    for i in range(len(allcode)):
        if locsearch == allcode[i][0]:
            return i
    else:
        return -1


ind = 0
end = ""
while True:
    if "DC" in allcode[ind]:
        variables[allcode[ind][0]] = int(allcode[ind][2])
    elif "LOAD" in allcode[ind]:
        if allcode[ind][1][0] == "=":
            acc = int(allcode[ind][-1][1:])
        else:
            acc = variables[allcode[ind][-1]]
    elif "READ" in allcode[ind]:
        variables[allcode[ind][-1]] = inps.pop(0)
    elif "STORE" in allcode[ind]:
        variables[allcode[ind][-1]] = acc
    elif "MULT" in allcode[ind]:
        if allcode[ind][1][0] == "=":
            acc = acc * int(allcode[ind][-1][1:])
        else:
            acc = acc * variables[allcode[ind][-1]]
    elif "DIV" in allcode[ind]:
        if allcode[ind][1][0] == "=":
            acc = acc // int(allcode[ind][-1][1:])
        else:
            acc = acc // variables[allcode[ind][-1]]
    elif "ADD" in allcode[ind]:
        if allcode[ind][1][0] == "=":
            acc += int(allcode[ind][-1][1:])
        else:
            acc += variables[allcode[ind][-1]]
    elif "SUB" in allcode[ind]:
        if allcode[ind][1][0] == "=":
            acc -= int(allcode[ind][-1][1:])
        else:
            acc -= variables[allcode[ind][-1]]
    elif "BG" in allcode[ind]:
        if acc > 0:
            ind = goto(allcode[ind][-1])
            continue
    elif "BL" in allcode[ind]:
        if acc < 0:
            ind = goto(allcode[ind][-1])
            continue
    elif "BE" in allcode[ind]:
        if acc == 0:
            ind = goto(allcode[ind][-1])
            continue
    elif "BU" in allcode[ind]:
        ind = goto(allcode[ind][-1])
        continue
    elif "END" in allcode[ind]:
        break
    ind += 1

print(acc)