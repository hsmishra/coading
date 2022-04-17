class TreeNode:
    def __init__(self, data_node=None, parent_node=None):
        self.data_node = data_node
        self.parent_node = parent_node
        self.children = []
    
    def add_child_node(self, child):
        child.parent_node = self
        self.children.append(child)

    def get_tree_level(self):
        level = 0
        parent = self.parent_node
        while parent:
            level += 1
            parent = parent.parent_node

        return level

    def print_tree(self):
        spaces = ' ' * self.get_tree_level() * 3
        prefix = spaces + "|-->" if self.parent_node else ""
        print(prefix + self.data_node)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_product_tree():
    root = TreeNode("!Electronics!")

    laptop = TreeNode("Laptop")
    laptop.add_child_node(TreeNode("Mac"))
    laptop.add_child_node(TreeNode("Surface"))
    laptop.add_child_node(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child_node(TreeNode("iPhone"))
    cellphone.add_child_node(TreeNode("Google Pixel"))
    cellphone.add_child_node(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child_node(TreeNode("Samsung"))
    tv.add_child_node(TreeNode("LG"))

    root.add_child_node(laptop)
    root.add_child_node(cellphone)
    root.add_child_node(tv)

    root.print_tree()


if __name__ == '__main__':
    build_product_tree()
