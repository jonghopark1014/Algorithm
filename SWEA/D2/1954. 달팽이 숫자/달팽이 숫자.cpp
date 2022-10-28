#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int dr[4] = {0, 1, 0, -1};
int dc[4] = {1, 0, -1, 0};

int main() {
    ios_base::sync_with_stdio(false);
	cin.tie(0);
    cout.tie(0);

    int T = 0;
    cin >> T;
    for (int tc = 1; tc < T + 1; tc++) {
        int N = 0;
        cin >> N;
        vector<vector<int>> snailR;
        vector<int> snailC(N);
        for (int k = 0; k < N; k++) {
            for (int j = 0; j < N; j++) {
                snailC[j] = 0;
            }
            snailR.push_back(snailC);
        }
        // 상 0 우 1 하 2 좌 3
        int cnt = 0;
        int r = 0;
        int c = -1;
        int dir = 0;
        while (true) {
            if (cnt == pow(N, 2)) {
                break;
            }
            else {
                cnt += 1;
                r += dr[dir];
                c += dc[dir];
                if (0 <= r && r < N && 0 <= c && c < N && snailR[r][c] == 0) {
                    snailR[r][c] = cnt;
                } else {
                    r -= dr[dir];
                    c -= dc[dir];
                    dir = (dir + 1) % 4;
                    cnt -= 1;
                }
            }
        }
        cout << '#' << tc <<endl;
        for (int r2 = 0; r2 < N; r2++) {
            for (int c2=0; c2 < N; c2++) {
                cout << snailR[r2][c2] << ' ';
            }
            cout << endl;
        }
    }
    return 0;
}