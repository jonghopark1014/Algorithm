#include <iostream>

using namespace std;

int n, m, type, a, b, arr[1000001];

int func_find(int num) {
    if (num == arr[num]) return num;
    return arr[num] = func_find(arr[num]);
}

void func_union(int x, int y) {
    x = func_find(x);
    y = func_find(y);

    if (x != y) arr[x] = y;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n >> m;

    for (int j = 0; j < n + 1; j++) {
        arr[j] = j;
    }
    for (int i = 0; i < m; i++) {
        cin >> type >> a >> b;
        if (!type) {
            func_union(a, b);
        }
        else {
            if (func_find(a) != func_find(b)) cout << "NO\n";
            else cout << "YES\n";
        }
    }

    return 0;
}