#include <iostream>

using namespace std;

int dr[4] = {0, 0, -1, 1};
int dc[4] = {1, -1, 0, 0};
int T, N, coreCnt = 0, minLen = 0, maxCore = 0, nowLen = 0, nowCore = 0;
int arr[12][12], arrR[12], arrC[12];

void cancelAll(int r, int c, int tmp, int dir, int cnt) {
    int r2 = r + dr[dir], c2 = c + dc[dir];
    if (0 <= r2 && r2 < N && 0 <= c2 && c2 < N && arr[r2][c2] == tmp) {
        arr[r2][c2] = 0;
        cancelAll(r2, c2, tmp, dir, cnt + 1);
    }
    else {
        nowLen -= cnt;
        if (cnt) {
            nowCore -= 1;
        }
    }
}

void cancelM(int r, int c, int tmp, int dir) {
    int r2 = r, c2 = c;
    while (true) {
        r2 -= dr[dir];
        c2 -= dc[dir];
        if (0 <= r2 && r2 < N && 0 <= c2 && c2 < N && arr[r2][c2] == tmp) {
            arr[r2][c2] = 0;
        } else {
            break;
        }
    }
}

void install(int r, int c, int tmp, int dir, int cnt) {
    int r2 = r + dr[dir], c2 = c + dc[dir];
    if (0 <= r2 && r2 < N && 0 <= c2 && c2 < N && arr[r2][c2] == 0) {
        arr[r2][c2] = tmp;
        install(r2, c2, tmp, dir, cnt + 1);
    }
    else if (0 > r2 || r2 >= N || 0 > c2 || c2 >= N) {
        nowCore += 1;
        nowLen += cnt;
    }
    else {
        cancelM(r2, c2, tmp, dir);
    }
}

void search(int cnt, int nl, int nc, int tmpP) {
    if (cnt == coreCnt) {
        if (maxCore < nc) {
            maxCore = nc;
            minLen = nl;
        }
        else if (maxCore == nc) {
            if (minLen > nl) {
                minLen = nl;
            }
        }
        return;
    }
    else if (maxCore > nc + (coreCnt - cnt)) {
        return;
    }
    else {
        for (int i = 0; i < 4; i ++) {
            install(arrR[cnt], arrC[cnt], tmpP, i, 0);
            search(cnt + 1, nowLen, nowCore, tmpP + 1);
            cancelAll(arrR[cnt], arrC[cnt], tmpP, i, 0);
        }
    }
}

void undo() {
    N = 0, coreCnt = 0, minLen = 0, maxCore = 0, nowLen = 0, nowCore = 0;
    int arr[12][12] = {0, }, arrR[12] = {0, }, arrC[12] = {0, };
}

int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> T;
    for (int tc = 1; tc < T + 1; tc++) {
        int num;
        cin >> N;
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                cin >> num;
                arr[r][c] = num;
                if (num == 1 && 1 <= r && r <= N - 2 && 1 <= c && c <= N - 2) {
                    arrR[coreCnt] = r;
                    arrC[coreCnt] = c;
                    coreCnt += 1;
                }
            }
        }
        search(0, nowLen, nowCore, 2);
        cout << '#' << tc << ' ' << minLen << endl;
        undo();
    }

    return 0;
}