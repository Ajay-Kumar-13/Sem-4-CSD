n = int(input('Enter number: '))
ans, i = 1,1
factorials = []

while n > ans:
    ans = ans * i
    i = i+1
    factorials.append(ans)

if n in factorials:
    print(factorials.index(n)+1)
else:
    print('Not a factorial')