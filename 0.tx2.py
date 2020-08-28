import sys

def fun(A, B, x):
    return (A/3) * x**3 + 0.5*x**2+B*x

def helper(A, B, C, D):
    a = fun(A, B, D)
    b = fun(A, B, C)
    return round(a - b, 6)

if __name__ == "__main__":
    # 打开输入文件
    f = open("0.inputfile.txt", "r")
    # 把标准输入流重定向到文件(默认是键盘输入缓冲区)
    sys.stdin = f
    N = int(input())
    for _ in range(N):
        A, B, C, D = map(int, input().split())
        print(helper(A, B, C, D))

# include <iostream>
using namespace std;
double fun(int A, int B, int x) {
    return (double)A/3.0 * pow(x, 3)+0.5*pow(x,2)+ B*x;
}
double helper(int A, int B, int C, int D) {
    double a = fun(A, B, D);
    double b = fun(A, B, C);
    return a-b;
}
int main() {
    int n;
    cin>>n;
    for (int i=0; i<n; i++) {
        int A,B,C,D;
        cin>>A>>B>>C>>D;
        cout<<helper(A, B, C, D)<<endl;
    }
}
