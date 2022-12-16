#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int N, M, K, check, res;

int dr[4] = {0, 0, -1, 1}, dc[4] = {1, -1, 0, 0};

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M >> K;

    char arr[N][M];
    vector<vector<pair<int, int>>> visited(N, vector<pair<int, int>>(M, {0, 0}));

    for (int r = 0; r < N; r++) {
        string tmp;
        cin >> tmp;
        for (int c = 0; c < M; c++) {
            arr[r][c] = tmp[c];
            visited[r][c].first = -1;
            visited[r][c].second = N * M;
        }
    }

    queue<vector<int>> q;

    q.push({0, 0, K, 1});

    while (!q.empty()) {
        int r = q.front()[0];
        int c = q.front()[1];
        int cnt = q.front()[3];
        if (r == N - 1 && c == M - 1) {
            check = 1;
            res = cnt;
            break;
        }
        int wall = q.front()[2];
        q.pop();
        for (int dir = 0; dir < 4; dir++) {
            int r2 = r + dr[dir];
            int c2 = c + dc[dir];
            if (0 <= r2 && r2 < N && 0 <= c2 && c2 < M) {
                if (arr[r2][c2] == '1' && wall) {
                    if (visited[r2][c2].first < wall - 1) {
                        q.push({r2, c2, wall - 1, cnt + 1});
                        visited[r2][c2].first = wall - 1;
                        visited[r2][c2].second = cnt;
                    }
                    else if (visited[r2][c2].second > cnt) {
                        q.push({r2, c2, wall - 1, cnt + 1});
                    }
                }
                else if (arr[r2][c2] == '0') {
                    if (visited[r2][c2].first < wall) {
                        q.push({r2, c2, wall, cnt + 1});
                        visited[r2][c2].first = wall;
                        visited[r2][c2].second = cnt;
                    }
                    else if (visited[r2][c2].second > cnt) {
                        q.push({r2, c2, wall, cnt + 1});
                    }
                }
            }
        }
        if (check) {
            break;
        }
    }
    if (check) {
        cout << res;
    }
    else {
        cout << -1;
    }

    return 0;
}