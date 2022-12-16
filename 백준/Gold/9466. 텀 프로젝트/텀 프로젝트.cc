#include <iostream>
#include <vector>

using namespace std;

int T;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> T;

    for (int tc = 1; tc < T + 1; tc++) {
        int student, res = 0;
        cin >> student;

        int arr[student + 1], visited[student + 1];

        fill(visited, visited + student + 1, 0);

        for (int i = 1; i < student + 1; i++) {
            cin >> arr[i];
        }


        for (int i = 1; i < student + 1; i++) {
            if (!visited[i]) {
                vector<int> select;
                int cnt = 0, sp = 0, nxt = 0, pre = -1;
                while (true) {
                    if (!cnt) {
                        visited[i] = 1;
                        cnt++;
                        select.push_back(i);
                        sp++;
                        nxt = arr[i];
                    }
                    else {
                        if (visited[nxt]) {
                            if (nxt == select.front()) {
                                res += sp;
                            }
                            else {
                                for (int q = 0; q < select.size(); q++) {
                                    if (nxt == select[q]) {
                                        res += select.size() - q;
                                        break;
                                    }
                                }
                            }
                            break;
                        }
                        else {
                            visited[nxt] = 1;
                            select.push_back(nxt);
                            sp++;
                            nxt = arr[nxt];
                        }
                    }
                }
            }
        }
        cout << student - res << '\n';
    }

    return 0;
}