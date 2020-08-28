import sys 
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# 给定前序遍历序列和中序遍历序列
# 输出该二叉树的叶节点个数
# 输入
# 3
# 1 2 3
# 2 1 3
# 输出
# 2

def reconstructTree(preOrder, inOrder):
    if len(preOrder) == 0 or len(inOrder) == 0:
        return None
    # 1.前序遍历序列的第一个为根节点
    node = TreeNode(preOrder[0])
    # 2.在中序遍历序列里找根节点的位置
    # 中序遍历的根节点左边为左子树，右边为右子树
    # 以此确定左右子树的所含节点的个数
    midIdx = inOrder.index(preOrder[0])
    leftNum = midIdx
    rightNum = len(inOrder)-1-midIdx
    # 3.给根节点挂左右子树的根节点
    # 左子树
    if leftNum > 0:
        # 从原序列中确定左子树的前中遍历序列 递归 返回左子树根节点
        node.left = reconstructTree(preOrder[1 : leftNum+1], inOrder[0 : midIdx])
    # 右子树
    if rightNum > 0:
        # 从原序列中确定右子树的前中遍历序列 递归 返回右子树根节点
        node.right = reconstructTree(preOrder[leftNum+1 :], inOrder[midIdx+1 :])
    return node

# 计算树的叶节点个数
def numOfLeaf(root):
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return 1
    else:
        return numOfLeaf(root.left) + numOfLeaf(root.right)



if __name__ == "__main__":
    # 打开输入文件
    f = open("0.inputfile.txt", "r")
    # 把标准输入流重定向到文件(默认是键盘输入缓冲区)
    sys.stdin = f
    # ========================================
    N = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, sys.stdin.readline().split()))
    res = numOfLeaf(reconstructTree(arr1, arr2))

    print(res)