from collections import deque


class Stack:
    def __init__(self) -> None:
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    def display(self):
        lst = []
        for i in self.container:
            if i is not None:
                lst.append(i)
        return lst


s = Stack()
s.push(4)
s.push(5)
s.push(6)
print(s.display())
print("================================")
s.pop()
print(s.display())
print("================================")
s.push(7)
print(s.peek())
print(s.display())
