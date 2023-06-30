class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)


def show_tree(node: TreeNode):
    if node:
        print(node.value)
        show_tree(node.left)
        show_tree(node.right)


show_tree(tree)
