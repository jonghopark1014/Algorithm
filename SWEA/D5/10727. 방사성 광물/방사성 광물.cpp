#include <iostream>

using namespace std;

int T, N, M, Q, ans, pre;
pair<int, int> arr[200002];

void input() {
    cin >> N >> M >> Q;
    for (int r = 1; r < N + 1 ; r++) {
        for (int c = 1; c < M + 1; c++) {
            int tmp;
            cin >> tmp;
            if (arr[r].first < tmp) {
                arr[r].first = tmp;
            }
            if (arr[N + c].first < tmp) {
                arr[N + c].first = tmp;
            }
        }
    }
    for (int r = 1; r < N + 1; r++) {
        for (int c = 1; c < M + 1; c++) {
            if (arr[r].first == arr[N + c].first) {
                arr[r].second = c;
                arr[N + c].second = r;
                pre++;
            }
        }
    }
}

void change(int cnt) {
    for (int i = 0; i < cnt; i++) {
				// flag 0 : 아무것도 안바뀜
				// flag 1 : r만 바뀜
				// flag 2 : c만 바뀜
				// flag 3 : r, c 둘다
        int flag = 0;
        int r, c, x;
        cin >> r >> c >> x;
        if (arr[r].first < x) {
            arr[r].first = x;
            flag = 1;
        }
        if (arr[N + c].first < x) {
            arr[N + c].first = x;
            if (flag == 1) {
                flag = 3;
            }
            else {
                flag = 2;
            }
        }
        if (flag == 0) {
            ans += pre;
        }
        else if (flag == 1) {
            if (arr[r].second) {
                arr[N + arr[r].second].second = 0;
                arr[r].second = 0;
                pre--;
            }
            ans += pre;
        }
        else if (flag == 2) {
            if (arr[N + c].second) {
                arr[arr[N + c].second].second = 0;
                arr[N + c].second = 0;
                pre--;
            }
            ans += pre;
        }
        else if (flag == 3) {
            if (arr[r].second == c && arr[N + c].second == r) {
                pre--;
            }
            else {
                if (arr[r].second) {
                    arr[N + arr[r].second].second = 0;
                    pre--;
                }
                if (arr[N + c].second) {
                    arr[arr[N + c].second].second = 0;
                    pre--;
                }
            }
            arr[r].second = c;
            arr[N + c].second = r;
            pre++;
            ans += pre;
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> T;
    for (int tc = 1; tc < T + 1; tc++) {
        input();
        change(Q);
        cout << "#" << tc << ' ' << ans << endl;
        ans = 0;
        pre = 0;
        for (int i = 0; i < N + M + 2; i++) {
            arr[i] = {0, 0};
        }
    }

    return 0;
}