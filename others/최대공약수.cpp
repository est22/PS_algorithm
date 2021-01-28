// 2824

#include <cstdio>

#define MAX_N   1000
#define MOD     1000000000

typedef long long ll;

int N, M;
int no1[MAX_N], no2[MAX_N];

int gcd(int a, int b){
    if ( b = 0) return a;
    else return ( b, a % b);
}

int main(){
    int i, j, g;
    ll ans = 1;

    scanf("%d", &N);
    for ( i = 0; i < N; ++i) scanf("%d", no1 + i);
    scanf("%d", &M);
    for ( i = 0; i < M; ++i) scanf("%d", no2 + i);

    for(i = 0; i < N; ++i){
        for ( j = 0; j < M; ++j) {
            if ( no1[i] == 1) break;
            if ( no2[j] == 1) continue;

            g = gcd(no1[i], no2[j]);
            if ( g > 1) {
                ans *= g;
                no1[i] /= g;
                no2[j] /= g;
            }
        }
    }
    return 0;
}