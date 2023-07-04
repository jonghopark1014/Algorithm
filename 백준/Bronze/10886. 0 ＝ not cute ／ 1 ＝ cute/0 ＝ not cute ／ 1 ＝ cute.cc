#include <iostream>

using namespace std;

int yesno[2];
int n;

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        int tmp;
        cin >> tmp;
        yesno[tmp] += 1;
    }
    if (yesno[0] > yesno[1]) {
        cout << "Junhee is not cute!";
    }
    else {
        cout << "Junhee is cute!";
    }

    
    return 0;
}