#include <iostream>
#include <queue>

using namespace std;

int N, M, ans, parent[200002];

struct line {
    int start, end, len;

    bool operator<(const line& l1) const {
        return len > l1.len;
    }
};

int findRoot(int spot) {
    if (parent[spot] == spot) return spot;
    return parent[spot] = findRoot(parent[spot]);
}

void unionRoot(int a, int b) {
    if (a != b) parent[b] = a;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N >> M;

    priority_queue<line> pq;

    for (int i = 0; i < M; i++) {
        int start, end, len;
        cin >> start >> end >> len;
        line l = {start, end, len};
        pq.push(l);
    }

    for (int i = 1; i <= N + 1; i++) {
        parent[i] = i;
        if (i == N + 1) continue;
        int start = i;
        int end = N + 1;
        int len;
        cin >> len;
        line l = {start, end, len};
        pq.push(l);
    }

    while (!pq.empty()) {
        line l = pq.top();
        pq.pop();
        int start = findRoot(l.start);
        int end = findRoot(l.end);
        if (start != end) {
            unionRoot(start, end);
            ans += l.len;
        }
    }
    cout << ans;

    return 0;
}