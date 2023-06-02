
#include <iostream>

using namespace std;

int a, d, b, e, c, f, x, y;

void input() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> a >> b >> c >> d >> e >> f;
}

void solve() {
    if (a != 0 && b != 0 && d != 0 && e != 0) {
        int bd = b * d;
        int ea = e * a;
        int dc = d * c;
        int fa = f * a;
        
        y = (dc - fa) / (bd - ea);
        x = (c - b * y) / a;
    }
    else if (a == 0) {
        y = c / b;
        x = (f - e * y) / d;
    }
    else if (b == 0) {
        x = c / a;
        y = (f - d * x) / e;
    }
    else if (d == 0) {
        y = f / e;
        x = (c - b * y) / a;
    }
    else if (e == 0) {
        x = f / d;
        y = (c - a * x) / b;
    }
    cout << x << ' ' << y;
}

int main() {
    input();
    solve();

    return 0;
}