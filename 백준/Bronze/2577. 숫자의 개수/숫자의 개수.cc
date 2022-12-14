#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int arr[10];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int a, b, c;
    cin >> a >> b >> c;

    int res = a * b * c;
    while (res > 0) {
        arr[res % 10] += 1;
        res /= 10;
    }

    for (int i = 0; i < 10; i++) {
        cout << arr[i] << '\n';
    }

    return 0;
}

