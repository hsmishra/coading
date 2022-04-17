class Node:

    # Constructor to initialize the node object
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def insert_data(self, data):
        node = Node(data, self.head)
        self.head = node

    # Add contents of two linked lists and return the head
    # node of resultant list
    def add_lists(self, first, second):
        carry = 0
        tmp_data = None
        prev = None

        # While both list exists
        while(first is not None or second is not None):
            first_data = 0 if first is None else first.data
            second_data = 0 if second is None else second.data
            addition = carry + first_data + second_data

            # update carry for next calculation
            carry = 1 if addition >= 10 else 0

            # update addition if it is greater than 10
            addition = addition if addition < 10 else addition % 10

            # Create a new node with addition as data
            tmp_data = Node(addition)

            # if this is the first node then set it as head
            # of resultant listNoa
            if self.head is None:
                self.head = tmp_data
            else:
                prev.next = tmp_data

            # Set prev for next insertion
            prev = tmp_data

            # Move first and second pointers to next nodes
            if first is not None:
                first = first.next
            if second is not None:
                second = second.next

        if carry > 0:
            tmp_data.next = Node(carry)

    # Utility function to print the LinkedList
    def printList(self):
        itr = self.head
        llstr = ''
        while itr:
            suffix = ''
            if itr.next:
                suffix = ' ---> '
            llstr += str(itr.data) + suffix
            itr = itr.next
        return llstr


# Driver code
first = LinkedList()
second = LinkedList()

# Create first list
first.insert_data(9)
first.insert_data(1)

print(f"List_one: {first.printList()}")

# Create second list
second.insert_data(1)
second.insert_data(9)

print(f"List_two: {second.printList()}")

# Add the two lists and see result
res = LinkedList()
res.add_lists(first.head, second.head)
print(f"Addition: {res.printList()}")
