#include <iostream>
#include <algorithm>
#include <deque>

using namespace std;

int N, M, K;
bool check[100][100], condo[100][100];

int dr[] = {0, 0, -1, 1};
int dc[] = {1, -1, 0, 0};

void init() {
    cin >> N >> M >> K;

    for (int r = 0; r < N; r++)
        for (int c = 0; c < M; c++)
        {
            check[r][c] = false;
            condo[r][c] = false;
        }


    int a, b;
    for (int i = 0; i < K; i++) {
        cin >> a >> b;
        condo[a - 1][b - 1] = true;
    }
}

int bfs(int r, int c) {
    int cnt = 0;
    deque<pair<int, int>> dq;
    dq.emplace_back(r, c);

    check[r][c] = true;
    while (!dq.empty()) {
        auto a = dq.front();
        dq.pop_front();
        cnt++;

        for (int i = 0; i < 4; i++) {
            int r2 = a.first + dr[i];
            int c2 = a.second + dc[i];
            if (0 <= r2 && r2 < N && 0 <= c2 && c2 < M && !check[r2][c2] && condo[r2][c2]) {
                check[r2][c2] = true;
                dq.emplace_back(r2, c2);
            }
        }
    }

    return cnt;
}

int solution() {
    int ans = 0;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++) {
            if (!check[i][j]&& condo[i][j]) ans = max(ans, bfs(i, j));
        }
    return ans;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    init();
    cout << solution();

    return 0;
}