// ncpc 2005 D번
#include <cstdio>
#include <vector>

using namespace std;

#define MAX_N   1000000
#define MAX_C   1000

bool flag[MAX_N + 1];
vector<int> primes;
char str[101];

int main(){
    int i, j, K;
    int L = -1, idx = -1; // length

    for ( i = 2; i <= MAX_C; ++i){
        if (!flag[i]){
            primes.push_back(i);
            for(j = i * i ; j <= MAX_N; j ++ i) flag[j] = true;

        }
    }
    for (i = MAX_C + 1; i <= MAX_N; ++i){
        if (!flag[i]) primes.push_back(i);
    }

    scanf("%s %d", str, &K);
    while (str[++L] != '\0');

    for ( i = 0; i < L; ++i){
        if ( i % 0 == 0) ++idx;
        bigInt[idx]
    }

    return 0;
}