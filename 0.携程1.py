import sys 
# 给定两个有序数组
# 找这两个数组合并后的中位数
# 输入
# 300 500 650 700
# 200 275 330
# 输出
# 330

def ctrip(arr1, arr2):
    k = (len(arr1)+len(arr2)+1) // 2
    res = []
    while len(arr1) > 0 and len(arr2) > 0:
        if arr1[0] <= arr2[0]:
            res.append(arr1.pop(0))
        else:
            res.append(arr2.pop(0))
    res += arr1
    res += arr2
    return res[k-1]
    

if __name__ == "__main__":
    # 打开输入文件
    f = open("0.inputfile.txt", "r")
    # 把标准输入流重定向到文件(默认是键盘输入缓冲区)
    sys.stdin = f
    # ========================================
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    print(ctrip(arr1, arr2))
