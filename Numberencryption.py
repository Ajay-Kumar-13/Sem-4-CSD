number = list(input('Enter a number: '))
actions = list(input('Enter action to be performed: '))

index = 0
for i,action in enumerate(actions):
    if action == 'R':
        index = index + 1
    elif action == 'L':
        index = index - 1
    elif action == 'T':
        if number[index] != '9':
            number[index] = int(number[index]) + 1
    elif action == 'D':
        if number[index] != '0':
            number[index] = int(number[index]) - 1
    elif action == 'S':
        number[index],number[int(actions[i+1])-1] = number[int(actions[i+1])-1],number[index]

for i in range(len(number)):
    number[i] = str(number[i])

encryptedString = ''.join(number)
print(encryptedString)