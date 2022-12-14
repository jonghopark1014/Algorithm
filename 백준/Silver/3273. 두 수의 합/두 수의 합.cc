#include <iostream>

using namespace std;

int len, target, num_arr[1000001], res;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> len;
    int arr[len];

    for (int i = 0; i < len; i++) {
        int num;
        cin >> num;
        arr[i] = num;
        num_arr[num] = 1;
    }

    cin >> target;

    for (int i = 0; i < len; i++) {
        if (target - arr[i] <= 1000000 && target - arr[i] > 0) {
            if (num_arr[target - arr[i]] == 1) {
                res++;
            }
        }
    }
    cout << res / 2;
    return 0;
}