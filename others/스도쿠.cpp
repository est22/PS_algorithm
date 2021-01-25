#include <cstdio>
#include <algorithm>

using namespace std;

bool HSels[9][10], VSels[9][10], BSels[9][10];
int sdk[9][9];

bool backtracking(int x, int y){
    if (y == 9) ++x, y = 0;
    if (x == 9) return true;
    if (sdk[x][y] != 0) return backtracking(x, y+1);

    bool res = false;
    int b = (x / 3) * 3 + y / 3; //box 찾기

    for (int i = 1; i <= 9; ++i){
        if (!HSels[x][i] && !VSels[y][i] && !BSels[b][i]){ // 선택이 안된 경우에만
            sdk[x][y] = i;
            HSels[x][i] = VSels[y][i] = BSels[b][i] = true;
            if (backtracking(x,y+1)){
                res = true;
                break;
            }
            HSels[x][i] = VSels[y][i] = BSels[b][i] = false;
            sdk[x][y] = 0;
        }
    }

    return res;
}


int main(){
    int x, y, n;

    for(x = 0; x < 9; ++x){
        for (y = 0; y < 9 ; ++y){
            scanf("%d",&sdk[x][y]);
            if (sdk[x][y] != 0){
                HSels[x][sdk[x][y]] = true;
                VSels[y][sdk[x][y]] = true;
                //박스를 3으로 나눠준다
                BSels[(x / 3) * 3 + y / 3][sdk[x][y]] = true;
            }
        }
    }

    if(backtracking(0,0)) printf("found it!");

    return 0;
}