import sys 


# 完全背包问题：动态规划
# f(0) = 0
# f(n) = min(1+f(n-i)) if i <= n
def trip(arr, n):
    # dp数组初始化为“无穷大”=》n+1
    dp = [n+1] * (n+1)
    # f(0) = 0
    dp[0] = 0
    # 从f(0)递推到f(n)
    for i in range(1, n+1):
        # 遍历每个硬币
        for coin in arr:
            # 如果可装
            if i >= coin:
                # 遍历coin 求 dp[i-coin]的最小值
                dp[i] = min(dp[i], 1+dp[i-coin])
    # 如果未更新dp的初始化，则说明无解
    if dp[n] == n + 1:
        return -1
    else:
        return dp[n]
    

if __name__ == "__main__":
    # 打开输入文件
    f = open("0.inputfile.txt", "r")
    # 把标准输入流重定向到文件(默认是键盘输入缓冲区)
    sys.stdin = f
    # ========================================
    arr = list(map(int, input().split()))
    n = int(input())
    arr.sort()
    print(trip(arr, n))

