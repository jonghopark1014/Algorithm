#include<iostream>

using namespace std;

int N, K;
int now = 0, cnt = 0;


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N >> K;
    int arr[N], arr2[N];
    for (int i = 0; i < N; i++) {
        arr[i] = i + 1;
        arr2[i] = -1;
    }
    cout << '<';
    while (true) {
        if (cnt == N) {
            break;
        }
        cnt += 1;
        int tmp = 0;
        while (true) {
            now = now % N;
            if (arr2[now] == -1) {
                tmp += 1;
                if (tmp == K) {
                    break;
                } else {
                    now += 1;
                }
            } else {
                now += 1;
            }
        }
        arr2[now] = cnt;
        if (cnt < N) {
            cout << arr[now] << ',' << ' ';
        } else {
            cout << arr[now] << '>';
        }
    }
    return 0;
}
