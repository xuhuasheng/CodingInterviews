# 先遍历的后输出，反向操作想到栈
class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.__list = []
    def isEmpty(self):
        return self.__list == []
    def push(self, data):
        self.__list.append(data)
    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.__list.pop()
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.__list[-1]
    def size(self):
        return len(self.__list)

# 栈实现
def printListReverse(head:ListNode):
    stack = Stack()
    node = head
    while node.next is not None:
        stack.push(node.data)
        node = node.next
    while not stack.isEmpty():
        print(stack.pop())

# 递归实现
def printListReverse2(head:ListNode):
    if head is not None:
        if head.next is not None:
            printListReverse2(head.next)
        print(head.data)