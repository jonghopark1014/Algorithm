#include <iostream>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int tc = 1; tc < T + 1; tc++) {
        int a;
        int b;
        cin >> a;
        cin >> b;
        if (a > b) {
            cout << "#" << tc << " " << ">" << endl;
        }
        else if (a == b) {
            cout << "#" << tc << " " << "=" << endl;
        } else {
            cout << "#" << tc << " " << "<" << endl;
        }
    }
    return 0;
}