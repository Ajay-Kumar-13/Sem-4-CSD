str = set(list(input('Enter a sentence').upper()))
alphabets = set(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

if alphabets.issubset(str):
    print('It is a panagram')
else:
    print('Not a panagram')