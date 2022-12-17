#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int H, N, M, res, check;

int dl[6] = {1, -1, 0, 0, 0, 0};
int dr[6] = {0, 0, 1, -1, 0, 0};
int dc[6] = {0, 0, 0, 0, 1, -1};

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> M >> N >> H;

    int arr[H][N][M];
    queue<vector<int>> q;

    for (int l = 0; l < H; l++) {
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < M; c++) {
                int tomato;
                cin >> tomato;
                arr[l][r][c] = tomato;
                if (tomato == 1) {
                    q.push({l, r, c});
                }
            }
        }
    }

    while(!q.empty()) {
        int l1 = q.front()[0];
        int r1 = q.front()[1];
        int c1 = q.front()[2];
        q.pop();
        for (int dir = 0; dir < 6; dir++) {
            int l2 = l1 + dl[dir];
            int r2 = r1 + dr[dir];
            int c2 = c1 + dc[dir];
            if (0 <= l2 && l2 < H && 0 <= r2 && r2 < N && 0 <= c2 && c2 < M && arr[l2][r2][c2] == 0) {
                arr[l2][r2][c2] = arr[l1][r1][c1] + 1;
                q.push({l2, r2, c2});
            }
        }
    }
    for (int l = 0; l < H; l++) {
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < M; c++) {
                if (arr[l][r][c] == 0) {
                    check = 1;
                    break;
                }
                res = max(res, arr[l][r][c]);
            }
            if (check) {
                break;
            }
        }
        if (check) {
            break;
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