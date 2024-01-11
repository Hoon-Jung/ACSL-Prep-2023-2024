# 1.  2 434 523 1 43 						1.  9 Works
# 2.  1 58 1 58 							2.  8 Works
# 3.  1 58 1 57 							3.  11 Works
# 4.  3 32 44 56 2 54 18 					4.  18
# 5.  4 345 456 567 678 2 36 55 				5.   22 Works


inp = "4 118 435 635 818 4 33 17 54 75" 
board = [[" " for col in range(8)] for row in range(8)]

def placex(board, x):
    x = str((int(x[0])-1)*10 + (int(x[1])-1))
    x=x.zfill(2)
    try:
        #spot itself
        if board[int(x[0])][int(x[1])] == "o":
            board[int(x[0])][int(x[1])] = " "
        else:
            board[int(x[0])][int(x[1])] = "o"
    except:
        pass

    try:
        #diagonal up-right
        if int(x[0])-1 >= 0:
            if board[int(x[0])-1][int(x[1])+1] == "o":
                board[int(x[0])-1][int(x[1])+1] = " "
            else:
                board[int(x[0])-1][int(x[1])+1] = "o"
    except:
        pass

    try:
        #diagonal down-right
        if board[int(x[0])+1][int(x[1])+1] == "o":
            board[int(x[0])+1][int(x[1])+1] = " "
        else:
            board[int(x[0])+1][int(x[1])+1] = "o"
    except:
        pass

    try:
        #diagonal up-left
        if int(x[0])-1 >= 0 and int(x[1])-1 >= 0:
            if board[int(x[0])-1][int(x[1])-1] == "o":
                board[int(x[0])-1][int(x[1])-1] = " "
            else:
                board[int(x[0])-1][int(x[1])-1] = "o"
    except:
        pass

    try:
        #diagonal down-left
        if int(x[1])-1 >= 0:
            if board[int(x[0])+1][int(x[1])-1] == "o":
                board[int(x[0])+1][int(x[1])-1] = " "
            else:
                board[int(x[0])+1][int(x[1])-1] = "o"
    except:
        pass

    #rows
    for i in range(1,3):
        try:
            #rows right
            if board[int(x[0])][int(x[1])+i] == "o":
                board[int(x[0])][int(x[1])+i] = " "
            else:
                board[int(x[0])][int(x[1])+i] = "o"
        except:
            pass

        try:
            #rows left
            if int(x[1])-i >= 0:
                if board[int(x[0])][int(x[1])-i] == "o":
                    board[int(x[0])][int(x[1])-i] = " "
                else:
                    board[int(x[0])][int(x[1])-i] = "o"
        except:
            pass
        
        try:
            #columns up
            if board[int(x[0])+i][int(x[1])] == "o":
                board[int(x[0])+i][int(x[1])] = " "
            else:
                board[int(x[0])+i][int(x[1])] = "o"
        except:
            pass

        try:
            #columns down
            if int(x[0])-i >= 0:
                if board[int(x[0])-i][int(x[1])] == "o":
                    board[int(x[0])-i][int(x[1])] = " "
                else:
                    board[int(x[0])-i][int(x[1])] = "o"
        except:
            pass
    return board

inp = inp.split()
on = []
xs = []
counter = 0
for i in range(int(inp.pop(0))):
    on.append(inp.pop(0))
for j in range(int(inp.pop(0))):
    xs.append(inp.pop(0))

for i in range(len(on)):
    for j in range(len(on[i])-1):
        board[int(on[i][0])-1][int(on[i][1+j])-1] = "o"

for i in range(len(xs)):
    board = placex(board, xs[i])

for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == "o":
            counter+=1

print(counter)