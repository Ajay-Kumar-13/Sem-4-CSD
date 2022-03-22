class Queue:
    def __init__(self, queue):
        self.queue = queue
        self.top = -1
    def push(self, element):
        self.top = self.top + 1
        self.queue[self.top] = element
    def pop(self):
        self.queue[self.top] = 0
        self.top -= 1
    def display(self):