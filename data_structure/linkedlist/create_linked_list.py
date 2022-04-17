class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
            

    def display(self):
        if self.head is None:
            return "Linked List is empty"

        current = self.head
        while current:
            print(current.data, "-->", end="")
            current = current.next


linked_list = LinkedList()

linked_list.head = Node(10)
linked_list_2 = Node(20)
linked_list_3 = Node(30)
linked_list_4 = Node(40)
linked_list_5 = Node(50)

linked_list.head.next = linked_list_2
linked_list_2.next = linked_list_3
linked_list_3.next = linked_list_4
linked_list_4.next = linked_list_5

print(linked_list.display())
