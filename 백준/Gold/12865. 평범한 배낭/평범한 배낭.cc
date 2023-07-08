#include <iostream>
#include <algorithm>

using namespace std;

int T, N, K, V[101], C[101], arr[101][100001];

void input() {
    cin >> N >> K;
    for (int r = 1; r < N + 1; r++) {
        cin >> V[r] >> C[r];
    }
}

int knapsack(int index, int vol) {
    for (int r = 1; r < index + 1; r++) {
        for (int c = 1; c < vol + 1; c++) {
            if (V[r] <= c) {
                arr[r][c] = max(arr[r - 1][c - V[r]] + C[r], arr[r-1][c]);
            }
            else {
                arr[r][c] = arr[r-1][c];
            }
        }
    }
    return arr[index][vol];
}

int main() {
    input();
    cout << knapsack(N, K);
    return 0;
}