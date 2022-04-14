import re


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child_node(self, data):
        if data == self.data:
            return # Node already exist...
        
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
    
    def search_ele(self, values):
        if self.data == values:
            return True
        
        if values < self.data:
            if self.left:
                return self.left.search_ele(values)
            else:
                return False
        
        if values > self.data:
            if self.right:
                return self.right.search_ele(values)
            else:
                return False



def binary_tree(ele):
    print("Creating the tree using the ", ele)
    root = Node(ele[0])

    for i in range(1, len(ele)):
        root.add_child_node(ele[i])
    return root


if __name__ == '__main__':
    countries = ["India", "Pakistan", "Germany",
                 "USA", "China", "India", "UK", "USA"]
    country_tree = binary_tree(countries)

    print("UK is in the list? ", country_tree.search_ele("UK"))
    print("Sweden is in the list? ", country_tree.search_ele("Sweden"))
