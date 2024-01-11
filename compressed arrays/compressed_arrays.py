# inp ='HELLOAWORLD 2'	# ADEHORW
# inp ='HELLOAWORLD 3'	# L
# inp ='HELLOAWORLD 4'	# ADEHORW
# inp ='HELLOAWORLD 7'	# ADEHL
# inp ='BARRINGTON 3'	# NONE
# inp ='RHODEISLAND 4'	# DHILNOR
# inp ='ABACUSSPACES 3'	# AS
# inp ='ICECREAMICE 7'	# NONE
# inp ='COFFEECUPS 4'	# CEFOP
# inp ='ALLSTARSTUDENTS 5'# ANRU
# inp ='SHESELLSSEASHELLSBYTHESEASHORE 4'	# BHLORT
# inp ='THEBROWNFOXJUMPSOVERTHEDOG 8'		# FGHJMNOPRSU
# inp ='ZYYXXXWWWWVVVVVUUUUUUTTTTTTT  6'		# UXYZ
# inp ='ABRACADABRAKALAMAZOOTIMBUKTU 5'		# BU
# inp ='SUPERCALIFRAGILISTICEXPIALLIDOCIOUS 4'	# EGLOPRTU
# inp ='MISSISSIPPIMASSACHUSETTSMISSOURI 9'	# APRTU
# inp ='ROGERWILLIAMSFOUNDEDRHODEISLAND 4'	# ADFGHMNSUW                                          
# inp ='PROGRAMMINGINPYTHONISPHANTASTIC 3'	# APT  
# inp ='AAAAABBBBCCCDDEDDCCCBBBBAAAAA 11'	# CDE 
inp ='ALLSTARCONTESTINBARRINGTONRI 8'		# LNORT

word, ind = inp.split()
ltrs = []
wordl = []
for i in range(len(word)):
    if word[i] not in ltrs:
        wordl.append([word.count(word[i]), word[i]])
        ltrs.append(word[i])
ltrs = ""


def addtwo(word):
    l1 = word.pop(0) 
    l2 = word.pop(0)
    word.append([l1[0] + l2[0], "".join(sorted(l1[1] + l2[1]))])
    return word


while len(wordl) > 1:
    for i in range(len(wordl)):
        if wordl[i][0] == int(ind):
            ltrs += wordl[i][1]
    wordl.sort()
    wordl = addtwo(wordl)

ltrs = "".join(sorted("".join(set(ltrs))))
print(ltrs)