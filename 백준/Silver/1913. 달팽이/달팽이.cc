#include <iostream>
using namespace std;

int arr[999][999];

int dr[4] = {1, 0, -1, 0};
int dc[4] = {0, 1, 0, -1};

int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int N, target, sqN, r = -1, c = 0, dir = 0, target_r, target_c;
    cin >> N >> target;
    sqN = N * N;
    while (true) {
        r = r + dr[dir];
        c = c + dc[dir];
        if (0 <= r && r < N && 0 <= c && c < N && !arr[r][c]) {
            arr[r][c] = sqN;
            if (target == sqN) {
                target_r = r + 1;
                target_c = c + 1;
            }
            sqN -= 1;
            if (sqN == 0) {
                break;
            }
        }
        else {
            r -= dr[dir];
            c -= dc[dir];
            dir = (dir + 1) % 4;
        }
    }
    for (int rr = 0; rr < N; rr++) {
        for (int cc = 0; cc < N; cc++) {
            cout << arr[rr][cc] << ' ';
        }
        cout << '\n';
    }
    cout << target_r << ' ' << target_c;
    return 0;
}