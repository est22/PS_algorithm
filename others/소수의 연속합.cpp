// 1644
#include <cstdio>
#include <vector>

using namespace std; // 하면 vector 활성화되는 이유?


#define MAX_N   4000000
#define MAX_C   2000

bool flag[MAX_N + 1];
vector<int> primes;

int main(){
    int i, j, N, s = 0; //s = sum
    int cnt;

    for ( i = 2; i <= MAX_C, ++i;){
        if (!flag[i]){
            primes.push_back(i);
            for ( j = i * i; j <= MAX_N; j += i) flag[j] = true;

        }
    }
    for (i = MAX_C + 1; i <= MAX_N, ++i;){
        if (!flag[i]) primes.push_back(i);
    }
    i = 0; j = 0;
    while ( j < primes.size()) {
        if ( s < N) s += primes[j++];
        else if (s > N) s -= primes[i++];
        else{
            ++cnt;
            s -= primes[i++];
        }
    }
    return 0;
}