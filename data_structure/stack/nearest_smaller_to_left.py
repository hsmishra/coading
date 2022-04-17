"""
Find the next smaller to left of each element
"""

from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()
        
    def is_empty(self):
        return len(self.container) == 0
    
    def push(self, val):
        self.container.append(val)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is underflow!!")
        else:
            self.container.pop()

    def peek(self):
        return self.container[-1]

    def print_stack(self):
        for i in self.container:
            print(i)


def next_smaller_to_left(lst):

    res = []
    stack = Stack()
    stack.print_stack()
    for i in range(0, len(lst)):
        if stack.is_empty():
            res.append(-1)
            stack.push(lst[i])

        elif not stack.is_empty():
            while not stack.is_empty() and lst[i] < stack.peek():
                stack.pop()

            if stack.is_empty():
                res.append(-1)
            else:
                res.append(stack.peek())
            stack.push(lst[i])

    return res


arr = [4, 5, 2, 10, 8]
print(next_smaller_to_left(arr))
