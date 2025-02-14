#include <iostream>
#include <unordered_map>
#include <vector>
#include <deque>

using namespace std;

int N, M, x;

unordered_map<int, vector<int>> low;
unordered_map<int, vector<int>> high;
int chk[100001];
int low_chk[100001];
int high_chk[100001];

int low_ans, high_ans;

int main() {

    cin >> N >> M >> x;

    low_ans = 1;
    high_ans = N;
    
    for (int i = 0; i < M; i++) {
        int s, e;
        cin >> s >> e;
        chk[s] = 1;
        chk[e]= 1;
        
        if (low.count(s)) {
            low[s].push_back(e);
        }
        else {
            low.insert({s, {e}});
        }
        if (high.count(e)) {
            high[e].push_back(s);
        }
        else {
            high.insert({e, {s}});
        }
    }

    if (chk[x] != 0) {
        deque<int> low_dq = {};
        int tmp_low = 0;
        deque<int> high_dq = {};
        int tmp_high = 0;
        
        low_chk[x] = 1;
        for (int i = 0; i < low[x].size(); i++) {
            low_dq.push_front(low[x][i]);
        }

        while (low_dq.size()) {
            int next = low_dq.front();
            low_dq.pop_front();
            if (low_chk[next] != 1) {
                low_chk[next] = 1;
                tmp_low++;
                for (int i = 0; i < low[next].size(); i++) {
                    low_dq.push_front(low[next][i]);
                }
            }
        }
        high_ans = N - tmp_low;

        high_chk[x] = 1;
        for (int i = 0; i < high[x].size(); i++) {
            high_dq.push_front(high[x][i]);
        }

        while (high_dq.size()) {
            int next = high_dq.front();
            high_dq.pop_front();
            if (high_chk[next] != 1) {
                high_chk[next] = 1;
                tmp_high++;
                for (int i = 0; i < high[next].size(); i++) {
                    high_dq.push_front(high[next][i]);
                }
            }
        }

        low_ans = tmp_high + 1;
    }

    cout << low_ans << ' ' << high_ans;
    
    return 0;
}