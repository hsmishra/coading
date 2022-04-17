class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        iteration = self.head
        while(iteration.next):
            iteration = iteration.next
        iteration.next = Node(data)

    def insert_value(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def display(self):
        itr = self.head
        llstr = ''
        while itr:
            suffix = ''
            if itr.next:
                suffix = ' ---> '
                llstr += str(itr.data) + suffix
        itr = itr.next
        print(llstr)


ll = LinkedList()
lst = [12, 21, 11, 23, 11]
ll.insert_value(lst)

ll.display()
