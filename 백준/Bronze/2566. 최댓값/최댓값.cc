#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    int maxNum = 0, maxNumR = 0, maxNumC = 0, num, R = 0, C = -1;
    for (int i = 0; i < 81; i++) {
        cin >> num;
        C += 1;
        if (C > 8) {
            C = 0;
            R += 1;
        }
        if (num > maxNum) {
            maxNum = num;
            maxNumR = R;
            maxNumC = C;
        }
    }
    cout << maxNum << '\n';
    cout << maxNumR + 1 << ' ' << maxNumC + 1;


    return 0;
}