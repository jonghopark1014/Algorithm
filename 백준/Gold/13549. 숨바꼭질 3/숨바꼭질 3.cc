#include <iostream>
#include <queue>

using namespace std;

int N, K, res = 100002;

int main() {
    cin >> N >> K;

    int arr[K + K + 1];
    fill(arr, arr + K + K + 1, K - N + 1);

    if (N - K >= 0) {
        res = N - K;
    }

    else {
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> q;
        q.push({N, 0});

        while(!q.empty()) {
            int loc = q.top().first;
            int cnt2 = q.top().second;
            q.pop();


            for (int i = 0; i < 3; i++) {
                if (i == 2) {
                    int loc2 = loc + 1;
                    if (0 <= loc2 && loc2 < K + K + 1 && arr[loc2] > cnt2 + 1) {
                        arr[loc2] = cnt2 + 1;
                        q.push({loc2, cnt2 + 1});
                    }
                }
                else if (i == 1) {
                    int loc2 = loc - 1;
                    if (0 <= loc2 && loc2 < K + K + 1 && arr[loc2] > cnt2 + 1) {
                        arr[loc2] = cnt2 + 1;
                        q.push({loc2, cnt2 + 1});
                    }
                }
                else if (i == 0) {
                    int loc2 = loc * 2;
                    if (0 <= loc2 && loc2 < K + K + 1 && arr[loc2] > cnt2) {
                        arr[loc2] = cnt2;
                        q.push({loc2, cnt2});
                    }
                }
            }
        }
    }
    if (res == 100002) {
        res = arr[K];
    }
    cout << res;

    return 0;
}