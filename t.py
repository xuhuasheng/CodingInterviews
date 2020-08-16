import sys
import math
def fun(m, n): 
    res = ""
    digt = [0] *3
    for x in range(m, n+1):
        tmp = x
        for i in range(2, -1, -1):
            digt[i] = tmp % 10
            tmp = tmp // 10
        if sum([j**3 for j in digt]) == x:
            res += str(x)
            res += ' '
    if res == "":
        return "no"
    else:
        return res


    
def duomiruo(hList, wList):
    import numpy as np
    hList_sidx = sorted(range(len(hList)), key=lambda k : hList[k])
    wList_sidx = sorted(range(len(wList)), key=lambda k : wList[k])
    # hList_sidx = np.argsort(np.array(hList))
    # wList_sidx = np.argsort(np.array(wList))
    maxcnt = 0
    for i in range(len(hList_sidx)):
        j = wList_sidx.index(hList_sidx[i])
        cnt = validNum(i, j, hList_sidx, wList_sidx)
        if maxcnt < cnt:
            maxcnt = cnt
    return maxcnt

def validNum(i, j, hList_sidx, wList_sidx):
    length = len(wList_sidx)
    cnt = 1
    for h in range(i+1, length):
        if wList_sidx.index(hList_sidx[h]) < j:
            break
        else:
            cnt += 1
            j = wList_sidx.index(hList_sidx[h])
    return cnt


if __name__ == "__main__":
    # 打开输入文件
    f = open("0.inputfile.txt", "r")
    # 把标准输入流重定向到文件(默认是键盘输入缓冲区)
    sys.stdin = f
    # ========================================
    while 1:
        try:
            arr = list(map(int, input().split()))
            n = int(input())
            print(res)
        except:
            break