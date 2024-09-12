#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int arr[9];
int res = 0;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int num;
    cin >> num;

    while (num > 0) {
        if (num % 10 < 9) {
            arr[num % 10] += 1;
            num /= 10;
        }
        else {
            arr[6] += 1;
            num /= 10;
        }
    }
    if (arr[6] > 0) {
        if (arr[6] % 2) {
            arr[6] = arr[6] / 2 + 1;
        }
        else {
            arr[6] = arr[6] / 2;
        }
    }

    for (int i = 0; i < 9; i++) {
        res = max(arr[i], res);
    }
    cout << res;

    return 0;
}

