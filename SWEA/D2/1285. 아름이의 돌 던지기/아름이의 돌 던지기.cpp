#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int T;
    cin >> T;
    for (int tc = 1; tc < T + 1; tc++) {
        int N;
        cin >> N;
        int minV;
        int ans = 0;
        for (int i = 0; i < N; i++) {
            int value;
            cin >> value;
            if (i == 0) {
                minV = abs(value);
                ans += 1;
            } else {
                if (minV > abs(value)) {
                    minV = abs(value);
                    ans = 1;
                } else if (minV == abs(value)) {
                    ans += 1;
                }
            }
        }
        cout << '#' << tc << ' ' << minV << ' ' << ans << endl;
    }
}