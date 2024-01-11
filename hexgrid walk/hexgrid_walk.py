# B2 22435
# C4 22435
# D6 54166231
# E5 162435
# E5 162435534261
# M5 123123123123
# G9 3
# G9 1
# B2 6163
# B2 3251616544

# 1. D1 (done)
# 2. E3 (done)
# 3. C7 (done)
# 4. E5 (done)
# 5. E5 (done)
# 6. U9 (done)
# 7. H9 (done)
# 8. G10 (done)
# 9. B3 (done)
# 10. A2 (done)

# D4 123456 1. D4 (done)
# E3 654321 2. E3(done)
# K7 63165 3. I8(done)
# E4 44454456445 4. B1(done)
# E4 444544564454334 5. B1(done)
# C5 51515151 6. A8(done)
# X8 34343434 7. Z3(done)
# M9 121 8. N12(done)
# K37 233245 9. N36(done)
# G123 54342125654345432123452 10. J118 (done)

def nextmove(spot, move):
    og = [spot[0], spot[1]]
    if move == 1:
        spot[1] += 1
    if move == 2:
        spot[0] = chr(ord(spot[0])+1)
        if ord(spot[0]) % 2 == 0:
            spot[1] += 1
    if move == 3:
        spot[0] = chr(ord(spot[0])+1)
        spot[1] -= 1
        if ord(spot[0]) % 2 == 0:
            spot[1] += 1
    if move == 4:
        spot[1] -= 1
    if move == 5:
        spot[0] = chr(ord(spot[0])-1)
        spot[1] -= 1
        if ord(spot[0]) % 2 == 0:
            spot[1] += 1
    if move == 6:
        spot[0] = chr(ord(spot[0])-1)
        if ord(spot[0]) % 2 == 0:
            spot[1] += 1

    
    if (ord(spot[0]) < 65) or (ord(spot[0]) > 90) or (spot[1] < 1):
        return og
    else:
        return spot


spot, moves = input().split()
spot = [spot[0], int(spot[1::])]
moves = list(map(lambda b: int(b), moves))
for i in range(len(moves)):
    spot = nextmove(spot, moves[i])

print(spot[0] + str(spot[1]))
