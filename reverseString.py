string = input('Enter string: ')
alphabets = []
numPos = []
res = []
for i,str in enumerate(string):
    if str.isnumeric():
        numPos.append(i)
    else:
        alphabets.append(str)
alphabets.reverse()
j = 0
for i in range(len(string)):
    if i in numPos:
        res.append(string[i])
    else:
        res.append(alphabets[j])
        j = j+1

space = ""
print(space.join(res))