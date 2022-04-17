class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_data(self, data):
        node = Node(data, self.head)
        self.head = node

    def find_loop(self):
        stored_data = set()
        iteration = self.head

        while iteration:
            if iteration in stored_data:
                return True
            stored_data.add(iteration)
            iteration = iteration.next
        return False

    def display(self):
        itr = self.head
        llstr = ''
        while itr:
            suffix = ''
            if itr.next:
                suffix = ' ---> '
            llstr += str(itr.data) + suffix
            itr = itr.next
        return llstr


if __name__ == "__main__":
    ll = LinkedList()
    ll.add_data(40)
    ll.add_data(30)
    ll.add_data(20)
    ll.add_data(10)
    print(ll.display())

    ll.head.next.next.next.next = ll.head

    if (ll.find_loop()):
        print("Yes")
    else:
        print("No")
