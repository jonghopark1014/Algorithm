#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int arr[26] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string word;
    cin >> word;

    for (int i = 0; i < word.length(); i++) {
        if (word[i] == 'a') {
            arr[0] += 1;
        }
        else if (word[i] == 'b') {
            arr[1] += 1;
        }
        else if (word[i] == 'c') {
            arr[2] += 1;
        }
        else if (word[i] == 'd') {
            arr[3] += 1;
        }
        else if (word[i] == 'e') {
            arr[4] += 1;
        }
        else if (word[i] == 'f') {
            arr[5] += 1;
        }
        else if (word[i] == 'g') {
            arr[6] += 1;
        }
        else if (word[i] == 'h') {
            arr[7] += 1;
        }
        else if (word[i] == 'i') {
            arr[8] += 1;
        }
        else if (word[i] == 'j') {
            arr[9] += 1;
        }
        else if (word[i] == 'k') {
            arr[10] += 1;
        }
        else if (word[i] == 'l') {
            arr[11] += 1;
        }
        else if (word[i] == 'm') {
            arr[12] += 1;
        }
        else if (word[i] == 'n') {
            arr[13] += 1;
        }
        else if (word[i] == 'o') {
            arr[14] += 1;
        }
        else if (word[i] == 'p') {
            arr[15] += 1;
        }
        else if (word[i] == 'q') {
            arr[16] += 1;
        }
        else if (word[i] == 'r') {
            arr[17] += 1;
        }
        else if (word[i] == 's') {
            arr[18] += 1;
        }
        else if (word[i] == 't') {
            arr[19] += 1;
        }
        else if (word[i] == 'u') {
            arr[20] += 1;
        }
        else if (word[i] == 'v') {
            arr[21] += 1;
        }
        else if (word[i] == 'w') {
            arr[22] += 1;
        }
        else if (word[i] == 'x') {
            arr[23] += 1;
        }
        else if (word[i] == 'y') {
            arr[24] += 1;
        }
        else if (word[i] == 'z') {
            arr[25] += 1;
        }
    }
    for (int i = 0; i < 26; i++) {
        cout << arr[i] << ' ';
    }

    return 0;
}

