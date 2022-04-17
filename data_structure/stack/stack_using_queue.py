from collections import deque


# Implement stack using two queues
class Stack:

    # Constructor
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    # Insert an item into the stack
    def insert_data(self, data):
        # Move all elements from the first queue to the second queue
        while len(self.q1):
            self.q2.append(self.q1.pop())

        # Push the given item into the first queue
        self.q1.append(data)

        # Move all elements back to the first queue from the second queue
        while len(self.q2):
            self.q1.append(self.q2.pop())

    # Remove the top item from the stack
    def remove_data(self):
        # if the first queue is empty
        if not self.q1:
            print('Underflow!!')
            exit(0)
        # return the front item from the first queue
        front = self.q1.popleft()
        return front


if __name__ == '__main__':

    keys = [5, 4, 3, 2, 1]

    # insert the above keys into the stack
    s = Stack()
    for key in keys:
        s.insert_data(key)

    while s:
        print(s.remove_data())

    print(s.remove_data())
