class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def in_order_traversal(node):
    if node:
        # Traverse the left subtree
        in_order_traversal(node.left)
        
        # Visit the current node
        print(node.value, end=' ')

        # Traverse the right subtree
        in_order_traversal(node.right)

# Example usage:
if __name__ == "__main__":
    # Create a binary tree
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)

    print("In-order traversal:")
    in_order_traversal(root)
