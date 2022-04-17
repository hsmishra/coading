from collections import deque


class Stack:
    def __init__(self) -> None:
        self.container = deque()

    def push(self, val):
        return self.container.append(val)

    def remove(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


def reverse_string(string):
    stack = Stack()
    for ch in string:
        stack.push(ch)
    rstr = ""
    while stack.size() != 0:
        rstr += stack.remove()
    return rstr


print(reverse_string("Hello"))
