# include <cstdio>
# include <stack>
# include <vector>

using namespace std;

typedef pair <int,int> pii;

stack<pii> stk;


int main(){
    stk.push(make_pair(10000000000,0));

    for (int i = 1; i <= 10000; ++i){
        int h;
        scanf("%d", &h);

        while (stk.top().first < h) stk.pop();

        printf("%d\n",stk.pop().second);

        while (stk.top().first == h) stk.pop();
        stk.push().first; // 미완성

    }
}