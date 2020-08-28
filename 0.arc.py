import sys
if __name__ == "__main__":
    # 打开输入文件
    f = open("0.inputfile.txt", "r")
    # 把标准输入流重定向到文件(默认是键盘输入缓冲区)
    sys.stdin = f
    n,m= map(int, input().split())
    a = input()
    b = a.split()
    b.sort()
    print(b)
    for i in range(n):
        print(list(map(int, input().split())))