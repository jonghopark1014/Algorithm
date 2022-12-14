#include <iostream>

using namespace std;

int arr[202];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int len;

    cin >> len;

    for (int i = 0; i < len; i++) {
        int num;
        cin >> num;
        arr[num + 100] += 1;
    }

    int target;
    cin >> target;

    cout << arr[target + 100];

    return 0;
}