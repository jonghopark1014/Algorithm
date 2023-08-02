#include <iostream>
#include <vector>

using namespace std;

int tc, N, M, W, a, b, c;
vector<vector<int>> edge;

const int INF = 1e9;

void input() {
    cin >> N >> M >> W;

    for (int i = 0; i < M + W; i++) {
        cin >> a >> b >> c;
        if (i < M) {
            edge.push_back({a, b, c});
            edge.push_back({b, a, c});
        }
        else {
            edge.push_back({a, b, -1 * c});
        }
    }
}

bool solution(int start) {
    // 그래프 정보 만들기
    int dist[N + 1];
    for (int i = 0; i <= N; i++) {
        dist[i] = INF;
    }
    dist[start] = 0;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M + M + W; j++) {
            int cur = edge[j][0];
            int next = edge[j][1];
            int cost = edge[j][2];
            if (dist[next] > dist[cur] + cost) {
                dist[next] = dist[cur] + cost;
                if (i == N - 1) {
                    return true;
                }
            }
        }
    }
    return false;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> tc;
    for (int i = 0; i < tc; i++) {
        input();
        bool negative = solution(1);
        if (negative) cout << "YES" << '\n';

        else cout << "NO" << '\n';
        edge.clear();
    }



    return 0;
}