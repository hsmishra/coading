from typing import Counter


class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next
        

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def insert_at_beginig(self, data):
         node = Node(data, self.head)
         self.head = node
    
    def get_length(self):
        counter = 0
        iteration = self.head
        while(iteration):
            counter += 1
            iteration = iteration.next 
        return counter
    
    def insert_at_nth_position(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception ("Please enter a valid index")
        if index == 0:
            self.insert_at_beginig(data)
            return
        iteration = self.head
        counter = 0
        while(iteration):
            if counter == index-1:
                node = Node(data, iteration.next)
                iteration.next = node
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
            llstr += str(itr.data) +suffix
            itr = itr.next 
        print(llstr)
            


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginig(90)
    ll.insert_at_beginig(80)
    ll.insert_at_nth_position(2, 10)
    ll.display()