#include <cstdio>
#include <vector>
#include <utility>
#include <algorithm>
#include <cstring>
#include <queue>

using namespace std;
int n,m,start,dest; // n <= 500     n^250000
int u, v, p;

int adjMat[505][505];
int dist[505];

//다익스트라 함수
void getShortestPath(){
    memset(dist, -1, sizeof(dist));
    priority_queue<pair<int,int>> pq;
    pq.push(make_pair(0,start));
    while ( ! pq.empty()){
        auto temp =  pq.top(); pq.pop();
        int here = temp.second; int cost = temp.first;
        if(dist[here]!= -1) continue;
        dist[here] = cost;
        for (int next = 0; next < n; next++){
            if (adjMat[here][next] == -1) continue;
            if(dist[next] != -1) continue;
            pq.push(make_pair(cost+adjMat[here][next],next));
        }
    }
}
//최단경로 제거하는 함수
void removeShortestPath(){
    queue <int> q;
    q.push(dest); // 거꾸로 돌며 일치하는 지점을 찾아나갈것이다.
    while (q.size()){
        int tmp = q.front();q.pop();
        for (int prev = 0; prev < n; i ++){
            if (adjMat[prev][tmp] == -1) continue; // 이전지점부터 현재까지 오는데 길이 없다면.
            if (dist[tmp] == dist[prev] + adjMat[prev][tmp]){
                //최단경로임
                adjMat[prev][tmp] == -1;
                q.push(prev);
            }
        }
    }
}
int main(){

    while (1){
        scanf("%d %d", &n, &m);
        if (n == 0 && m == 0) break;
        for (int i = 0; i < 505; i ++){
            for (int j = 0; j < 505; j++){
                adjMat[i][j] = -1 ;// -1이 길이 없다는 뜻
            }
        }
        memset(adjMat, -1, sizeof(adjMat));
        scanf("%d %d", &start, &dest);
        for (int i = 0; i < m; i ++){
            scanf("%d %d %d", &u, &v, &p);
            adjMat[u][v] = p;
        }
        getShortestPath();
        removeShortestPath();
        getShortestPath();
        printf("%d\n", dist[dest]);
    }
}