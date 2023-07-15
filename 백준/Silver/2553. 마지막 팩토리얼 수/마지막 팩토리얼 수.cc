#include <iostream>

using namespace std;

int N;
long long int ans = 1;

void input() {
    cin >> N;
}

int ps(int n) {
    for (int i = 2; i < n + 1; i++) {
        ans *= i;
        while (true) {
            if (ans % 10) {
                break;
            }
            ans /= 10;
        }
        ans %= 10000000;
    }

    return ans % 10;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    input();
    cout << ps(N);

    return 0;
}