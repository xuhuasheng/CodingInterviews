# include <bits/stdc++.h>
using namespace std;
const int N = 210;
int n, a[N][N], f[N][N];

int main() {
    scanf("%d", &n);
    for (int i=1;i<=n; i++) {
        for (int j=n-i+1; j<=n+i-1; j++){
            scanf("%d", &a[i][j]);
        }
    }
    for (int i=n;i>0;i--) {
        for(int j=n-i+1; j<=n+i-1; ++j) {
            f[i][j] = a[i][j] + max(f[i+1][j-1], max(f[i+1][j], f[i+1][j+1]));
        }
    }
    cout<<f[1][n];
    return 0;
}
