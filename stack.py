class Stack:
    def __init__(self, stack):
        self.stack = stack
        self.top = -1

    def push(self, element):
        self.top = self.top + 1
        self.stack[self.top] = element
    
    def pop(self):
        self.stack[self.top] = 0
        self.top = self.top - 1

    def size(self):
        return self.top+1

    def display(self):
        while self.top != -1:
            print(self.stack[self.top], end=" ")
            self.top -= 1

if __name__ == '__main__':
    lst = [0] * 5
    S = Stack(lst)
    S.push(5)
    print('Size',S.size())
    S.push(15)
    S.push(20)
    S.push(25)
    S.push(30)
    print('Size',S.size())
    S.display()