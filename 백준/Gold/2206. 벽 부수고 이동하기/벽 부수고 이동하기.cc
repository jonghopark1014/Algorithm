#include <iostream>
#include <queue>

using namespace std;

int N, M, check, res;
char arr[1000][1000];

int dr[4] = {0, 0, -1, 1}, dc[4] = {1, -1, 0, 0};


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M;

    int visited[N][M];
    int cnt_arr[N][M];

    for (int r = 0; r < N; r++) {
        string tmp;
        cin >> tmp;
        for (int c = 0; c < M; c++) {
            visited[r][c] = 1;
            cnt_arr[r][c] = 1000000;
            arr[r][c] = tmp[c];
        }
    }
    queue<vector<int>> q;
    q.push({0, 0, 1, 1});
    while (!q.empty()) {
        int r1 = q.front()[0];
        int c1 = q.front()[1];
        int cnt = q.front()[2];
        if (r1 == N - 1 && c1 == M - 1) {
            check = 1;
            res = cnt;
            break;
        }
        int wall = q.front()[3];
        q.pop();
        for (int i = 0; i < 4; i++) {
            int r2 = r1 + dr[i];
            int c2 = c1 + dc[i];
            if (0 <= r2 && r2 < N && 0 <= c2 && c2 < M) {
                if (arr[r2][c2] == '1') {
                    if (wall && cnt_arr[r2][c2] > cnt + 1) {
                        cnt_arr[r2][c2] = cnt + 1;
                        visited[r2][c2] = 0;
                        q.push({r2, c2, cnt + 1, 0});
                    }
                }
                else {
                    if (visited[r2][c2] == 1) {
                        if (wall) {
                            visited[r2][c2] = 2;
                            q.push({r2, c2, cnt + 1, 1});
                        }
                        else {
                            if (cnt_arr[r2][c2] > cnt + 1) {
                                q.push({r2, c2, cnt + 1, 0});
                                cnt_arr[r2][c2] = cnt + 1;
                            }
                        }
                    }
                    else {
                        if (wall && cnt_arr[r2][c2] > cnt + 1) {
                            cnt_arr[r2][c2] = cnt + 1;
                            q.push({r2, c2, cnt + 1, 1});
                        }
                    }
                }
            }
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