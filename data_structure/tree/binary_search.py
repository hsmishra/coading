class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child_node(self, data):
        if data == self.data:
            return  # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child_node(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.add_child_node(data)
            else:
                self.right = Node(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False


def binary_tree(ele):
    print("Building tree with these ele:", ele)
    root = Node(ele[0])

    for i in range(1, len(ele)):
        root.add_child_node(ele[i])

    return root


if __name__ == '__main__':
    countries = ["India", "Pakistan", "Germany",
                 "USA", "China", "India", "UK", "USA"]
    country_tree = binary_tree(countries)

    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))
