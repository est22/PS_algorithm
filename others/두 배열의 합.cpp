#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

#define MAX_N   1000

int A[MAX_N], B[MAX_N];
vector<int> subA, subB;

int main(){
    int T, N, M, i, j, ans;

    scanf("%d", &N);
    for (i = 0; i < N; ++i){
        scanf("%d", A+i);

    }
    for (i = 0; i < N; ++i){
        s = 0;
        for (j = i; j < N; ++j){
            s += A[j]; // 처음에는 s에 i가 들어오지만 
            subA.push_back(s);
        }
    }
    scanf("%d", &M);
    for (i = 0; i < M; ++i){
        scanf("%d", B + i);
    }
    for (i = 0; i < N; ++i){
        s = 0;
        for (j = i; j < N; ++j){
            s += B[j]; // 처음에는 s에 i가 들어오지만 
            subB.push_back(s);
        }
    }
sort(subA.begin(), subA.end());
sort(subB.begin(), subB.end());

i = 0; j = subB.size() -1;
while(i < subA.size() && j >= 0){
    if (subA[i] + subB[j] > T) --j;
    else if (subA[i] + sub[j] < T) ++i;
    else{
        int t = subA[i], cnt = 0;
        while (i < subA.size() && subA[i] == t) ++cnt, ++i;
        int cnt2 = 0;
        while (j >=0 && subB[j] == t) ++cnt2, --j;
        ans += cnt1 * cnt2;
    }
}
return 0;
}

