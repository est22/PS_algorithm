#include <cstdio>
#include <queue>

using namespace std;

int nos[10000]; // 1~2^30, 3,45,3,54,36 
queue<int> que;
bool visited[10000];

void relabeling(){ // 정렬의 응용 ; 유일성 검사, 중복 제거
    int i, p, idx = -1;
    for (i = 0; i < 1000; ++i){
        if (p != nos[i]){
            p = nos[i]
            ++idx;
        }
    }

}

void bfs(int S){
    que.push(S);
    visited[S] = true;

    for (!que.empty()){
        int cur = que.front();
        for (int nxt:adjs[cur]){
            if (!visited[nxt]){
                que.push[nxt];
                visited[nxt] = true;
            }
        }
    }
}
