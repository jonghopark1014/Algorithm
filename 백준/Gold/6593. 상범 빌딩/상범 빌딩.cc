#include <iostream>
#include <queue>

using namespace std;

int L, R, C, EP[3], res, check;
int dr[6] = {0, 0, -1, 1, 0, 0}, dc[6] = {1, -1, 0, 0, 0, 0};
int dl[6] = {0, 0, 0, 0, -1, 1};
char arr[30][30][30];


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    while (true) {

        cin >> L >> R >> C;

        if (L == 0 && R == 0 && C == 0) {
            break;
        }
        queue<vector<int>> q;
        for (int l = 0; l < L; l++) {
            for (int r = 0; r < R; r++) {
                string tmp;
                cin >> tmp;
                for (int c = 0; c < C; c++) {
                    if (tmp[c] == 'S') {
                        q.push({l, r, c, res});
                    }
                    else if (tmp[c] == 'E') {
                        EP[0] = l;
                        EP[1] = r;
                        EP[2] = c;
                    }
                    arr[l][r][c] = tmp[c];
                }
            }
        }
        while (!q.empty()) {
            int l2 = q.front()[0];
            int r2 = q.front()[1];
            int c2 = q.front()[2];
            int cnt = q.front()[3];
            q.pop();
            if (EP[0] == l2 && EP[1] == r2 && EP[2] == c2) {
                check = 1;
                res = cnt;
                break;
            }
            for (int dir = 0; dir < 6; dir++) {
                int l3 = l2 + dl[dir];
                int r3 = r2 + dr[dir];
                int c3 = c2 + dc[dir];
                if (0 <= l3 && l3 < L && 0 <= r3 && r3 < R && 0 <= c3 && c3 < C && (arr[l3][r3][c3] == '.' || arr[l3][r3][c3] == 'E')) {
                    q.push({l3, r3, c3, cnt + 1});
                    arr[l3][r3][c3] = 'S';
                }
            }
        }
        if (!check) {
            cout << "Trapped!" << '\n';
        }
        else {
            cout << "Escaped in " << res << " minute(s)." << '\n';
        }
        for (int l = 0; l < L; l++) {
            for (int r = 0; r < R; r++) {
                for (int c = 0; c < C; c++) {
                    arr[l][r][c] = '#';
                }
            }
        }
        res = 0;
        check = 0;
    }

    return 0;
}