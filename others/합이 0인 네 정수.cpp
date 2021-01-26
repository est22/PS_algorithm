#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

#define MAX_N   4000
typedef long long ll;

int A[MAX_N], B[MAX_N], C[MAX_N], D[MAX_N];
vector<int> subA, subB;

int main(){
    int N, i, j;

    scanf("%d", &N);
    for(i = 0; i < N; ++i) scanf("%d %d %d %d", A+i, B+i, C+i, D+i);

    foor (  i = 0; i  < N; ++i){
        for (j = 0; j < N; ++j) subA.push_back(A[i] + B[j]);
    }
    for ( i = 0; i < N; ++i){
        for (j = 0; j < N; ++j) subB.push_back(C[i] + D[j]);
    }
    sort (subA.begin(), subA.end());
    sort (subB.begin(), subB.end());

    return 0;
}
