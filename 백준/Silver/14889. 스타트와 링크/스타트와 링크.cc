#include <iostream>

using namespace std;

int arr[20][20], pick[10], visited[20];
int N, sumA = 0, sumB = 0, ans = 99999999;


void combi(int x) {
    if (x == N / 2) {
        for (int j = 0; j < N / 2; j++) {
            for (int k = 0; k < N / 2; k++) {
                if (j != k) {
                    sumA += arr[pick[j]][pick[k]];
                }
            }
        }
        for (int l = 0; l < N; l++) {
            for (int m = 0; m < N; m++) {
                if (!visited[l] && !visited[m] && l != m) {
                    sumB += arr[l][m];
                }
            }
        }
        int tmpV = sumB - sumA;
        if (tmpV < 0) {
            tmpV *= -1;
        }
        if (tmpV < ans) {
            ans = tmpV;
        }
        sumA = 0;
        sumB = 0;
        return;
    }
    for (int i = 0; i < N; i++) {
        if (!visited[i] && pick[x - 1] <= i) {
            visited[i] = true;
            pick[x] = i;
            combi(x + 1);
            visited[i] = false;
        }
    }
}

int main() {
    cin >> N;
    for (int r = 0; r < N; r++) {
        for (int c= 0; c < N; c++) {
            cin >> arr[r][c];
        }
    }
    combi(0);
    cout << ans;


    return 0;
}