#include <cstdio>
#include <algorithm>
#include <vector>
#include  <queue> // BFS?

using namespace std;

#define MAX_N   50
typedef pair<int,int> pii;

int N,K, maps[MAX_N][MAX_N], types[MAX_N][MAX_N]; // 매번 new를 하게 되면 속도 면에서 손해를 본다. 여러 테스트케이스를 동시에 똘리기때문!
int seq, visited[MAX_N][MAX_N];
vector<int> heights;
int ans = 100000000;
pii S;
int mvX[8] = {-1, -1, -1, 0, 0, 1, 1, 1}, mvY[8]={-1, 0, 1, -1, 1, -1, 0, 1};
bool check(int low, int high){
    queue<pii> que;

    que.push(S);
    ++seq;
    int k;

    visited[S.first][S.second] = seq;
    que.push(S);
    while(!que.empty()){
        pii cur = que.front();
        que.pop();
        if(types[cur.first][cur.second] == 2) {
            ++k;
            if (k == K) break;
        }
        for (int i = 0; i < 8; ++i){
            pii next;
            next.first = cur.first + mvX[i];
            next.second = cur.second + mvY[i];
            if (next.first < 0 || .... || visited[][] != seq) continue;
            visited[][] = seq;
            que.push(next);

        }
    }

    return (k == K);
}

int main(){
    for (int i = 0; i<N; ++i){
        for(int j = 0; j < N ; ++j){
        scanf("%d", &maps[i][j]);
        heights.push_back(maps[i][j]);

        }
    }
    sort(heights.begin(), heights.end());
    int low = 0, high = 0;

    while (high < heights.size()){
        if (check(heights[low], heights[high])){
            if(heights[high]-heights[low]<ans)ans = heights[high]
            ++low;
        }
        else{
            ++high;
        }
    }
    return 0;
}