class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.root = None
    def insert(self, data):
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

ll = Linkedlist()
ll.insert(12)
ll.insert(72)
ll.insert(15)
ll.insert(4)
ll.insert(43)
ll.insert(2)
ll.insert(25)
ll.insert(3)