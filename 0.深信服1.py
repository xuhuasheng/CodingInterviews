import sys

def func(n):
    if n <= 3:
        return 0
    if 4 <= n and n <= 6:
        return 1
    k = ((n-7)//5+1) * 2
    base = 5*((n-7)//5) + 7
    idx = n-base
    if idx >= 0 and idx <=2:
        return k
    else:
        return k+1

if __name__ == "__main__":
    # 打开输入文件
    f = open("0.inputfile.txt", "r")
    # 把标准输入流重定向到文件(默认是键盘输入缓冲区)
    sys.stdin = f
    # ========
    N = int(input())
    for _ in range(N):
        n = int(input())
        print(func(n))

    t=int(input())
    for _ in range(t):
        x = int(input())
        if x<4:
            print(0)
        else:
            i=1
            while x>=(i+1)*2*i:
                i+=1
            x -= i * 2 * (i - 1)
            ans=(i-1)**2
            while x>=3:
                x-=3
                ans+=1
                if x>2*(i-1):
                    x-=2*(i-1)
                    ans+=i-1
                else:
                    ans+=x//2
                    break
                i+=1
            print(ans)