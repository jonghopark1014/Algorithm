#include <iostream>

using namespace std;

int M, N;
int arr[8];
int check[9];

void input() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    // M, N 받기
    cin >> M >> N;
}

void recur(int m, int n, int cnt) {
    if (cnt == n) {
        for (int i = 0; i < n; i++) {
            cout << arr[i] << ' ';
        }
        cout << '\n';
        return;
    }
    for (int i = 1; i < m + 1; i++) {
        if (check[i] == 0) {
            check[i] = 1;
            arr[cnt] = i;
            recur(m, n, cnt + 1);
            check[i] = 0;
        }
    }
}

int main() {
    input();
    recur(M, N, 0);

    return 0;
}