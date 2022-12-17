#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int N, M, res;

int dr[4] = {1, -1, 0, 0}, dc[4] = {0, 0, 1, -1};

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M;

    int arr[N][M];

    queue<vector<int>> q;

    for (int r = 0; r < N; r++) {
        for (int c = 0; c < M; c++) {
            int ice;
            cin >> ice;
            arr[r][c] = ice;
            if (ice != 0) {
                q.push({r, c, 0});
            }
        }
    }
    int check = 0;

    while (!q.empty()) {
        while(!q.empty()) {
            int cnt = q.front()[2];
            if (cnt != check) {
                break;
            }
            int r1 = q.front()[0];
            int c1 = q.front()[1];
            q.pop();
            for (int i = 0; i < 4; i++) {
                int r2 = r1 + dr[i];
                int c2 = c1 + dc[i];
                if (0 <= r2 && r2 < N && 0 <= c2 && c2 < M) {
                    if (arr[r2][c2] == 0 && arr[r1][c1] > 1) {
                        arr[r1][c1]--;
                    }
                    else if (arr[r2][c2] == 0 && arr[r1][c1] == 1) {
                        arr[r1][c1] = -1;
                    }
                }
            }
            if (arr[r1][c1] != -1) {
                q.push({r1, c1, cnt+1});
            }
        }

        check++;

        int visited[N][M], island = 0;

        for (int r = 0; r < N; r++) {
            for (int c = 0; c < M; c++) {
                if (arr[r][c] == -1) {
                    arr[r][c]++;
                }
                visited[r][c] = 0;
            }
        }

        queue<pair<int, int>> q2;

        for (int r = 0; r < N; r++) {
            for (int c = 0; c < M; c++) {
                if (arr[r][c] !=0 && visited[r][c] != 1) {
                    q2.push({r, c});
                    visited[r][c] = 1;
                    island++;

                    while (!q2.empty()) {
                        int cr1 = q2.front().first;
                        int cc1 = q2.front().second;
                        q2.pop();
                        for (int i = 0; i < 4; i++) {
                            int cr2 = cr1 + dr[i];
                            int cc2 = cc1 + dc[i];
                            if (0 <= cr2 && cr2 < N && 0 <= cc2 && cc2 < M && visited[cr2][cc2] == 0 && arr[cr2][cc2]) {
                                visited[cr2][cc2] = 1;
                                q2.push({cr2, cc2});
                            }
                        }
                    }
                }
                if (island > 1) {
                    break;
                }
            }
            if (island > 1) {
                break;
            }
        }
        if (island > 1) {
            res = check;
            break;
        }
    }
    cout << res;

    return 0;
}