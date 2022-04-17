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
            raise Exception("Stack underflow!!")
        return self.container.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.container[-1]

    def print_stack(self):
        return [i for i in self.container]


def near_great_to_right(lst):
    stack = Stack()
    res = []
    for i in range(len(lst)-1, -1, -1):
        if stack.is_empty():
            res.append(-1)
            stack.push(lst[i])
        elif not stack.is_empty():
            while not stack.is_empty() and lst[i] > stack.peek():
                stack.pop()
            if stack.is_empty():
                res.append(-1)
            else:
                res.append(stack.peek())
            stack.push(lst[i])
    res.reverse()
    return res


arr = [2, 8, 3, 6, 9]
print(near_great_to_right(arr))
