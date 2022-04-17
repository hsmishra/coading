class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


# pre order traversal
def pre_order(root):
    if root:
        print(root.data)
        pre_order(root.left)
        pre_order(root.right)


# in order traversal
def in_order(root):
    if root:
        in_order(root.left)
        print(root.data)
        in_order(root.right)


# post order traversal
def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.data)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
pre_order(root)
