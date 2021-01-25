#include <cstdio>
// 최소 한개의 모음과 한개의 자음을 어떻게 할 것인가?
int tp[26] = { 1, 0, 0, 0, 1, 0, 0, 0, 1,0, 0, 0, 0,0,0,1,0};
int L, C, chs[15];
char ans[16];

void backtracking(int loc, int cnt, int cnt1, int cnt2) {
    if (cnt == L) {
        if (cnt1 > 0 && cnt2 > 1) printf("&s\n", ans); //모음 1, 자음 2개 이상일 경우 출력
        return;
    }
    if (loc == C) return;
    for (int i = loc; i < C; ++i){
        ans[cnt] = chs[i] + 'a';
        backtracking(i + 1, cnt + 1, cnt1 + 1 ? 0; cnt2 + 1 ? 0);
    }

}

int main(){

    ans[L] = '\n';
    backtracking(0,0,0,0);
    
    return  0;
}