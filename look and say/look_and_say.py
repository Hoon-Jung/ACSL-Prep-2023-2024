#25 min
inp = input().split()
def updatenum(num):
    fd = [num[0], 0]
    fs = ""
    for i in range(len(num)):
        if fd[0] == num[i]:
            fd[1] += 1
        else:
            fs += str(fd[1]) + fd[0]
            fd = [num[i], 1]
    fs += str(fd[1]) + fd[0]
    return fs


term = 1
seq = "1"
while term < int(inp[0]):
    seq = updatenum(seq)
    term += 1


print(seq[int(inp[1])-1:int(inp[1]) + int(inp[2])])