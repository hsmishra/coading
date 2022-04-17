import insert_at_begining

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    


class LinkedList(insert_at_begining.LinkedList):
    def __init__(self):
        self.head = None
        
    def get_length(self):
        iteration = self.head
        counter = 0
        while (iteration):
            counter += 1
            iteration = iteration.next
        return f"Lenght of the linked list is {counter} "
    

ll = LinkedList()
ll.insert_at_begining(10)
ll.insert_at_begining(20)
ll.insert_at_begining(30)
ll.insert_at_begining(40)

ll.display()
print(ll.get_length())