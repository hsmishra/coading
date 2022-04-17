# Python program to find the inorder successor in a BST

# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, key=None, left=None, right=None):
        self.data = key
        self.left = left
        self.right = right


def in_order_successor(n):

    # Step 1 of the above algorithm
    if n.right is not None:
        return min_val(n.right)

    # Step 2 of the above algorithm
    p = n.parent
    while(p is not None):
        if n != p.right:
            break
        n = p
        p = p.parent
    return p

# Given a non-empty binary search tree, return the
# minimum data value found in that tree. Note that the
# entire tree doesn't need to be searched


def min_val(node):
    current = node

    # loop down to find the leftmost leaf
    while(current is not None):
        if current.left is None:
            break
        current = current.left

    return current


# Given a binary search tree and a number, insert_nodes a
# new node with the given number in the correct place
# in the tree. Returns the new root pointer which the
# caller should then use( the standard trick to avoid
# using reference parameters)
def insert_node(node, data):

    # 1) If tree is empty then return a new singly node
    if node is None:
        return Node(data)
    else:

        # 2) Otherwise, recur down the tree
        if data <= node.data:
            temp = insert_node(node.left, data)
            node.left = temp
            temp.parent = node
        else:
            temp = insert_node(node.right, data)
            node.right = temp
            temp.parent = node

        # return the unchanged node pointer
        return node


# Driver program to test above function

root = None

# Creating the tree given in the above diagram
root = insert_node(root, 20)
root = insert_node(root, 8)
root = insert_node(root, 22)
root = insert_node(root, 4)
root = insert_node(root, 12)
root = insert_node(root, 10)
root = insert_node(root, 14)
temp = root.left.right.right

succ = in_order_successor(temp)
if succ is not None:
    print("\nInorder Successor of % d is % d " % (temp.data, succ.data))
else:
    print("\nInorder Successor doesn't exist")
