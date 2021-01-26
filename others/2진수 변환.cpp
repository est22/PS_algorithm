#include <cstdio>
// 거듭제곱을 분할정복으로 빠르게 계산하기
typedef long long ll;

ll multi(ll a, ll b){
    if (b == 0) return 1;
    else if (b ==1) return a;

    ll res = multi(a, b/2);
    res *= res;
    if (b % 2 == 1) res*= a;
    return res;
}

int main(){
    ll a, b;
    ll ans = 1; //합을 처음에 1로 초기화

    ll t = b / 2; //반으로 나눔
    ll s = multi(a,t);

    while(b > 0){
        if (b & 1 ) ans * a; //bit 연산
        b >>= 1; //bit 연산
        a *= a;
    }



    return 0;
}