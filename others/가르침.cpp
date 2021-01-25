#include <cstdio>
#include <queue>
#include <vector>

using namespace std;

#define MAX_N   50
#define SZ_CH   26 //알파벳 최대 개수

int words[SZ_CH][MAX_N]; //작은 것을 앞에
int N, K, ans = 0;
bool sels[SZ_CH];

int count(){

}
void backtracking(const int& k, const const int& loc){
    if (k == K){
        int t = count();
        if(t > ans) ans = t;
        return;
    }
    for (int i = loc; i < SZ_CH; ++i){
        if (!sels[i]){
            sels[i] = true;
            backtracking(k + 1, i + 1);
            sels[i] = false;
        }
    }

}
int main() {
    char ins[16];
    int j;

    scanf("%d %d", &N, &K);
    for (int i = 0; i < N; ++i){
        scanf("%s", ins);
        j = -1;
        while (ins[++j] != '\0'){
            ++words[ins[j] - 'a' ][i]; //i번째 문자의 캐릭터가 a보다 크면 증가시킴
        }
    }
    backtracking(0, 0);

    return 0;
}