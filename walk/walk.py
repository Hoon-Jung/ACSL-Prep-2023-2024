# 1. C, C7, 85, D6, 46, D7, E6, 87                          1. 2, 5
# 2. 2, 3, L, 2                                             2. 2, 5
# 3. 2, 7, B, 8                                             3. 6, 4
# 4. 4, 5, R, 3                                             4. 3, 7
# 5. 6, 7, A, 5                                             5. 6, 1
# 6. 8, 8, L, 7


r = "C, C7, 85, D6, 46, D7, E6, 87"
r = r.split(", ")
temp = [bin(int(row, 16))[2:].zfill(8) for row in r]
board = []
for rows in temp:
    t2 = []
    for col in rows:
        if col == "1":
            t2.append("1-1")
        else:
            t2.append("0")
    board.append(t2)

p = "2, 3, L, 2"
p = p.split(", ")
currentp = [int(p[0])-1, int(p[1])-1]
#directions: 0 = L, 1 = U, 2 = R, 3 = D
if p[2] == "L":
    direction = 0
elif p[2] == "A":
    direction = 1
elif p[2] == "R":
    direction = 2
elif p[2] == "B":
    direction = 3

def fixspot(spot, d):
    if spot[0] == 8:
        spot[0] = 0
    elif spot[0] == -1:
        spot[0] = 7
    if spot[1] == 8:
        spot[1] = 0
    elif spot[1] == -1:
        spot[1] = 7
    
    d = d % 4
    return spot, d


#directions: 0 = L, 1 = U, 2 = R, 3 = D
def movespot(spot, d):
    if d == 0:
        spot[1] -= 1
    elif d == 1:
        spot[0] -= 1
    elif d == 2:
        spot[1] += 1
    elif d == 3:
        spot[0] += 1
    

    return spot


for i in range(int(p[3])):
    if board[currentp[0]][currentp[1]] == "0":
        currentp = movespot(currentp, direction)
    elif board[currentp[0]][currentp[1]][0] == "1":
        direction += int(board[currentp[0]][currentp[1]][1:])
        board[currentp[0]][currentp[1]] = "1"+str(int(board[currentp[0]][currentp[1]][1:]) + 1)
        if int(board[currentp[0]][currentp[1]][1]) > 3:
            board[currentp[0]][currentp[1]] = "1-1"
        currentp, direction = fixspot(currentp, direction)
        currentp = movespot(currentp, direction)
    currentp, direction = fixspot(currentp, direction)
    
    

