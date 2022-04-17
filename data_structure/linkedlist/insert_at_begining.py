class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        


class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
    
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
    ll.insert_at_begining(10)
    ll.insert_at_begining(20)
    ll.insert_at_begining(30)
    ll.insert_at_begining(40)
    ll.display()