# 字符串str1能否提供排列组合成str2

# 输入
# rkqodlw
# world
# 输出
# True

# 直接上字典记录str1的出现字符和次数
# 然后遍历str2，查表，有的话次数要记得减一
import sys
def fun(str1, str2):
    if len(str1) < len(str2):
        return False
    dic = {}
    for i in str1:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    for i in str2:
        if i in dic:
            dic[i] -= 1
            if dic[i] == 0:
                del dic[i]
            continue
        else:
            return False
    return True


if __name__ == "__main__":
    # 打开输入文件
    f = open("0.inputfile.txt", "r")
    # 把标准输入流重定向到文件(默认是键盘输入缓冲区)
    sys.stdin = f
    # ========================================
    str1 = input()
    str2 = input()
    res = fun(str1, str1)
    print(res)