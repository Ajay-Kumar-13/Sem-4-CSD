def decimalToBinary(n):
    return bin(n).replace("0b", "")
   
length = int(input('Enter length: '))
inputs = []
binaries = []
res = []
for i in range(length):
    inputs.append(int(input('Enter number: ')))

for input in inputs:
    for i in range(1,input):
        b = decimalToBinary(i)
        binary = [int(x) for x in str(b)]
        binarySum = sum(binary) + i
        binaries.append(binarySum)
    if input in binaries:
        res.append('SUPPORTED')
    else:
        res.append('BLEAK')

print(res)