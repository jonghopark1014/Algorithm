#include <iostream>
#include <queue>

using namespace std;

int dr[] = {1, -1, 0, 0}, dc[] = {0, 0, -1, 1};

int N, M, res;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M;

    int arr[N][N], light_info[M][4], light_room[N][N];

    for (int i = 0; i < M; i++) {
        for (int j = 0; j < 4; j++) {
            int num;
            cin >> num;
            light_info[i][j] = num - 1;
        }
    }

    for (int r = 0; r < N; r++) {
        for (int c = 0; c < N; c++) {
            if (r == 0 && c == 0) {
                arr[r][c] = 1;
                res++;
            }
            else {
                arr[r][c] = 0;
            }
            light_room[r][c] = 0;
        }
    }

    queue<pair<int, int>> q;
    queue<pair<int, int>> q2;

    q.push({0, 0});

    while (true) {

        if (q.empty()) {
            break;
        }

        while(!q.empty()) {
            int r1 = q.front().first;
            int c1 = q.front().second;
            q.pop();
            light_room[r1][c1] = 1;
            for (int i = 0; i < M; i++) {
                if (light_info[i][1] == r1 && light_info[i][0] == c1 && arr[light_info[i][3]][light_info[i][2]] == 0) {
                    arr[light_info[i][3]][light_info[i][2]] = 1;
                    res++;
                }
            }
        }

        q2.push({0, 0});


        int visited[N][N];
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                visited[r][c] = 0;
            }
        }

        while (!q2.empty()) {
            int r2 = q2.front().first;
            int c2 = q2.front().second;
            q2.pop();

            for (int i = 0; i < 4; i++) {
                int r3 = r2 + dr[i];
                int c3 = c2 + dc[i];
                if (0 <= r3 && r3 < N && 0 <= c3 && c3 < N && arr[r3][c3] == 1 && visited[r3][c3] == 0) {
                    q2.push({r3, c3});
                    visited[r3][c3] = 1;
                    if (light_room[r3][c3] == 0) {
                        q.push({r3, c3});
                    }
                }
            }
        }
    }

    cout << res;

    return 0;
}