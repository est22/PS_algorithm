#include <cstdio>
#include <stack>
#include <vector>
#include <deque>

using namespace std;

typedef pair<int,int> pii;

stack<pii> stk;
deque<pii> dq;

int main(){

    int N = 10000, L, n;

    for ( int i = 0; i < N; ++i){
        scanf("%d",&n);
        if(dq.front().second < i - L) dq.pop_front();
        while (dq.back().first >= n) dq.pop_back();
        dq.push_back(make_pair(n,i)); // 내 자신을 넣어줌
        printf("%d\n", dq.front().first); // 계속 찌기어줌
    }
    

    return 0;
}