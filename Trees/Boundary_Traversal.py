class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_leaves(node):
    if node:
        print_leaves(node.left)
        if not node.left and not node.right:
            print(node.val, end=" ")
        print_leaves(node.right)

def print_left_boundary(node):
    if node:
        if node.left:
            print(node.val, end=" ")
            print_left_boundary(node.left)
        elif node.right:
            print(node.val, end=" ")
            print_left_boundary(node.right)

def print_right_boundary(node):
    if node:
        if node.right:
            print_right_boundary(node.right)
            print(node.val, end=" ")
        elif node.left:
            print_right_boundary(node.left)
            print(node.val, end=" ")

def boundary_traversal(root):
    if not root:
        return
    
    print(root.val, end=" ")

    # Print left boundary excluding the root node
    print_left_boundary(root.left)

    # Print all the leaf nodes
    print_leaves(root)

    # Print right boundary excluding the root node
    print_right_boundary(root.right)

# Create a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(8)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.left.left = TreeNode(9)
root.right.left.right = TreeNode(10)

boundary_traversal(root)
