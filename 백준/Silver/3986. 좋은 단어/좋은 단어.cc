#include <iostream>

using namespace std;

int cnt, res;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> cnt;

    for (int i = 0; i < cnt; i++) {
        char arr[100000];
        int top = -1;
        string str;
        cin >> str;
        for (int j = 0; j < str.length(); j++) {
            if (j == 0) {
                arr[top] = str[j];
                top++;
            }
            else {
                if (arr[top-1] == str[j]) {
                    top--;
                }
                else {
                    arr[top] = str[j];
                    top++;
                }
            }
        }
        if (top == -1) {
            res += 1;
        }
    }
    cout << res;

    return 0;
}