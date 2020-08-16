class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def treeDepth(root):
    if root is None:
        return 0
    return max(treeDepth(root.left), treeDepth(root.right)) + 1

if __name__ == "__main__":
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.right = TreeNode(3)
    node.left.left = TreeNode(4)
    node.left.right = TreeNode(5)
    node.left.right.left = TreeNode(7)
    node.right.right = TreeNode(6)
    print(treeDepth(node))