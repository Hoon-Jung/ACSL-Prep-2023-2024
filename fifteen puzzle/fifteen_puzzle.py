# 7 BL 1. 10
# 7 BLARBLAR 2. 7
# 7 BBLLAA 3. 5
# 10 RRAALLBB 4. 10
# 1 RRBRAL 5. 3
# 10 LBRA 6. 10
# 2 RRBLLAL 7. 1
# 8 BBLLAALBAR 8. 6
# 16 ALALALBRBRBR 9. 16
# 4 LBLBLBRRRAAA 10. 4

# 1 BRBRBRALAL 1. 6
# 11 BLARALBRALBBL 2. 13
# 7 ARBLARBLARBLAR 3. 4
# 16 LALALARBRBRB 4. 16
# 16 AAALLBBBRRALL 5. 10
# 2 LBRBBRALALA 6. 1
# 5 RRRBBLLLAAARBLBRBLA 7. 9
# 12 BLLAARRBBLARBLLARRB 8. 16
# 15 ABABLRLRABABRLRL 9. 15
# 13 AAARRRBBLLAARRBBLARB 10. 12

loc, moves = input().split()
loc = int(loc)
moves = list(moves)

def move(l, move):
    if move == "B":
        l += 4
    elif move == "A":
        l -= 4
    elif move == "L":
        l -= 1
    else:
        l += 1
    return l


for i in range(len(moves)):
    loc = move(loc, moves[i])

print(loc)