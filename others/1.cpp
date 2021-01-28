#include <cstdio>
#include <vector>

using namespace std;

int main(){
    int n, cnt, t;

    while (~scanf("%d",&n)){
        t = 1, cnt = 1;
        while (true){
            if (t % n == 0 )break;
            t %= n;
            t = t*10 + 1;
            ++cnt;

        }
        printf("%d\n",cnt);
    }
    return 0;
}