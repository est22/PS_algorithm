#include <cstdio>
#include <queue>
#include <vector>

using namespace std;

#define MAX_N   50

int maps[MAX_N][MAX_N];
int mvX[4] = {-1,1,0,0}, mvY[4] = {0,0,-1,1};
bool visited[MAX_N][MAX_N];
int R, C; //row, column

int backtracking(int r, int c){
    if (r < 0 || r >= R || c < 0 || c >= C || maps[r][c] == 0 ) return 0; //maps[r][c] :구멍
    if (visited[r][c]) return -1;

    visited[r][c] = false;
    //몰라.....

    int s = 0;
    for (int i = 0 ; i < 4; ++i){
        int t = backtracking(r + mvX[i]+maps[r][c], c+mvY[i]*maps[r][c]);
        if (t == -1) return -1;
        if (t > s) s = t;
    }
    return s + 1;
}

int main(){
    return 0;
}