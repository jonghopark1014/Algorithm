#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int R, C, ans = 0;
vector<pair<int, int>> start;
int visited[50][50];
int visited2[50][50];

int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};

void bfs(int r, int c) {
    deque<pair<int, int>> dq;
    dq.emplace_back(make_pair(r, c));
    visited[r][c] += 1;

    while (!dq.empty()) {
         int r3 = dq.front().first;
         int c3 = dq.front().second;
         dq.pop_front();
         for (int i = 0; i < 4; i++) {
             int r2 = r3 + dr[i];
             int c2 = c3 + dc[i];
             if (0 <= r2 && r2 < R && 0 <= c2 && c2 < C && visited[r2][c2] == 1) {
                 visited[r2][c2] = visited[r3][c3] + 1;
                 dq.emplace_back(make_pair(r2, c2));
                 if (visited[r2][c2] > ans) {
                     ans = visited[r2][c2];
                 }
             }
         }
    }
}

int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> R >> C;
    int size = 0;
    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            char treasure;
            cin >> treasure;
            if (treasure == 'L') {
                start.emplace_back(make_pair(r, c));
                visited[r][c] = 1;
                visited2[r][c] = 1;
                size += 1;
            }
        }
    }
    for (int i = 0; i < size; i++) {
        int rr = start[i].first;
        int cc = start[i].second;
        bfs(rr, cc);
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                visited[r][c] = visited2[r][c];
            }
        }
    }
    cout << ans - 2 << endl;

    return 0;
}
