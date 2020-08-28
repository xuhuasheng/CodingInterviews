import sys
if __name__ == "__main__":
    # 打开输入文件
    f = open("0.inputfile.txt", "r")
    # 把标准输入流重定向到文件(默认是键盘输入缓冲区)
    sys.stdin = f
    arr = list(map(float, input().split(',')))
    min = arr[0]
    for i in arr:
        if  i < min:
            min = i
    cnt = 0
    for i in arr:
        if i == min:
            cnt += 1
    print(cnt)