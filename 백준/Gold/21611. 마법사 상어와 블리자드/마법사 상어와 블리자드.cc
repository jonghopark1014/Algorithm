#include <iostream>
#include <map>

using namespace std;

int N, M, res[4], result;
map<int, pair<int, int>> number_map;

int dr2[] = {0, 1, 0, -1}, dc2[] = {1, 0, -1, 0};

int dr[] = {0, -1, 1, 0, 0}, dc[] = {0, 0, 0, -1, 1};

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N >> M;

    pair<int, int> shark;
    shark.first = (N - 1) / 2;
    shark.second = (N - 1) / 2;

    int max_num = N * N - 1;

    int arr[N][N];
    pair<int, int> ds[M];

    for (int r = 0; r < N; r++) {
        for (int c = 0; c < N; c++) {
            cin >> arr[r][c];
            if (r == (N - 1) / 2 && c == (N - 1) / 2) {
                arr[r][c] = 9;
            }
        }
    }

    for (int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        ds[i] = {a, b};
    }

    int tmp_arr[N][N];
    for (int r = 0; r < N; r++) {
        for (int c = 0; c < N; c++) {
            tmp_arr[r][c] = 0;
        }
    }


    int basic_r = 0;
    int basic_c = -1;
    int basic_dir = 0;
    while (true) {
        if (max_num == 0) {
            break;
        }
        int basic_r2 = basic_r + dr2[basic_dir];
        int basic_c2 = basic_c + dc2[basic_dir];
        if (0 <= basic_r2 && basic_r2 < N && 0 <= basic_c2 && basic_c2 < N && tmp_arr[basic_r2][basic_c2] == 0) {
            number_map.insert({max_num, {basic_r2, basic_c2}});
            tmp_arr[basic_r2][basic_c2] = 1;
            basic_r = basic_r2, basic_c = basic_c2;
            max_num--;
        }
        else {
            basic_dir = (basic_dir + 1) % 4;
        }
    }

    for (int i = 0; i < M; i++) {
        // 블리자드
        int tmp_d = ds[i].first;
        int tmp_s = ds[i].second;
        int tmp_bli_r = shark.first;
        int tmp_bli_c = shark.second;
        for (int s = 0; s < tmp_s; s++) {
            tmp_bli_r += dr[tmp_d];
            tmp_bli_c += dc[tmp_d];
            arr[tmp_bli_r][tmp_bli_c] = 0;
        }
//        cout << "---------" << i << "-----------" << '\n';
//
//        cout << "---bli---" << '\n';
//        for (int r = 0; r < N; r++) {
//            for (int c = 0; c < N; c++) {
//                cout << arr[r][c] << ' ';
//            }
//            cout << '\n';
//        }
//        cout << '\n';

        // 구슬 채우기
        int basic_num = 1;
        int comp_num = 2;
        while (true) {
            if (comp_num > N * N - 1) {
                break;
            }
            int tmp_r = number_map[basic_num].first;
            int tmp_c = number_map[basic_num].second;
            if (arr[tmp_r][tmp_c] == 0) {
                int comp_r = number_map[comp_num].first;
                int comp_c = number_map[comp_num].second;
                if (arr[comp_r][comp_c] == 0) {
                    comp_num++;
                }
                else {
                    arr[tmp_r][tmp_c] = arr[comp_r][comp_c];
                    arr[comp_r][comp_c] = 0;
                    basic_num++, comp_num++;
                }
            }
            else {
                basic_num++, comp_num++;
            }
        }

//        cout << "1st_fill" << '\n';
//        for (int r = 0; r < N; r++) {
//            for (int c = 0; c < N; c++) {
//                cout << arr[r][c] << ' ';
//            }
//            cout << '\n';
//        }
//        cout << '\n';

        // 구슬 4개이상 폭발
        while (true) {
            int check = 0;
            int marble_num = 0;
            int marble_stack = 0;
            for (int b_num = 1; b_num < N * N; b_num++) {
                if (b_num == 1) {
                    marble_num = arr[number_map[b_num].first][number_map[b_num].second];
                    marble_stack++;
                } else {
                    if (marble_num == arr[number_map[b_num].first][number_map[b_num].second] && marble_num > 0) {
                        marble_stack++;
                    } else {
                        if (marble_stack > 3 && marble_num > 0) {
                            check = 1;
                            res[marble_num] += marble_stack;
                            for (int k = b_num - 1; k > b_num - marble_stack - 1; k--) {
                                arr[number_map[k].first][number_map[k].second] = 0;
                            }

                            marble_num = arr[number_map[b_num].first][number_map[b_num].second];
                            marble_stack = 1;
                        } else {
                            marble_num = arr[number_map[b_num].first][number_map[b_num].second];
                            marble_stack = 1;
                        }
                    }
                }
            }
//            cout << "burn!" << '\n';
//            for (int r = 0; r < N; r++) {
//                for (int c = 0; c < N; c++) {
//                    cout << arr[r][c] << ' ';
//                }
//                cout << '\n';
//            }
//            cout << '\n';


            // 터진 부분 메우기
            if (check == 1) {
                int basic_num2 = 1;
                int comp_num2 = 2;
                while (true) {
                    if (comp_num2 == N * N) {
                        break;
                    }
                    int tmp_r2 = number_map[basic_num2].first;
                    int tmp_c2 = number_map[basic_num2].second;
                    if (arr[tmp_r2][tmp_c2] == 0) {
                        int comp_r2 = number_map[comp_num2].first;
                        int comp_c2 = number_map[comp_num2].second;
                        if (arr[comp_r2][comp_c2] == 0) {
                            comp_num2++;
                        } else {
                            arr[tmp_r2][tmp_c2] = arr[comp_r2][comp_c2];
                            arr[comp_r2][comp_c2] = 0;
                            basic_num2++, comp_num2++;
                        }
                    } else {
                        basic_num2++, comp_num2++;
                    }
                }
//                cout << "second_fill" << '\n';
//                for (int r = 0; r < N; r++) {
//                    for (int c = 0; c< N; c++) {
//                        cout << arr[r][c] << ' ';
//                    }
//                    cout << '\n';
//                }
//                cout << '\n';
            }
            else {
                break;
            }
        }
        // 구슬 복제
        int comp_arr[N][N];

        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                comp_arr[r][c] = 0;
            }
        }

        int rule = 1;
        int comp_arr_num = 1;
        int marble_num = 0;
        int marble_stack = 0;
        for (int b_num = 1; b_num < N * N; b_num++) {
            if (b_num == 1) {
                marble_num = arr[number_map[b_num].first][number_map[b_num].second];
                marble_stack++;
            }
            else {
                if (marble_num == arr[number_map[b_num].first][number_map[b_num].second]) {
                    marble_stack++;
                }
                else {
                    comp_arr[number_map[comp_arr_num].first][number_map[comp_arr_num].second] = marble_stack;
                    if (comp_arr_num < N * N) {
                        comp_arr[number_map[comp_arr_num + 1].first][number_map[comp_arr_num + 1].second] = marble_num;
                    }
                    rule += 2;
                    comp_arr_num += 2;
                    marble_num = arr[number_map[b_num].first][number_map[b_num].second];
                    marble_stack = 1;
                }
                if (rule > N * N - 2) {
                    break;
                }
            }
        }
//        cout << "------result" << '\n';
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                arr[r][c] = comp_arr[r][c];
//                cout << arr[r][c] << ' ';
            }
//            cout << '\n';
        }
    }
    cout << 1 * res[1]+ 2 * res[2] + 3 * res[3];

    return 0;
}