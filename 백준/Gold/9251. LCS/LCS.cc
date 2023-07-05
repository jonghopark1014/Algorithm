#include <iostream>
#include <algorithm>

using namespace std;

string A;
string B;

int ans;

void input() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> A >> B;
}

int bottom_up() {
    int arr[A.length() + 1][B.length() + 1];

    for (int r = 0; r < A.length() + 1; r++) {
        for (int c = 0; c < B.length() + 1; c++) {
            if (r == 0 || c == 0) {
                arr[r][c] = 0;
            }
            else {
                if (A[r - 1] == B[c - 1]) {
                    arr[r][c] = arr[r - 1][c - 1] + 1;
                }
                else {
                    arr[r][c] = max(arr[r - 1][c], arr[r][c - 1]);
                }
            }
        }
    }

    return arr[A.length()][B.length()];
}

int main() {
    input();
    cout << bottom_up();

    return 0;
}