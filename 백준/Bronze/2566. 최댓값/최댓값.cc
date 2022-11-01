#include<iostream>
#include<bits/stdc++.h>

using namespace std;

int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int maxR = 0, maxC = 0, maxV = 0;
    for (int r = 0; r < 9; r++) {
        for (int c = 0; c < 9; c++) {
            int Num;
            cin >> Num;
            if (Num > maxV) {
                maxV = Num;
                maxR = r;
                maxC = c;

            }
        }
    }
    cout << maxV << endl;
    cout << maxR + 1 << ' ' << maxC + 1;
    return 0;
}
