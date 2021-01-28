// 3955
// 사람 수 K ,사탕 수  X
// K * Y = C * Y + 1
// K * Y + C * X = 1    원래 KY - CX 지만 음수를 양수로 바꿀 수 있음
// 구해질 수 있냐는 것이 issue이기 때문. 확장 유클리드 호제법 써야함
// K로 나누는 mod 연산에서 1이 나와야 함. -> K, C의 gcd는 1이 나와야함. 

#include <cstdio>

#define MAX_N   1000000

int nos[MAX_N];
int lgcd[MAX_N];
int rgcd[MAX_N];

typedef long long ll;

ll ee(ll a, ll b){
    ll s, s0 = 1, s1 = 0, t, t0 = 0, t1 = 1, q, r;
    while ( b != 0) {
        q = a / b, r = a % b;
        a = b, b = r;
        s = s0 - q * s1;
        t = t0 - q * t1;
        s0 = s1, s1 = s;
        t0 = t1, t1 = t;
    }
}


int main(){
    //?
}