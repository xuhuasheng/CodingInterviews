import sys

def check(s, lucky):
    ss = list(s)
    dic = {}
    for c in ss:
        if c not in dic:
            dic[c] = 1
        else:
            dic[c] += 1
    luck_c = ss[lucky]
    if 'a' not in dic and 'r' in dic and 'c' in dic and 's' in dic and 'o' in dic and 'f' in dic and 't' in dic:


if __name__ == "__main__":
    # 打开输入文件
    f = open("0.inputfile.txt", "r")
    # 把标准输入流重定向到文件(默认是键盘输入缓冲区)
    sys.stdin = f
    T=int(input())
    for _ in range(T):
        n,m = map(int, input().split())
        for m_ in range(m):
            s, a, b = input().split()
            a = int(a)
            b = int(b)
            lucky = (a**b) % 7
            if len(s) < 7:
                print("no")
                continue

#include <iostream>
#include <string>
#include <vector>

using namespace std;

string model = "arcsoft";

string check(string& str, int a, int b) {
	int index = 1;
	for (int i = 0; i < b; i++) {
		index *= a;
	}
	index = index % 7;
	int len = str.length();
	if (len < 7) {
		return "no";
	}
	for (int i = 0; i + 6 < len; i++) {
		int j = i;
		bool exist = true;
		for (; j < i + 7; j++) {
			if (index == j || str[j] == model[j - i]) {
				continue;
			}
			else {
				exist = false;
				break;
			}
		}
		if (exist == true) {
			return "yes";
		}
	}
	return "no";
}

int main() {
	int T;
	cin >> T;
	vector<vector<string>> res;
	res.resize(T);
	for (int i = 0; i < T; i++) {
		int N, M;
		cin >> N >> M;
		vector<string> ans;
		ans.resize(M);
		for (int j = 0; j < M; j++) {
			string str;
			cin >> str;
			int a, b;
			cin >> a >> b;
			ans[j] = check(str, a, b);
		}
		res.push_back(ans);
	}
	for (auto path : res) {
		for (string str : path) {
			cout << str << endl;
		}
	}

	return 0;
}



