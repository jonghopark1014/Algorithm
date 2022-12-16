#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int R, C, res;
char arr[1003][1003];
int dr[4] = {0, 0, -1, 1}, dc[4] = {1, -1, 0, 0};

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> R >> C;

    queue<vector<int>> pQ;
    queue<vector<int>> fQ;

    for (int r = 0; r < R; r++) {
        string tmp;
        cin >> tmp;
        for (int c = 0; c < C; c++) {
            arr[r][c] = tmp[c];
            if (tmp[c] == 'J') {
                pQ.push({r, c, 1});
            }
            else if (tmp[c] == 'F') {
                fQ.push({r, c, 1});
            }
        }
    }

    int cnt = 1;

    while (!pQ.empty()) {
        while (!pQ.empty() && pQ.front()[2] == cnt) {
            int r2 = pQ.front()[0];
            int c2 = pQ.front()[1];
            int acc = pQ.front()[2];
            if (acc == 1 && ((r2 == 0 || r2 == R - 1) || (c2 == 0 || c2 == C - 1))) {
                cnt = 0;
                break;
            }
            if (cnt == 0) {
                break;
            }

            pQ.pop();
            if (arr[r2][c2] == 'J') {
                for (int i = 0; i < 4; i++) {
                    int r3 = r2 + dr[i];
                    int c3 = c2 + dc[i];
                    if (0 <= r3 && r3 << R && 0 <= c3 && c3 < C && arr[r3][c3] == '.') {
                        pQ.push({r3, c3, acc+ 1});
                        arr[r3][c3] = 'J';
                    }
                }
            }
        }
        if (res == 1) {
            break;
        }
        while (!fQ.empty() && !pQ.empty() && fQ.front()[2] == cnt) {
            int fr2 = fQ.front()[0];
            int fc2 = fQ.front()[1];
            int facc = fQ.front()[2];
            fQ.pop();
            for (int i = 0; i < 4; i++) {
                int fr3 = fr2 + dr[i];
                int fc3 = fc2 + dc[i];
                if (0 <= fr3 && fr3 < R && 0<= fc3 && fc3 < C) {
                    if (arr[fr3][fc3] == '.' || arr[fr3][fc3] == 'J') {
                        fQ.push({fr3, fc3, facc + 1});
                        arr[fr3][fc3] = 'F';
                    }
                }
            }
        }
        for (int r = 0; r < R; r++) {
            if (arr[r][0] == 'J' || arr[r][C-1] == 'J') {
                res = 1;
                break;
            }
        }
        for (int c = 0; c < C; c++) {
            if (arr[0][c] == 'J' || arr[R - 1][c] == 'J') {
                res = 1;
                break;
            }
        }
        if (res) {
            break;
        }
        cnt++;
    }
    if (!res) {
        cout << "IMPOSSIBLE";
    }
    else {
        cout << cnt + 1;
    }
}
