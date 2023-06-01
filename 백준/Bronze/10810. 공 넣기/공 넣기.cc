#include <iostream>

using namespace std;

int N, M;
int basket[101];

void input() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M;
}

void putBall(int m) {
    int i, j, k;
    for (int idx = 0; idx < m; idx++) {
        cin >> i >> j >> k;
        for (int l = i; l < j + 1; l++) {
            basket[l] = k;
        }
    }
}

void answer(int n) {
    for (int i = 1; i < n + 1; i++) {
        cout << basket[i] << ' ';
    }
}

int main() {
    input();
    putBall(M);
    answer(N);
}