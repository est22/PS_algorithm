#include <cstdio>
#include <vector>

using namespace std;

#define MAX_N 10000

int ep[MAX_N +1]


int main(){
    int i, j;
    for (int i = 2 ; i <= MAX_N; ++i) ep[i] = i;
    
    for ( i = 2; i <= MAX_N; ++i){
        if ( i == ep[i]){
            for (j = i;j-max_n;j+= i)
        }
    }

    {
        if (!flag[i]){
            primes.push_back(i);
            for(long long j = (long long)i + i; j <= 10000000; j += 1) flag[j] = true;
        }
    }
    return 0;
}