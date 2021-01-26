#include <cstdio>

typedef long long ll;

ll D[10000];

ll fibo(int n){ // 무조건 순서 구성을 이렇게! 연습은 이렇게. stack overflow 발생, top-down?
    // 1. 기저조건
    if (n == 0) return 0;
    else if(n == 1) return 1;

    // 2. memoization
    if (D[n] > 0) return D[n];

     // 3. 점화식
    D[n] = fibo(n - 1) + fibo(n - 2);
    return D[n];
}
// 최종적으로는 배열로 바꿔준다. 이렇게 구현을 해야 stack overflow가 안남.
ll dp2(int n){
    // 기저조건
    D[0] = 0, D[1] = 1;
    // 점화식을 이용
    for (int i = 2; i <= n; ++i) D[i] = D[i - 1] + D[i - 2];
    // 해당 값 반환
    return D[n];
}
int main(){
    
    return 0;
}
