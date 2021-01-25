#include <cstdio>
#include <queue> //배열을 통해 할 수도 있는데 더 어려울 것 같아서
#include <vector> //위치정보를 사용하기 위해

using namespace std;

#define MAX_n   50
#define INF     100000000

typedef pair<int,int> pii;

int mins[MAX_n][MAX_n];
int mvX[4] = {-1,1,0,0}, mvY[4] = {0,0,-1,1};
queue<pii> que;
vector <pii> waters;
int X, Y;

void bfsWater(){
    int x, y, nx, ny;
    int i;

    for (i=0; i<waters.size(); ++i) que.push(waters[i]);
    while (!que.empty()){
        pii cur = que.front(); que.pop();
        for (i = 0; i < 4; ++i){
            nx = cur.first + mvX[i], ny = cur.second + mvY[i];
            if (nx < 0 || nx >= X || ny < 0 || ny >= Y) continue; // out of range
            if (mins[nx][ny] > mins[cur.first][cur.second] + 1){
                mins[nx][ny] = mins[cur.first][cur.second] + 1;
                que.push(make_pair(nx,ny));
            }
        }
    }

}


int main(){
    int X, Y;
    int x, y;
    char ins[MAX_n + 1];

    for (x=0; x < X; ++x){
        scanf("%s",ins);
        for (y=0; y<Y; ++y){
            if (ins[y] == '*') mins[x][y] = 0;
            else if (ins[y] == 'X') mins[x][y] = -1;
            else if (ins[y] == 'S') mins[x][y] = 0;
            else mins[x][y] = INF; // overflow가 일어날 수 있기 때문에 적당히 큰값을 잡아서 세팅.
        }
    }
    return 0;
}
