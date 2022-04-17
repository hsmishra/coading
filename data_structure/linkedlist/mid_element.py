class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_end(self, data):
        iteration = self.head
        if self.head is None:
            self.head = Node(data)
            return

        while(iteration.next):
            iteration = iteration.next
        iteration.next = Node(data)

    def find_mid_element(self):
        ptr_1 = self.head
        ptr_2 = self.head

        if self.head is not None:
            while(ptr_1 is not None and ptr_1.next is not None):
                ptr_1 = ptr_1.next.next
                ptr_2 = ptr_2.next
            return ptr_2.data

    def display(self):
        iteration = self.head
        llstr = ""
        while(iteration):
            suffix = ""
            if iteration.next:
                suffix = " ---> "
            llstr += str(iteration.data) + suffix
            iteration = iteration.next
        return llstr


ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_end(40)
ll.insert_at_end(50)
ll.insert_at_end(60)
ll.insert_at_end(70)
ll.insert_at_end(80)
print(ll.find_mid_element())
print(ll.display())
