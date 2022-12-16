#include <iostream>
#include <queue>

using namespace std;

int N, M, check, res;

int dr[4] = {0, 0, -1, 1}, dc[4] = {1, -1, 0, 0};

int main() {
    cin >> M >> N;

    int arr[N][M];

    queue<pair<int, int>> q;

    for (int r = 0; r < N; r++) {
        for (int c = 0; c < M; c++) {
            int tomato;
            cin >> tomato;
            arr[r][c] = tomato;
            if (tomato == 1) {
                q.push({r, c});
            }
        }
    }

    while (!q.empty()) {
        int r1 = q.front().first;
        int c1 = q.front().second;
        q.pop();
        for (int dir = 0; dir < 4; dir++) {
            int r2 = r1 + dr[dir];
            int c2 = c1 + dc[dir];
            if (0<= r2 && r2 < N && 0 <= c2 && c2 < M && arr[r2][c2] == 0) {
                arr[r2][c2] = arr[r1][c1] + 1;
                q.push({r2, c2});
            }
        }
    }

    for (int r = 0; r < N; r++) {
        for (int c = 0; c < M; c++) {
            if (arr[r][c] == 0) {
                check = 1;
                break;
            }
            res = max(res, arr[r][c]);
        }
    }

    if (check) {
        cout << -1;
    }
    else {
        cout << res - 1;
    }

    return 0;
}