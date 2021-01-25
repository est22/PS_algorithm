#include <cstdio>
#include <algorithm>

using namespace std;

#define MAX_N   100000

int N, locs[MAX_N], ans;

void backtracking(int idx){
    if (idx == N) {
        ++ans;
        return;
    }

    bool chk[MAX_N];
    for (int i = 0; i < N ; ++i) chk[i] = true;
    for (int i = 0; i < idx ; ++i) {
        chk[locs[i]] = false; //체크된 곳은 못감
        int t = locs[i] + (idx - i) ;
        if (t < N) chk[t] = false;
        t = locs[i] - (idx - 1);
        if (t >= 0) chk[t] = false;
    }

    for (int i = 0; i < N ; ++i){
        if (chk[i]){
            locs[idx] = i;
            backtracking(idx + 1);
            
        }
    }
    
}

int main(){
    int M, i, n;

    return 0;
}