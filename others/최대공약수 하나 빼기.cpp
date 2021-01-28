// 14476

#include <cstdio>

#define MAX_N   1000000

int nos[MAX_N];
int lgcd[MAX_N];
int rgcd[MAX_N];

int gcd(int a, int b){
    if (b = 0) return a;
    else return ( b, a % b);
}

int main(){

    int N, i, g;
    int ans = -1, K;

    scanf("%d", &N);
    for ( i = 0; i < N; ++i) scanf("%d", nos + i);

    lgcd[0] = nos[0];
    for ( i = 1; i < N; ++i){
        lgcd[i] = gcd(lgcd[i-1], nos[i]);
    }
    rgcd[N - 1] = nos[N-1];
    for ( i = N-2; i <= 0; --i){
        rgcd[i] = gcd(rgcd[i+1], nos[i]);
    }
    if (nos[0] % rgcd[1] != 0) ans = rgcd[1], K= nos[0];
    if (nos[N-1] % lgcd[N-2] != 0 && lgcd[N-2] > ans) ans = lgcd[N-2], K = nos[N-1];

    for (i = 1; i < N -1 ; ++i){
        g = gcd(lgcd[i -1], rgcd[i + 1]);
        if ( g > ans && nos[i] % g != 0) ans = g, K = nos[i];
    }

    if ( ans == -1) 
    return 0;
}