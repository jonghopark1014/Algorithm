#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int dr[8] = {-1, -1, 0, 1, 1, 1, 0, -1};
int dc[8] = {0, 1, 1, 1, 0, -1, -1, -1};

// pre_move 파이어볼 움직이기 전, moved 움직인 후
queue<vector<int>> pre_move;
vector<vector<int>> moved;

// arr 파이어볼 갯수 체크
int arr[50][50], N, M, K, res;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M >> K;
    for (int i = 0; i < M; i++) {
        vector<int> tmp_input;
        for (int j = 0; j < 5; j++) {
            int tmp_num;
            cin >> tmp_num;
            if (j < 2) {
                tmp_input.push_back(tmp_num - 1);
            }
            else {
                tmp_input.push_back(tmp_num);
            }
        }
        arr[tmp_input[0]][tmp_input[1]] += 1;
        // vector 인자 r, c, m(질량), s(속력), d(방향)
        pre_move.push(tmp_input);
    }

    int try_cnt = 0;
    while (try_cnt <= K) {
//        for (int r5 = 0; r5 < N; r5++) {
//            for (int c5 = 0; c5 < N; c5++) {
//                cout << arr[r5][c5] << ' ';
//            }
//            cout << '\n';
//        }
        if (try_cnt == K) {
            while (!pre_move.empty()) {
                int m = pre_move.front()[2];
//                cout << '\n' << m << '\n';
                pre_move.pop();
                res += m;
            }
            break;
        }
//        cout << '\n';

        // 먼저 이동
        while (!pre_move.empty()) {
            int r = pre_move.front()[0];
            int c = pre_move.front()[1];
            int m = pre_move.front()[2];
            int s = pre_move.front()[3];
            int d = pre_move.front()[4];
            pre_move.pop();
            arr[r][c] -= 1;
            int r2 = r + dr[d] * s;
            int c2 = c + dc[d] * s;
            if (0 <= r2 && r2 < N && 0 <= c2 && c2 < N) {
                ;
            }
            else if (0 <= r2 && r2 < N) {
                if (c2 < 0) {
                    while (c2 < 0) {
                        c2 += N;
                    }
                }
                else {
                    while (c2 >= N) {
                        c2 -= N;
                    }
                }
            }
            else if (0 <= c2 && c2 < N) {
                if (r2 < 0) {
                    while (r2 < 0) {
                        r2 += N;
                    }
                }
                else {
                    while (r2 >= N) {
                        r2 -= N;
                    }
                }
            }
            else {
                if (r2 < 0) {
                    if (c2 < 0) {
                        while (r2 < 0) {
                            r2 += N;
                        }
                        while (c2 < 0) {
                            c2 += N;
                        }
                    }
                    else {
                        while (r2 < 0) {
                            r2 += N;
                        }
                        while (c2 >= N) {
                            c2 -= N;
                        }
                    }
                }
                else {
                    if (c2 < 0) {
                        while (r2 >= N) {
                            r2 -= N;
                        }
                        while (c2 < 0) {
                            c2 += N;
                        }
                    }
                    else {
                        while (r2 >= N) {
                            r2 -= N;
                        }
                        while (c2 >= N) {
                            c2 -= N;
                        }
                    }
                }
            }
            vector<int> tmp_vec = {};
            tmp_vec.push_back(r2); tmp_vec.push_back(c2); tmp_vec.push_back(m); tmp_vec.push_back(s); tmp_vec.push_back(d);
            moved.push_back(tmp_vec);
            arr[r2][c2] += 1;
        }
        // 파이어볼 2개있는지 체크(2개 이상이면 로직 실행)
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                if (arr[r][c] > 1) {
                    int tmp_cnt = 0;
                    int check = 0;
                    int mod = 0;
                    int tmp_m = 0;
                    int tmp_s = 0;

                    for (int i = 0; i < moved.size(); i++) {
                        if (moved[i][0] == r && moved[i][1] == c) {
                            if (tmp_cnt == 0) {
                                mod = moved[i][4] % 2;
                                tmp_cnt++;
                            }
                            else {
                                if (check == 0) {
                                    if (mod != moved[i][4] % 2) {
                                        check = 1;
                                    }
                                }
                            }
                            tmp_m += moved[i][2];
                            tmp_s += moved[i][3];
                            moved[i][0] = 99;
                        }
                    }
                    int new_s = tmp_s / arr[r][c];
                    int new_m = tmp_m / 5;
                    arr[r][c] = 0;
                    if (new_m > 0) {
                        if (check == 1) {
                            int add_arr[4] = {1, 3, 5, 7};
                            for (int k = 0; k < 4; k++) {
                                vector<int> tmp_pre;
                                tmp_pre.push_back(r);
                                tmp_pre.push_back(c);
                                tmp_pre.push_back(new_m);
                                tmp_pre.push_back(new_s);
                                tmp_pre.push_back(add_arr[k]);
                                pre_move.push(tmp_pre);
                                arr[r][c] += 1;
                            }
                        }
                        else {
                            int add_arr[4] = {0, 2, 4, 6};
                            for (int k = 0; k < 4; k++) {
                                vector<int> tmp_pre;
                                tmp_pre.push_back(r);
                                tmp_pre.push_back(c);
                                tmp_pre.push_back(new_m);
                                tmp_pre.push_back(new_s);
                                tmp_pre.push_back(add_arr[k]);
                                pre_move.push(tmp_pre);
                                arr[r][c] += 1;
                            }
                        }
                    }
                }
            }
        }
        if (!moved.empty()) {
            // 최종 결과물 pre_move에 넣기
            for (int i = 0; i < moved.size(); i++) {
                if (moved[i][0] != 99) {
                    pre_move.push(moved[i]);
                }
            }
        }
        moved = {};
        try_cnt += 1;
    }
    cout << res;

    return 0;
}