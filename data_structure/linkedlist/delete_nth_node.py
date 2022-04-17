import insert_at_begining


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList(insert_at_begining.LinkedList):
    def __init__(self):
        self.head = None

    def get_length(self):
        counter = 0
        iteration = self.head
        while(iteration):
            counter += 1
            iteration = iteration.next
        return counter

    def delete_nth_node(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index!")

        if index == 0:
            self.head = self.head.next
            return

        counter = 0
        iteration = self.head
        while(iteration):
            if counter == index-1:
                iteration.next = iteration.next.next
                break
            iteration = iteration.next
            counter += 1

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
ll.insert_at_begining(12)
ll.insert_at_begining(11)
ll.insert_at_begining(10)
ll.insert_at_begining(9)
ll.display()
ll.delete_nth_node(0s)
ll.display()
