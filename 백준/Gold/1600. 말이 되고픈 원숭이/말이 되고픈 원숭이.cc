#include <iostream>
#include <queue>

using namespace std;

int dr[12] = {1, -1, 0, 0, 2, 2, -2, -2, 1, 1, -1, -1};
int dc[12] = {0, 0, -1, 1, 1, -1, 1, -1, 2, -2, 2, -2};

int K, W, H, res, check;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> K >> W >> H;

    queue<vector<int>> q;

    int arr[H][W], visited[H][W], cnt_arr[H][W];

    for (int r = 0; r < H; r++) {
        for (int c = 0; c < W; c++) {
            cin >> arr[r][c];
            visited[r][c] = K + 1;
            cnt_arr[r][c] = H * W;
        }
    }
    visited[0][0] = 0;
    cnt_arr[0][0] = 0;

    q.push({0, 0, 0, 0});

    while (!q.empty()) {
        int r1 = q.front()[0];
        int c1 = q.front()[1];
        int cnt = q.front()[2];
        int k = q.front()[3];
        if (r1 == H - 1 && c1 == W - 1) {
            check = 1;
            res = cnt;
            break;
        }

        q.pop();
        for (int i = 0; i < 12; i++) {
            if (k < K && i >= 4) {
                int r2 = r1 + dr[i];
                int c2 = c1 + dc[i];
                int k2 = k + 1;
                if (r2 == H - 1 && c2 == W - 1) {
                    check = 1;
                    res = cnt + 1;
                    break;
                }
                if (0 <= r2 && r2 < H && 0 <= c2 && c2 < W && arr[r2][c2] == 0) {
                    if (cnt_arr[r2][c2] < cnt + 1) {
                        if (visited[r2][c2] > k) {
                            q.push({r2, c2, cnt + 1, k2});
                            visited[r2][c2] = k2;
                            cnt_arr[r2][c2] = cnt + 1;
                        }
                    }
                    else {
                        if (visited[r2][c2] > k2) {
                            visited[r2][c2] = k2;
                            cnt_arr[r2][c2] = cnt + 1;
                            q.push({r2, c2, cnt + 1, k2});
                        }
                    }
                }
            }
            else if (i < 4){
                int r2 = r1 + dr[i];
                int c2 = c1 + dc[i];
                if (r2 == H - 1 && c2 == W - 1) {
                    check = 1;
                    res = cnt + 1;
                    break;
                }
                if (0 <= r2 && r2 < H && 0 <= c2 && c2 < W && arr[r2][c2] == 0) {
                    if (cnt_arr[r2][c2] < cnt + 1) {
                        if (visited[r2][c2] > k) {
                            q.push({r2, c2, cnt + 1, k});
                            visited[r2][c2] = k;
                            cnt_arr[r2][c2] = cnt + 1;
                        }
                    }
                    else {
                        if (visited[r2][c2] > k) {
                            visited[r2][c2] = k;
                            cnt_arr[r2][c2] = cnt + 1;
                            q.push({r2, c2, cnt + 1, k});
                        }
                    }
                }
            }
        }
        if (check == 1) {
            break;
        }
    }
    if (check == 1) {
        cout << res;
    }
    else {
        cout << -1;
    }



    return 0;
}