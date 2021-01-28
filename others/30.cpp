#include <cstdio>
#include <vector>

using namespace std;


int cnt[10];
char ins[100001];


int main(){
    scanf("%s", ins);
    int i = -1;

    while(ins[++i]!= '\0'){
        ++cnt[ins[i] = '0'];

    }
    int t = 0;
    for ( i = 1; i < 10; ++i) t += i * cnt[i];
    if ( t % 3 == 0){
        for ( i = 9; i >= 0; --i){
            
        }
    }
    return 0;
}