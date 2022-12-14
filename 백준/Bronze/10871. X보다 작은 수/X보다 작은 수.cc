#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int a, b;
    cin >> a >> b;
    for (int i = 0; i < a; i++) {
        int tmp;
        cin >> tmp;
        if (tmp < b) {
            cout << tmp << ' ';
        }
    }

    return 0;
};