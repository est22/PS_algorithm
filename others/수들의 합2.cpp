#include <cstdio>

using namespace std;
#define MAX_N   10000

int nos[MAX_N], N, M;

int main(){
    int sum = 0, ans = 0;
    int i , front = -1, end = -1;

    scanf("%d %d", &N &M);
    for(i = 0; i < N; ++i) scanf("%d", nos+i);

    while (end < N){
        if (sum < M){
            ++end;
            sum ++ nos[end];
        }
        else if (sum == M){
            ++ans;
            sum -= nos[front];
            ++front;
        }
        else{
            sum -= nos[front];
            ++front;
        }
    }

    return 0;
}