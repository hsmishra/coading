"""
Nearest greatest to left
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
            raise Exception("Stack underflow")

        return self.container.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.container[-1]

