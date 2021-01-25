#include <cstdio>
#include <algorithm>

using namespace std;

#define MAX_N   100000

int N, nos[MAX_N];

int getIndex(int n){
    int low = 0, high = N-1, mid;

    while (low <= high) {
        mid = (low + high) / 2;
        if (nos[mid] <= n) low = mid - 1;
        else high = mid + 1;
    } // 소스가 짧고 단순해ㅐ서 활용도가 높다.

    return low + 1; //주어진 숫자 중 작거나 같은 것 중 제일 큰 것?
}
int main(){
    int M, i, n;

    scanf("%d", &N);
    for (i = 0; i < N; ++i) scanf("%d", nos+i);
    sort(nos, nos+N);

    scanf("%d", &M);
    while (M--){
        scanf("%d",&n);
        i = getIndex(n);
        if ( i >= 0 && nos[i] == n) printf("1\n");
        else printf("0\n");
    }
    return 0;
}