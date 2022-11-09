#include<iostream>
#include<bits/stdc++.h>

using namespace std;

list<char> arr;
int N;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    string word;
    cin >> word;
    for (auto w: word) {
        arr.push_back(w);
    }
    auto now = arr.end();
    cin >> N;
    for (int i = 0; i < N; i++) {
        char a;
        cin >> a;
        if (a == 'P') {
            char b;
            cin >> b;
            arr.insert(now, b);
        }
        else if (a == 'B') {
            if (now != arr.begin()) {
                now --;
                now = arr.erase(now);
            }
        }
        else if (a == 'L') {
            if (now != arr.begin()) {
                now --;
            }
        }
        else if (a == 'D') {
            if (now != arr.end()) {
                now ++;
            }
        }
    }
    for (auto c : arr) {
        cout << c;
    }
    return 0;
}
