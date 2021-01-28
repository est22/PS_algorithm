//11653
#include <cstdio>
#include <vector>

using namespace std;


int main(){

    int n, i;
    scanf("%d", &n);
    for ( i = 2; i * i <= n ; ++i){
        while(n % i == 0){
            printf("%d\n", i);
            n /= i;
        }
    }
    if ( n > 1) printf("%d\n",n); //함정?!
    return 0;
}