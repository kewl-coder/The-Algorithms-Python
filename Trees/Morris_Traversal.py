class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def morris_inorder_traversal(root):
    current = root
    while current:
        if not current.left:
            print(current.val, end=" ")  # Visit the current node
            current = current.right  # Move to the right child
        else:
            # Find the inorder predecessor of the current node
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right

            if not predecessor.right:
                predecessor.right = current  # Make a temporary threaded link
                current = current.left  # Move to the left child
            else:
                predecessor.right = None  # Remove the threaded link
                print(current.val, end=" ")  # Visit the current node
                current = current.right  # Move to the right child

# Example usage:
# Construct a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("In-order traversal using Morris Traversal:")
morris_inorder_traversal(root)
