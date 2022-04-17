class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_element(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        iteration = self.head
        while iteration.next:
            iteration = iteration.next
        iteration.next = Node(data)

    def display(self):
        iteration = self.head
        while(iteration):
            print(iteration.data)
            iteration = iteration.next


ll = LinkedList()
ll.insert_element(10)
ll.insert_element(20)
ll.display()
