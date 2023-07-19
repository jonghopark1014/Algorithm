#include <iostream>

using namespace std;

long long int N, dp[1000001];

int main() {
    cin >> N;
    dp[0] = 0;
    dp[1] = 0;
    dp[2] = 1;
    for (int i = 3; i <= N; i++) {
        dp[i] = ((i - 1) * dp[i - 1] + (i - 1) * dp[i - 2]) % 1000000000;
    }
    cout << dp[N];

    return 0;
}