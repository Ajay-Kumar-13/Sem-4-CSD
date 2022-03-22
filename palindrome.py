n = int(input('Enter a number: '))

def checkPalindrome(b):
    c = int(str(b)[::-1])
    if b == c:
        return True
    else:
        return False

while True:
    reverse = int(str(n)[::-1])
    b = n + reverse
    if checkPalindrome(b):
        print(b)
        break
    else:
        n = b
