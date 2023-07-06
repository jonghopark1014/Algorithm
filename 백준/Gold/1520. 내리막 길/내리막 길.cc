#include <iostream>

using namespace std;

int N, M, arr[501][501], H, dp[501][501];
int dr[] = {-1, 1, 0, 0}, dc[] = {0,0, -1, 1};

void input() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> M >> N;
    for (int r = 0; r < M; r++) {
        for (int c = 0; c < N; c++) {
            cin >> arr[r][c];
            dp[r][c] = -1;
        }
    }
}

int walking(int r, int c) {
    if (r == M - 1 && c == N - 1) {
        return 1;
    }
    if (dp[r][c] != -1) {
        return dp[r][c];
    }
    dp[r][c] = 0;
    for (int i = 0; i < 4; i++) {
        int tmp_r = r + dr[i];
        int tmp_c = c + dc[i];
        if (0 <= tmp_r && tmp_r < M && 0 <= tmp_c && tmp_c < N) {
            if (arr[r][c] > arr[tmp_r][tmp_c]) {
                dp[r][c] += walking(tmp_r, tmp_c);
            }
        }
    }
    return dp[r][c];
}


int main() {
    input();
    cout << walking(0, 0);

    return 0;
}