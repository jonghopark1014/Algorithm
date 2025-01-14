#include <iostream>

using namespace std;

bool visited[1500][1500];

int x, y, z;
int max_value = 0;
int flag = 0;

void simulate(int a, int b, int c) {
    if ((a == b) && (a == c)) {flag = 1; return;}
    int cnt = 0;
    while (cnt != 3 && flag != 1) {
        cnt++;
        if (cnt == 1) {
            if (a < b) {
                if (!visited[a*2][b-a] && !visited[b-a][a*2]) {
                    visited[a*2][b-a] = true;
                    visited[b-a][a*2] = true;
                    simulate(a * 2, b - a, c);    
                }
            }
            else if (a > b) {
                if (!visited[a-b][b*2] && !visited[b*2][a-b]) {
                    visited[a-b][b*2] = true;
                    visited[b*2][a-b] = true;
                    simulate(a - b, b * 2, c);    
                }
                
            }
        }
        else if (cnt == 2) {
            if (a < c) {
                if (!visited[a*2][c-a] && !visited[c-a][a*2]) {
                    visited[a*2][c-a] = true;
                    visited[c-a][a*2] = true;
                    simulate(a * 2, b, c - a);    
                }
            }
            else if (a > c) {
                if (!visited[a-c][c*2] && !visited[c*2][a-c]) {
                    visited[a-c][c*2] = true;
                    visited[c*2][a-c] = true;
                    simulate(a - c, b, c * 2);    
                }
            }
        }
        else {
            if (b < c) {
                if (!visited[b*2][c-b] && !visited[c-b][b*2]) {
                    visited[b*2][c-b] = true;
                    visited[c-b][b*2] = true;
                    simulate(a, b * 2, c - b);    
                }
            }
            else if (b > c) {
                if (!visited[b-c][c*2] && !visited[c*2][b-c]) {
                    visited[b-c][c*2] = true;
                    visited[c*2][b-c] = true;
                    simulate(a, b - c, c * 2);    
                }
            }
        }
    }
}

int main() {
    cin >> x >> y >> z;
    max_value = x + y + z;
    if (max_value % 3 != 0) {cout << 0; return 0;}
    if (x == y == z) {cout << 1; return 0;}
    simulate(x, y, z);
    if (flag) {cout << 1;}
    else {cout << 0;}
    
    return 0;
}
