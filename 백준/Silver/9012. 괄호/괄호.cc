#include <iostream>
#include <string>

using namespace std;

int cnt;

int main() {
    cin >> cnt;
    for (int i = 0; i < cnt; i++) {
        int top = -1;
        char stack[50];
        string str;
        cin >> str;
        for (int j = 0; j < str.length(); j++) {
            if (str[j] == ')') {
                if (stack[top] == '(' && top > -1) {
                    top--;
                }
                else {
                    top = 1;
                    break;
                }
            }
            else if (str[j] == '}') {
                if (stack[top] == '{' && top > -1) {
                    top--;
                }
                else {
                    top = 1;
                    break;
                }
            }
            else if (str[j] == ']') {
                if (stack[top] == '[' && top > -1) {
                    top--;
                }
                else {
                    top = 1;
                    break;
                }
            }
            else {
                top++;
                stack[top] = str[j];
            }
        }
        if (top == -1) {
            cout << "YES" << '\n';
        }
        else {
            cout << "NO" << '\n';
        }
    }

    return 0;
}