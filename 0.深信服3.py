import sys

     


if __name__ == "__main__":
    # 打开输入文件
    f = open("0.inputfile.txt", "r")
    # 把标准输入流重定向到文件(默认是键盘输入缓冲区)
    sys.stdin = f
    # ========
    T = int(input())
    for _ in range(T):
        N = int(input())
        arr = []
        start = []
        end= []
        cnt = 0
        tmp = 0
        for n in range(N):
            a, b = list(map(int, input().split(' ')))
            arr.append([a, b])
            start.append(a)
            end.append(b)
        s = min(start)
        e = max(end)
        for i in range(s, e+1):
            cnt = 0
            for t in arr:
                if i <= t[1] and i >= t[0]:
                    cnt += 1
            if cnt > tmp:
                tmp = cnt
        print(tmp)

        