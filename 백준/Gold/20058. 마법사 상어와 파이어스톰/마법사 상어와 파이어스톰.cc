#include <iostream>
#include <queue>

using namespace std;

int dr[] = {0, 0, -1, 1}, dc[] = {1, -1, 0, 0};

int N, Q, res1, res2;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> Q;

    int tmp_n = 1;

    for (int i = 0; i < N; i++) {
        tmp_n *= 2;
    }

    int arr[tmp_n][tmp_n];
    int visited[tmp_n][tmp_n];
    for (int r = 0; r < tmp_n; r++) {
        for (int c = 0; c < tmp_n; c++) {
            visited[r][c] = 0;
        }
    }

    int arr_L[Q];
    for (int i = 0; i < Q; i++) {
        arr_L[i] = 0;
    }

    for (int i = 0; i < tmp_n; i++){
        for (int j = 0; j < tmp_n; j++) {
            cin >> arr[i][j];
        }
    }

    for (int i = 0; i < Q; i++) {
        cin >> arr_L[i];
    }

    int cnt = 0;

    while (cnt < Q) {
        // 구간 나누기 시작, odd - 짝수 홀수 판단

        int tmp_r = 0, tmp_c = 0, tmp_v = 1, L = -1;

        while (true) {
            if (L < 0) {
                L = arr_L[cnt];
                if (L == 0) {
                    break;
                }
                //// 격자 크기 구하기
                for (int i = 0; i < L; i++) {
                    tmp_v *= 2;
                }
            }

            //// 교체할 수 있는 가짜 배열 생성
            int tmp_arr[tmp_v][tmp_v];
            for (int r = 0; r < tmp_v; r++) {
                for (int c = 0; c < tmp_v; c++) {
                    tmp_arr[r][c] = -1;
                }
            }

            // 만약 tmp_v 범위를 넘어버리면 줄바꿈
            if (tmp_v + tmp_c > tmp_n) {
                tmp_c = 0, tmp_r += tmp_v;
            }

            if (tmp_r == tmp_n) {
                break;
            }

            //// 배열 돌리기
            for (int r = tmp_r; r < tmp_r + tmp_v; r++) {
                for (int c = tmp_c; c < tmp_c + tmp_v; c++) {
                    tmp_arr[c - tmp_c][tmp_r + tmp_v - 1 - r] = arr[r][c];
                }
            }

            for (int r = tmp_r; r < tmp_r + tmp_v; r++) {
                for (int c = tmp_c; c < tmp_c + tmp_v; c++) {
                    arr[r][c] = tmp_arr[r-tmp_r][c-tmp_c];
                }
            }
            tmp_c += tmp_v;
        }

//        cout << '\n';
//        for (int r = 0; r < tmp_n; r++) {
//            for (int c = 0; c < tmp_n; c++) {
//                cout << arr[r][c] << ' ';
//            }
//            cout << '\n';
//        }

        queue<pair<int, int>> q2;
        for (int r = 0; r < tmp_n; r++) {
            for (int c = 0; c < tmp_n; c++) {
                int check = 0;
                for (int dir = 0; dir < 4; dir++) {
                    int r2 = r + dr[dir];
                    int c2 = c + dc[dir];
                    if (0 <= r2 && r2 < tmp_n && 0 <= c2 && c2 < tmp_n && arr[r2][c2]) {
                        check++;
                    }
                }
                if (check < 3 && arr[r][c] > 0) {
                    q2.push({r, c});
                }
            }
        }
        while (!q2.empty()) {
            int r5 = q2.front().first;
            int c5 = q2.front().second;
            q2.pop();
            if (arr[r5][c5] > 0) {
                arr[r5][c5] -= 1;
            }
        }
        cnt++;
    }

    for (int r = 0; r < tmp_n; r++) {
        for (int c = 0; c < tmp_n; c++) {
            res1 += arr[r][c];
        }
    }

    for (int r = 0; r < tmp_n; r++) {
        for (int c = 0; c < tmp_n; c++) {
            int tmp_res2 = 0;
            queue<pair<int, int>> q;
            if (visited[r][c] == 0 && arr[r][c] > 0) {
                q.push({r, c});
                visited[r][c] = 1;
                tmp_res2++;
            }
            while (!q.empty()) {
                int r3 = q.front().first;
                int c3 = q.front().second;
                q.pop();
                for (int i = 0; i < 4; i++) {
                    int r4 = r3 + dr[i];
                    int c4 = c3 + dc[i];
                    if (0 <= r4 && r4 < tmp_n && 0 <= c4 && c4 < tmp_n && visited[r4][c4] == 0 && arr[r4][c4] > 0) {
                        tmp_res2 += 1;
                        visited[r4][c4] = 1;
                        q.push({r4, c4});
                    }
                }
            }
            if (tmp_res2 > res2) {
                res2 = tmp_res2;
            }
        }
    }
    cout << res1 << '\n' << res2;

    return 0;
}