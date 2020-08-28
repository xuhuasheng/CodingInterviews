import sys
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = [] #创建一个空栈
    # s = "".join(s.split())
    #s里面没有括号
    if not s:
        return 0
    for i in s:
        if stack == []:
            stack.append(i)
        elif i == '[' or i == '(':
            stack.append(i)
        elif i == ']':
            if stack[-1]== '[':
                stack.pop()
            else:
                stack.append(i)
        elif i == ')':
            if stack[-1]== '(':
                stack.pop()
            else:
                stack.append(i)
    return len(stack)

if __name__ == "__main__":
    # 打开输入文件
    #f = open("0.inputfile.txt", "r")
    # 把标准输入流重定向到文件(默认是键盘输入缓冲区)
    #sys.stdin = f
    # s = list(input())
    s=")(][][)("
    print(isValid(s))
    # return r1+r2