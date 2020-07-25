# 题目：判断一个树是不是对称的二叉树，即是否与其镜像相同
# 法1：复杂：递归：先判断左右子节点是否相等，再判断左右子树是否成镜像
# 法2：直接：正向DFS和反向DFS 序列是否相等

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

# 递归法
def isSymmetrical(root):
    if root is None:
        return False
    # 左右没有子节点
    if root.leftChild is None and root.rightChild is None:
        return True
    # 左右有子节点
    if root.leftChild is not None and root.rightChild is not None:
        # 且左右子节点相等
        if root.leftChild.data == root.rightChild.data:
            # 进一步判断左右子树是否镜像
            return isMirrorTree(root.leftChild, root.rightChild)
        else:
            return False
    return False

# 判断左右子树是否镜像
def isMirrorTree(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif root1 is not None and root2 is not None:
        if root1.data == root2.data:
            # 镜像的四种可能情况
            if root1.leftChild is not None and root2.rightChild is not None and root1.rightChild is None and root2.leftChild is None:
                if root1.leftChild.data == root2.rightChild.data and isMirrorTree(root1.leftChild, root2.rightChild):
                    return True
            elif root1.leftChild is None and root2.rightChild is None and root1.rightChild is not None and root2.leftChild is not None:
                if root1.rightChild.data == root2.leftChild.data and isMirrorTree(root1.rightChild, root2.leftChild):
                    return True
            elif root1.leftChild is not None and root2.rightChild is not None and root1.rightChild is not None and root2.leftChild is not None:
                if root1.leftChild.data == root2.rightChild.data and isMirrorTree(root1.leftChild, root2.rightChild):
                    if root1.rightChild.data == root2.leftChild.data and isMirrorTree(root1.rightChild, root2.leftChild):
                        return True
            elif root1.leftChild is None and root2.rightChild is None and root1.rightChild is None and root2.leftChild is None:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


# 遍历与反向遍历
# 如果对称则相等
def isSymmetrical2(root):
    arr1 = []
    arr2 = []
    return preOrder(root, arr1) == inPreOrder(root, arr2)
    
# 正向前序遍历
def preOrder(root, arr):
    if root is None:
        return
    arr.append(root.data)
    preOrder(root.leftChild, arr)
    preOrder(root.rightChild, arr)
    return arr

# 反向前序遍历
def inPreOrder(root, arr):
    if root is None:
        return
    arr.append(root.data)
    inPreOrder(root.rightChild, arr)
    inPreOrder(root.leftChild, arr)
    return arr


if __name__ == "__main__":
    root = TreeNode(8)
    root.leftChild = TreeNode(6)
    root.rightChild = TreeNode(6)
    root.leftChild.leftChild = None #TreeNode(5)
    root.leftChild.rightChild = TreeNode(7)
    root.rightChild.leftChild = TreeNode(7)
    root.rightChild.rightChild = None #TreeNode(5)
    arr1 = []
    arr2=[]
    print(preOrder(root, arr1))
    print(inPreOrder(root, arr2))
    print(isSymmetrical2(root))
    print(isSymmetrical(root))
