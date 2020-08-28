import sys 
# 在n个正整数中，任意挑选k个数字，之和计为sum，另有一个正整数m，请问sum%m的最大是多少


# 输入
# 5 5
# 1 2 3 4 5
# 输出
# 4

# max(sum%m)的取值为[0, m-1]
# 从m-1开始遍历，转化为完全背包问题
def fun(arr, m):
    for i in range(m-1, 0, -1):
        if package(arr, i):
            return i
    return 0

def package(arr, n):
    dp = [n+1] * (n+1)
    dp[0] = 0
    for i in range(1, n+1):
        for j in arr:
            if i>=j:
                dp[i] = min(dp[i], 1+dp[i-j])
    if dp[n] == n+1:
        return False
    else:
        return True

if __name__ == "__main__":
    # 打开输入文件
    f = open("0.inputfile.txt", "r")
    # 把标准输入流重定向到文件(默认是键盘输入缓冲区)
    sys.stdin = f
    # ========================================
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    res = fun(arr, m)
    print(res)