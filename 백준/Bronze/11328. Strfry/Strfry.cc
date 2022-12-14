#include <iostream>

using namespace std;

int cnt, arr[26];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> cnt;
    
    for (int i = 0; i < cnt; i++) {
        string str1, str2;
        cin >> str1 >> str2;
        int tf = 1;
        if (str1.length() != str2.length()) {
            tf = 0;
        }
        else {
            for (int j = 0; j < str1.length(); j++) {
                arr[str1[j] - 'a'] += 1;
            }
    
            for (int k = 0; k < str2.length(); k++) {
                if (arr[str2[k] - 'a'] == 0) {
                    tf = 0;
                    break;
                }
                else {
                    arr[str2[k] - 'a'] -= 1;
                }
            }
        }
        if (tf) {
            cout << "Possible" << '\n';
            fill(arr, arr+26, 0);
        }
        else {
            cout << "Impossible" << '\n';
            fill(arr, arr+26, 0);
        }
    }
}