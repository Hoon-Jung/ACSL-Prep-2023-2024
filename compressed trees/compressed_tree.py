# HELLOAWORLD W 1. 011
# ABCDEFHHHLLLNNN D 2. 1011
# ABCDGGGKKKKK G 3. 10
# LYAAEEGGPPP L 4. 010
# ABCDEFHHLLL A 5. 1100
# ABCCDDEEFFF C 6. 111
# AABBBCCCCDDDDDEEEEEEFFFFFFF B 7. 1111
# ABCCGGGHHHKKKKK B 8. 1001
# ABFFFGGGGCCCCC C 9. 0
# XAABBCCCDDDKKKKLLLL L 10. 01


string, let = input().split()
lets = set()
tree = []
binaryvals = {}


def addtobin(vals, num):
    for letter in vals:
        try:
            binaryvals[letter] = num + binaryvals[letter]
        except:
            binaryvals[letter] = num


for i in range(len(string)):
    if string[i] not in lets:
        tree.append([string.count(string[i]), string[i]])
    lets.add(string[i])

tree.sort()
for j in range(len(tree)):
    if len(tree) > 1:
        val1 = tree.pop(0)
        val2 = tree.pop(0)
        addtobin(list(val1[1]), "0")
        addtobin(list(val2[1]), "1")
        newval = [val1[0] + val2[0], val1[1] + val2[1]]
        tree.append(newval)
        tree.sort()

print(binaryvals[let])