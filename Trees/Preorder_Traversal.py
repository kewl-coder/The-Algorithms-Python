class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder_traversal(node):
    if node is not None:
        print(node.value, end=" ")  # Visit the current node
        preorder_traversal(node.left)  # Recursively traverse the left subtree
        preorder_traversal(node.right)  # Recursively traverse the right subtree

# Example usage:
# Construct a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Perform preorder traversal starting from the root
print("Preorder traversal:")
preorder_traversal(root)
