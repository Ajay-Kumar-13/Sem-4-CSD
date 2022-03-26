class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.root = None
        self.size = 0
    def insert(self, data):
        self.size += 1
        newNode = Node(data)
        if self.root:
            traverser = self.root
            while traverser.next != None:
                traverser = traverser.next
            if traverser.data < data:
                while traverser.next != None:
                    traverser = traverser.next
                traverser.next = newNode
            else:
                traverser = self.root
                if data < traverser.data:
                    self.root = newNode
                    newNode.next = traverser
                else:
                    while traverser.next.data < data:
                        traverser = traverser.next
                    next = traverser.next
                    while next.data < data:
                        traverser = traverser.next
                    traverser.next = newNode
                    newNode.next = next
        else:
            self.root = newNode

    def getCenterElements(self):
        if self.size % 2 != 0:
            center = self.size // 2
            traverser = self.root
            for i in range(center):
                traverser = traverser.next
            print(traverser.data)
        else:
            center = self.size // 2
            print(center)
            traverser = self.root
            for i in range(center-1):
                traverser = traverser.next
            print(traverser.data, end=" ")
            print(traverser.next.data)
            print()

ll = Linkedlist()
ll.insert(12)
ll.insert(14)
ll.insert(15)
ll.insert(4)
ll.insert(43)
ll.insert(2)
ll.insert(25)
ll.insert(3)
ll.insert(72)
ll.getCenterElements()