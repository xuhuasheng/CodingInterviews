# include <bits/stdc++.h>
using namespace std;
// typedef pair<int, int> pii;
// typedef long long ll;
string num[2001];
long long vis[2001];
int main() {
    int m;
    cin>>m;
    for (int i=1; i<=m; i++) {
        int op;
        cin>>op;
        if (op == 1) {
            long long a;
            string b;
            cin >> a>>b;
            if(vis[a]) {
                int r=a;
                for(;vis[r];r++);
                for(int j=r; j>a; j--) vis[j]=1, num[j]=num[j-1];
                num[a] = b;
            }
            else {
                num[a] = b;
                vis[a] = 1;
            }
        }
        if(op==2) {
            int a;
            cin>>a;
            int t = 0;
            for(int i=1; i < 2000; i++) {
                if(vis[i]) t++;
                if(t==a) break;
            }
            num[t] = ' ';
            vis[a] = 0;
        }
        if(op==3){
            for (int i=1;i<=2000;i++){
                if(vis[i])
                cout<<num[i]<<' ';
            }
            cout<<"\n";
        }
    }
}
