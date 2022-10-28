#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int T;
    cin >> T;
    for (int tc = 1; tc < T + 1; tc++) {
        int day;
        cin >> day;
        vector<int> day_lst(day);
        for (int i = 0; i < day; i++) {
            cin >> day_lst[day - i - 1];
        }
        int maxV = 0;
        long long benefit = 0;
        for (int j = 0; j < day; j++) {
            if (j == 0) {
                maxV = day_lst[j];
            } else {
                if (maxV > day_lst[j]) {
                    benefit += maxV - day_lst[j];
                } else {
                    maxV = day_lst[j];
                }
            }
        }
        cout << "#" << tc << " " << benefit << endl;
    }
    return 0;
}