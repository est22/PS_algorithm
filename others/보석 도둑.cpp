#include <cstdio>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

#define MAX_N   300000

typedef pair<int,int> pii;

pii gems[MAX_N];
int bags[MAX_N];
priority_queue<int> pq;

int main(){
    int N, K, i, j;
    long long ans = 0;

    scanf("%d, %d", &N, &K);

    for(i = 0; i < N; ++i) scanf("%d %d", &gems[i].first, &gems[i].second);
    for(i = 0; i < K; ++i) scanf("%d", bags + i);
    
    sort(gems, gems + N);
    sort(bags, bags + K);

    j = 0;
    for (i = 0; i < K; ++i){
        while (j < N && gems[j].first <= bags[i])pq.push(gems[j++].second);
        if (!pq.empty()) ans += pq.top(), pq.pop();
    }
    printf("%lld\n",ans);

    return 0;
}
