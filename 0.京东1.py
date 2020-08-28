
# 路径动态规划
# 路径表是等腰直角三角形
# 小球从顶点滚下，选择的路径是左下、下、右下
# 求小球走路径的最大得分
# 3     #行数
#     1
#   2 1 2
# 3 4 2 1 3
import sys
if __name__ == "__main__":
    # 打开输入文件
    f = open("0.inputfile.txt", "r")
    # 把标准输入流重定向到文件(默认是键盘输入缓冲区)
    sys.stdin = f
    n = int(input())
    # import numpy as np
    # 这里不能用二维list，[[0]*210]*210, 要用np.array
    # a = np.zeros((210,210), dtype=np.int)   #路径分数表
    a = [[0 for j in range(210)] for i in range(210)]
    # dp = np.zeros((210,210),dtype=np.int)   #二维dp表，此题不能压缩成一维
    dp = [[0 for j in range(210)] for i in range(210)]
    for i in range(1, n+1):
        tmp = list(map(int, input().split(' ')))
        for j in range(n-i+1, n+i-1 + 1):
            a[i][j] = tmp[j-n+i-1]
    # 从最低行往上递推到顶点位置
    for i in range(n, 0, -1):
        for j in range(n-i+1, n+i-1 + 1):
            dp[i][j] = a[i][j] + max(dp[i+1][j-1], dp[i+1][j], dp[i+1][j+1])
    print(dp[i][n])