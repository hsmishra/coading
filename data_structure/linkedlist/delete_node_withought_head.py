from platform import node


class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next
        

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def insert_node(self, data):
        node = Node(data, self.head)
        self.head = node
    
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
    
    def delete_node(self, node):
        if (node == None):
            return
        if (node.next == None):
            print("Not to be deleted")
        else:
            node.data = node.next.data
            node.next = node.next.next
            


ll = LinkedList()
ll.insert_node(1)
ll.insert_node(2)
ll.insert_node(3)
ll.insert_node(4)
ll.insert_node(5)
ll.insert_node(6)
ll.insert_node(7)
print("Before delete node 3")
ll.display()
ll.delete_node(ll.head.next)
ll.display()
            