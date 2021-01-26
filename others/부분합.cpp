#include <cstdio>

using namespace std;
#define MAX_N   10000
#define INF     1000000000

int nos[MAX_N],S;

int main(){
    int sum = 0, ans = INF;
    int i , start = 0, end = -1;

    scanf("%d %d", &N &S);
    for(i = 0; i < N; ++i) scanf("%d", nos+i);

    while (end < N){
        if (sum < S){
            ++end;
            sum ++ nos[end];
        }
        
        else{
            if (end-start < ans) ans = end - start + 1;
            sum -= nos[start];
            ++start;
        }
    }

    return 0;
}