class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def reconstructTree(preOrder, inOrder):
    if len(preOrder) == 0 or len(inOrder) == 0:
        return None
    # 1.前序遍历序列的第一个为根节点
    root = preOrder[0]
    node = TreeNode(root)
    # 2.在中序遍历序列里找根节点的位置
    # 中序遍历的根节点左边为左子树，右边为右子树
    # 以此确定左右子树的所含节点的个数
    for i in range(len(inOrder)):
        if inOrder[i] == root:
            midRootIndex = i
            leftChildNodeNum = i
            rightChildNodeNum = len(inOrder)-1-i
    # 3.给根节点挂左右子树的根节点
    # 左子树
    if leftChildNodeNum == 0:
        node.leftChild = None
    else:
        # 从原序列中确定左子树的前中遍历序列 递归 返回左子树根节点
        node.leftChild = reconstructTree(preOrder[1 : leftChildNodeNum+1], inOrder[0 : midRootIndex])
    # 右子树
    if rightChildNodeNum == 0:
        node.rightChild = None
    else: 
        # 从原序列中确定右子树的前中遍历序列 递归 返回右子树根节点
        node.rightChild = reconstructTree(preOrder[leftChildNodeNum+1 :], inOrder[midRootIndex+1 :])
    return node

# 深度优先搜索
class DFS:
    # 前序遍历
    @staticmethod
    def preOrderTraveral(node):
        if node is None:
            return
        print(node.data)
        DFS.preOrderTraveral(node.leftChild)
        DFS.preOrderTraveral(node.rightChild)

if __name__ == "__main__":
    preOrder = [1,2,4,7,3,5,6,8]
    inOrder = [4,7,2,1,5,3,8,6]
    head = reconstructTree(preOrder, inOrder)
    DFS.preOrderTraveral(head)