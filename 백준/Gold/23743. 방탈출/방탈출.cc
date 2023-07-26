#include <iostream>
#include <queue>

using namespace std;

struct room {
    int origin, next, val;
};

struct compare {
    bool operator()(const room& r1, const room& r2) {
        return r1.val > r2.val;
    }
};

int arr[200002], N, M;

priority_queue<room, vector<room>, compare> pq;

void input() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N >> M;
    for (int i = 1; i <= N; i++) {
        arr[i] = i;
    }
    for (int j = 0; j < M; j++) {
        room tmp;
        cin >> tmp.origin;
        cin >> tmp.next;
        cin >> tmp.val;
        pq.push(tmp);
    }
    for (int k = 1; k <= N; k++) {
        room tmp2;
        tmp2.origin = k;
        tmp2.next = N + 1;
        cin >> tmp2.val;
        pq.push(tmp2);
    }
}

int find_root(int a) {
    if (arr[a] == a) return a;
    return arr[a] = find_root(arr[a]);
}

void union_root(int a, int b) {
    a = find_root(a);
    b = find_root(b);
    if (a != b) arr[b] = a;
}

void ps() {
    int time = 0;
    int cnt = 0;

    while (cnt != N) {
        room line = pq.top();
        pq.pop();
        if (find_root(line.origin) != find_root(line.next)) {
            time += line.val;
            cnt += 1;
            union_root(line.origin, line.next);
        }
    }
    cout << time;
}

int main() {
    input();
    ps();


    return 0;
}