#include <iostream>

using namespace std;

int N,M, k;
int arr[22][22];
int tmp[22][22];
//int shark_direction[401];
int shark_priority[1000][5][5];

int smell_remain[22][22];               // 냄새가 남아있는 시간
int smell_number[22][22];               // 특정 상어의 냄새

int dr[] = {0,-1,1,0,0};
int dc[] = {0,0,0,-1,1};


void move_shark(int r, int c, int *shark_direction) { // 항상 방향은 우선순위를 가진 방향 기준임

    int num = arr[r][c];                // 상어 번호
    int dir = shark_direction[num];     // 상어 현재 방향

    // 인접한 곳 중에서 아무 냄새가 없는 경우
    for (int i = 1; i <= 4; i++){
        int pri_d = shark_priority[num][dir][i]; // 상어 우선순위 방향
        int nr = r + dr[pri_d];
        int nc = c + dc[pri_d];

        if (nr >= 0 && nr < N && nc >= 0 && nc < N) {
            if (smell_remain[nr][nc] == 0){
                // 상어가 움직이는 공간에 값이 비어있으면 상어 그대로 두기, 아니면 작은 상어만 살아남기
                if (tmp[nr][nc] == 0) {
                    // 상어의 위치 이동
                    tmp[r][c] = 0;
                    tmp[nr][nc] = num;
                    shark_direction[num] = pri_d;           // 이동한 방향이 상어의 다음 방향이 됨.
                    return;
                }
                    // 비어있지 않은 경우
                else {
                    if (num < tmp[nr][nc]){
                        // 상어의 위치 이동
                        tmp[r][c] = 0;
                        tmp[nr][nc] = num;
                        shark_direction[num] = pri_d;           // 이동한 방향이 상어의 다음 방향이 됨.
                        return;
                    }
                }
                return;                                 // return 위치가 여기인 이유 : 빈 공간으로 어찌되었던 이동했으니까.
            }
        }
    }

    // 냄새가 나는 곳으로 이동
    for (int i = 1; i <= 4; i++) {
        int pri_d = shark_priority[num][dir][i]; // 상어 우선순위 방향
        int nr = r + dr[pri_d];
        int nc = c + dc[pri_d];
        if (nr >= 0 && nr < N && nc >= 0 && nc < N) {
            if (smell_number[nr][nc] == num) {
                // 상어의 위치 이동
                tmp[r][c] = 0;
                tmp[nr][nc] = num;
                shark_direction[num] = pri_d;           // 이동한 방향이 상어의 다음 방향이 됨.
                return;
            }
        }
    }

}

void smell() {
    for (int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            // 상어의 위치에는 k로 냄새를 남김
            if (arr[i][j] != 0) {
                smell_remain[i][j] = k;
                smell_number[i][j] = arr[i][j];
            }
                // 기존에 남아있던 냄새는 -1 씩 감소
            else if (smell_remain[i][j] > 0) {
                smell_remain[i][j] -= 1;
                if (smell_remain[i][j] == 0) {
                    smell_number[i][j] = 0;
                }
            }
        }
    }

}

void move(int *shark_direction) {
    // 방향에 맞게 상어 이동
    for (int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            if (arr[i][j] != 0) {
                move_shark(i,j, shark_direction);
            }
        }
    }
    // 임시로 저장된 상어 값을 다시 원래 배열로 복귀
    for (int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            arr[i][j] = tmp[i][j];
        }
    }

    // 이동 후 냄새를 좌표에 남김.
    smell();

    //tmp 초기화
    for (int r = 0; r < N; r++) {
        for (int c = 0; c < N; c++) {
            tmp[r][c] = 0;
        }
    }
}


int main() {
    cin >> N >> M >> k;
    // 초기값 설정 : 상어 위치 선정(배열)
    for (int i = 0; i < N; i++) {
        for (int j=0; j < N; j++) {
            cin >> arr[i][j];

        }
    }
    // 초기값 설정 :  냄새
    for (int i=0; i<N; i++) {
        for (int j = 0; j < N; j++) {
            // 상어의 위치에는 k로 냄새를 남김
            if (arr[i][j] != 0) {
                smell_remain[i][j] = k;
                smell_number[i][j] = arr[i][j];
            }
        }
    }

    // 상어의 초기 방향 입력
    int shark_direction[1000];

    for (int i=1; i <=M; i++){
        cin >> shark_direction[i];
    }
    // 상어 번호별 방향 우선 순위 선정
    for (int i=1; i<=M; i++) {
        for (int j=1; j<=4; j++) {
            for (int l=1; l<=4; l++) {
                cin >> shark_priority[i][j][l];
            }
        }
    }

    // 이동
    int cnt = 1;
    while (cnt <= 1000) {
        // 상어 이동
        move(shark_direction);
        // 상어 1마리 남았는지 체크
        int chk = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (arr[i][j] != 0) {
                    chk++;
                }
            }
        }

        // 종료조건
        if (chk == 1) {
            cout << cnt;
            break;
        }
        cnt++;


    }

    if (cnt == 1001) {
        cout << -1;
    }
}