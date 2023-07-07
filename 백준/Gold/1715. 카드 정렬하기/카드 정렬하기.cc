#include <iostream>
#include <queue>

using namespace std;

int N, ans;
priority_queue<int, vector<int>, greater<>> pq;

void input() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N;
    for (int i = 0; i < N; i++) {
        int num = 0;
        cin >> num;
        pq.push(num);
    }
}

void sum_card() {
    while (!pq.empty()) {
        if (pq.size() == 1) {
            pq.pop();
        }
        else {
            int num1 = pq.top();
            pq.pop();
            int num2 = pq.top();
            pq.pop();
            ans += num1 + num2;
            if (!pq.empty()) {
                pq.push(num1 + num2);
            }
        }
    }
}

int main() {
    input();
    sum_card();
    cout << ans;

    return 0;
}