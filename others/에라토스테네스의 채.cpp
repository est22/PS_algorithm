#include <cstdio>
#include <vector>

using namespace std;

bool flag[1000001];
vector<int> primes;

int main(){
    for (int i = 0 ; i <= 1000000; i++){
        if (!flag[i]){
            primes.push_back(i);
            for(long long j = (long long)i + i; j <= 10000000; j += 1) flag[j] = true;
        }
    }
    return 0;
}