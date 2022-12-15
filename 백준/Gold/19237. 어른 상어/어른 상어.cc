#include <iostream>
#include <vector>

using namespace std;

int N, M, K;
int dr[5] = {0, -1, 1, 0, 0}, dc[5] = {0, 0, 0, -1, 1};

void smell(vector<vector<pair<int, int>>> &smell_vec, vector<vector<pair<int, int>>> &shark_vec) {
    for (int r = 0; r < N; r++) {
        for (int c = 0; c < N; c++) {
            if (shark_vec[r][c].first) {
                smell_vec[r][c].first = shark_vec[r][c].first;
                smell_vec[r][c].second = K;
            }
        }
    }
}

void move(vector<vector<pair<int, int>>> &shark_vec, vector<vector<pair<int, int>>> &smell_vec, vector<pair<int, int>> &shark_location, vector<vector<vector<int>>> &shark_dir) {
    for (int i = 1; i < M + 1; i++) {
        int r = shark_location[i].first;
        if (r == 99) {
            continue;
        }
        int c = shark_location[i].second;
        int dir = shark_vec[r][c].second;

        vector<vector<int>> my_smell_location(4, vector<int>(3, 0));
        int try_cnt = 0;
        int tmp_value = -1;

        for (int j = 1; j < 5; j++){
            int new_dir = shark_dir[i][dir][j];
            int r2 = r + dr[new_dir];
            int c2 = c + dc[new_dir];
            if (0 <= r2 && r2 < N && 0 <= c2 && c2 < N) {
                if (smell_vec[r2][c2].first != 0) {
                    if (smell_vec[r2][c2].first == i && tmp_value == -1) {
                        my_smell_location[try_cnt][0] = r2;
                        my_smell_location[try_cnt][1] = c2;
                        my_smell_location[try_cnt][2] = new_dir;
                        tmp_value = try_cnt;
                    }
                    try_cnt++;
                }
                else {
                    if (shark_vec[r2][c2].first != 0) {
                        if (shark_vec[r2][c2].first > i) {
                            int tmp_shark = shark_vec[r2][c2].first;
                            shark_location[tmp_shark].first = 99;
                            shark_location[tmp_shark].second = 99;
                            shark_vec[r2][c2].first = i;
                            shark_vec[r2][c2].second = new_dir;
                        }
                        else {
                            shark_location[i].first = 99;
                            shark_location[i].second = 99;
                        }
                    }
                    else {
                        shark_vec[r2][c2].first = i;
                        shark_vec[r2][c2].second = new_dir;
                        shark_location[i].first = r2;
                        shark_location[i].second = c2;
                    }
                    shark_vec[r][c].first = 0;
                    shark_vec[r][c].second = 0;
                    break;
                }
            }
            else {
                try_cnt++;
            }
        }

        if (try_cnt == 4) {
            int r3 = my_smell_location[tmp_value][0];
            int c3 = my_smell_location[tmp_value][1];
            int dir3 = my_smell_location[tmp_value][2];
            shark_vec[r][c].first = 0;
            shark_vec[r][c].second = 0;
            shark_vec[r3][c3].first = i;
            shark_vec[r3][c3].second = dir3;

            shark_location[i].first = r3;
            shark_location[i].second = c3;
        }
    }
}

void check_shark(vector<vector<pair<int, int>>> &shark_vec, int &check) {
    int shark_cnt = 0;
    for (int r = 0; r < N; r++) {
        for (int c = 0; c < N; c++) {
            if (shark_vec[r][c].first != 0) {
                shark_cnt++;
                if (shark_cnt > 1) {
                    break;
                }
            }
        }
        if (shark_cnt > 1) {
            break;
        }
    }
    if (shark_cnt == 1) {
        check = 1;
    }
}

void turn_off(vector<vector<pair<int, int>>> &shark_vec, vector<vector<pair<int, int>>> &smell_vec) {
    for (int r = 0; r < N; r++) {
        for (int c = 0; c < N; c++) {
            if (!shark_vec[r][c].first && smell_vec[r][c].second) {
                if (smell_vec[r][c].second == 1) {
                    smell_vec[r][c].second = 0;
                    smell_vec[r][c].first = 0;
                }
                else {
                    smell_vec[r][c].second--;
                }
            }
        }
    }
}

int main() {
    cin >> N >> M >> K;

    // shark_first = 초기 방향값 넣기 위한 vector
    // shark_vec 상어 테이블, smell_vec 냄새 테이블
    // shark_dir 상어 방향 우선 순위
    vector<pair<int, int>> shark_location(M + 1, {0, 0});
    vector<vector<pair<int, int>>> shark_vec(N, vector<pair<int, int>>(N, {0, 0}));
    vector<vector<pair<int, int>>> smell_vec(N, vector<pair<int, int>>(N, {0, 0}));
    vector<vector<vector<int>>> shark_dir(M + 1, vector<vector<int>>(5, vector<int>(5, 0)));

    int check = 0;

    // 테이블 정보 가져 오기
    for (int r = 0; r < N; r++) {
        for (int c = 0; c < N; c++) {
            // 상어 정보 넣기(상어 번호, 이동 방향)
            int num;
            cin >> num;
            if (num) {
                shark_location[num].first = r;
                shark_location[num].second = c;
            }
            shark_vec[r][c].first = num;
        }
    }
    // 상어 초기 방향 설정
    for (int i = 1; i < M + 1; i++) {
        int dir;
        cin >> dir;
        shark_vec[shark_location[i].first][shark_location[i].second].second = dir;
    }

    // 상어 별 방향 우선 순위 설정
    for (int i = 1; i < M + 1; i++) {
        for (int j = 1; j < 5; j++) {
            vector<int> arr(4);
            cin >> arr[0] >> arr[1] >> arr[2] >> arr[3];
            shark_dir[i][j][1] = arr[0];
            shark_dir[i][j][2] = arr[1];
            shark_dir[i][j][3] = arr[2];
            shark_dir[i][j][4] = arr[3];
        }
    }
    int cnt = 0;

    while (cnt < 1000) {
        cnt++;
        if (cnt == 1) {
            smell(smell_vec, shark_vec);
        }
        move(shark_vec, smell_vec, shark_location, shark_dir);
        check_shark(shark_vec, check);
        if (check) {
            break;
        }
        turn_off(shark_vec, smell_vec);
        smell(smell_vec,shark_vec);
    }
    if (!check) {
        cnt = -1;
    }
    cout << cnt;

    return 0;
}