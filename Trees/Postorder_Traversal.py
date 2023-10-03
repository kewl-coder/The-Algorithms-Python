class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.left)  # Recursively traverse the left subtree
        postorder_traversal(node.right)  # Recursively traverse the right subtree
        print(node.value, end=" ")  # Visit the current node

# Example usage:
# Construct a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Perform postorder traversal starting from the root
print("Postorder traversal:")
postorder_traversal(root)
