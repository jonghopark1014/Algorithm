#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

int n, m, arr[500][500], visited[500][500], cnt, res;

int dr[4] = {0, 0, 1, -1}, dc[4] = {1, -1, 0, 0};

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;

    for (int r = 0; r < n; r++) {
        for (int c = 0; c < m; c++) {
            cin >> arr[r][c];
        }
    }

    for (int r = 0; r < n; r++) {
        for (int c = 0; c < m; c++) {
            if (arr[r][c] && !visited[r][c]) {
                int pic = 1;
                cnt++;

                queue<pair<int, int>> Q;
                Q.push({r, c});
                visited[r][c] = 1;
                while (!Q.empty()) {
                    pair<int, int> location = Q.front(); Q.pop();
                    int r2 = location.first;
                    int c2 = location.second;
                    for (int i = 0; i < 4; i++) {
                        int r3 = r2 + dr[i];
                        int c3 = c2 + dc[i];
                        if (0 <= r3 && r3 < n && 0 <= c3 && c3 < m && !visited[r3][c3] && arr[r3][c3]) {
                            Q.push({r3, c3});
                            visited[r3][c3] = 1;
                            pic++;
                        }
                    }
                }
                res = max(res, pic);
            }
        }
    }
    cout << cnt << '\n';
    cout << res;
    return 0;
}